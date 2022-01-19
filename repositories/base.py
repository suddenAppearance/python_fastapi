import logging

from models.base import create_async_session



def async_execute(one=False):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            executable = func(*args, **kwargs)
            async with create_async_session() as session:
                result = await session.execute(executable)
                await session.commit()
                return result.scalars().first() if one else result.scalars()

        return wrapper

    return decorator


def async_add(func):
    async def wrapper(*args, **kwargs):
        obj = func(*args, **kwargs)
        async with create_async_session() as session:
            session.add(obj)
            await session.commit()

    return wrapper
