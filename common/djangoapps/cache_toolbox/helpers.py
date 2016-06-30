"""
Helper functions for caching course assets.
"""
from django.core.cache import cache
from opaque_keys import InvalidKeyError


def set_cached_content(content, version=None):
    """
    Stores the given piece of content in the cache, using its location as the key.
    """
    cache.set(unicode(content.location).encode("utf-8"), content, version=version)


def get_cached_content(location, version=None):
    """
    Retrieves the given piece of content by its location if cached.
    """
    return cache.get(unicode(location).encode("utf-8"), version=version)


def del_cached_content(location, version=None):
    """
    Delete content for the given location, as well versions of the content without a run.

    It's possible that the content could have been cached without knowing the course_key,
    and so without having the run.
    """
    def location_str(loc):
        return unicode(loc).encode("utf-8")

    locations = [location_str(location)]
    try:
        locations.append(location_str(location.replace(run=None)))
    except InvalidKeyError:
        # although deprecated keys allowed run=None, new keys don't if there is no version.
        pass

    cache.delete_many(locations, version=version)
