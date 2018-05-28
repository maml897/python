#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

' url handlers '
import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post
import asyncio, logging

import aiomysql

@get('/')
def index(*,a='bbb'):
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql)
        rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('rows returned: %s' % len(rs))

    lassmates = ['Michael', 'Bob', 'Tracy']
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    return {
        '__template__': 'home.html',
        'name': 'ok'+a,
        'list':lassmates,
        'map':d
    }
