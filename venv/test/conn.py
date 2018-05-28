import asyncio, logging

import aiomysql
from aiohttp import web
import asyncio, os, inspect, logging, functools
from urllib import parse
from aiohttp import web

@asyncio.coroutine
def create_pool(loop, **kw):
    print("create database connection pool...");
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw.get('user','root'),
        password=kw.get('password','mysql'),
        db=kw.get('db','flytree'),
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

@asyncio.coroutine
def select(sql):
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql)
        rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs


@asyncio.coroutine
def find():
        rs = yield from select('select * from user')
        if len(rs) == 0:
            return None
        return rs

async def api_get_blog():
    blog = await find();
    print(blog);
    return blog

async def index(a):
    print("a:"+str(a));
    resp = web.Response(body=b'<h1>Awesome</h1>')
    resp.content_type = 'text/html;charset=utf-8'
    await api_get_blog()
    return resp


async def init(loop):
    await create_pool(loop=loop)
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()

loop.run_until_complete(init(loop))
loop.run_forever()
