import asyncio
import datetime
import random
import types


# Generator based coroutines
@types.coroutine
def my_sleep_func():
    yield from asyncio.sleep(random.randint(0, 5))


# Native coroutines
async def display_date(num, loop, ):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await my_sleep_func()


loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()