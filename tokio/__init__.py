import asyncio
from asyncio.events import BaseDefaultEventLoopPolicy as __BasePolicy

from . import _tokio

__all__ = ('new_event_loop', 'EventLoopPolicy')


class EventLoop(asyncio.AbstractEventLoop):
    def __init__(self):
        self.__loop = _tokio.new_event_loop()

    def current_task(self):
        return self.__loop.current_task()

    def create_future(self):
        return self.__loop.create_future()

    def create_task(self, coro):
        return self.__loop.create_task(coro)

    def time(self):
        return self.__loop.time()

    def millis(self):
        return self.__loop.millis()

    def call_soon(self, callback, *args):
        return self.__loop.call_soon(callback, *args)

    def call_soon_threadsafe(self, callback, *args):
        return self.__loop.call_soon_threadsafe(callback, *args)

    def call_later(self, delay, callback, *args):
        return self.__loop.call_later(delay, callback, *args)

    def call_at(self, when, callback, *args):
        return self.__loop.call_at(when, callback, *args)

    def stop(self):
        return self.__loop.stop()

    def is_running(self):
        return self.__loop.is_running()

    def is_closed(self):
        return self.__loop.is_closed()

    def close(self):
        return self.__loop.close()

    def run_in_executor(self, executor, func, *args):
        return self.__loop.run_in_executor(executor, func, *args)

    def set_default_executor(self, executor):
        return self.__loop.set_default_executor(executor)

    def getaddrinfo(self, host, port, *, family=0, type=0, proto=0, flags=0):
        return self.__loop.getaddrinfo(host, port,
                                       family=family,
                                       type=type,
                                       proto=proto,
                                       flags=flags)

    def get_exception_handler(self):
        return self.__loop.get_exception_handler()

    def set_exception_handler(self, handler):
        return self.__loop.set_exception_handler(handler)

    def get_debug(self):
        return self.__loop.get_debug()

    def set_debug(self, enabled):
        return self.__loop.set_debug(enabled)

    def run_forever(self):
        return self.__loop.run_forever()

    def run_until_complete(self, future):
        return self.__loop.run_until_complete(future)


def new_event_loop():
    return EventLoop()


class EventLoopPolicy(__BasePolicy):
    """Event loop policy."""

    def _loop_factory(self):
        return new_event_loop()
