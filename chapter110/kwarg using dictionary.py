def foobar(foo=None, bar=None):   
    return "{}{}".format(foo, bar)
values = {"foo": "foo", "bar": "bar"}
foobar(**values) 
