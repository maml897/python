
def add_routes(module_name):
    print(module_name);
    mod = __import__(module_name, globals(), locals())
    print(mod);

    for attr in dir(mod):
        if attr.startswith('_'):
            continue

        fn = getattr(mod, attr)
        if callable(fn):
            method = getattr(fn, '__method__', None)
            path = getattr(fn, '__route__', None)
            if method and path:
                print(method,path);
                #add_route(app, fn)

add_routes('handlers')
