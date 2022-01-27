from functools import lru_cache

from core.settings import Settings


@lru_cache(maxsize=None)  # == @cache on python>=3.9
def get_settings():
    return Settings()
