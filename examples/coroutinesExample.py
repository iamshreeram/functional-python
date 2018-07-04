def coro():
    # If yield stores any value to variable, it becomes coroutine
    hello = yield "Hello"
    yield hello


c = coro()
print(next(c))
print(c.send("World"))