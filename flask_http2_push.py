"""
File: flask_http2_push.py

"""

import json

import flask
import functools

__author__ = 'David Aroesti'

PUSH_MANIFEST = 'push_manifest.json'
manifest_cache = dict()  # Stores the constructed link header


def http2push(manifest=PUSH_MANIFEST):
    """ """
    if not manifest_cache:
        _set_manifest_cache(manifest)

    return _add_link_header(manifest_cache[manifest])


def _set_manifest_cache(manifest):
    global manifest_cache
    with open(manifest) as push_manifest:
        push_urls = json.loads(push_manifest.read())

        # JDAV 11-JAN-2017 Start from second char `[1:]` to avoid double slash
        # i.e., https://mysite.com/ + /some-url = http://mysite.com//some-url
        link_header_value = ['<{host}{url}>; rel=preload; as={type}'.format(
            host=flask.request.url_root,
            url=url[1:],
            type=metadata['type']) for url, metadata in push_urls.iteritems()]

        manifest_cache[manifest] = ','.join(link_header_value)


def _add_link_header(link_header):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            response = flask.make_response(func(*args, **kwargs))
            response.headers['Link'] = link_header

            return response
        return wrapper
    return decorator
