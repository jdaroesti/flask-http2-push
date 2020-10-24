"""
File: flask_http2_push.py

Exposes a decorator `http2push` that can be used on
Flask's view functions.

    @app.route('/')
    @http2push()
    def main():
        return 'hello, world!'

"""

import json

import flask
import functools
import six

__author__ = 'David Aroesti'

PUSH_MANIFEST = 'push_manifest.json'
manifest_cache = dict()  # Stores the constructed link header


def http2push(manifest=PUSH_MANIFEST):
    """
    Creates the Link header needed in order to use http2 server push
    to send resources to the clients on first request.
    This is done, primarily, so new clients can render the app
    as quickly as possible.

    The spec specifies a header with the following characteristics:

        Link: <https://www.dadant.co/static_file.js>; rel=preload; as=script, ...

    The value will be taken from the instance cache or will be created by
    reading the `push_manifest.json` file (slow) and storing the value in the
    cache.

    :param manifest: The path to the push_manifest.json file.
    :return: The response with the http2 server push headers.
    """

    return _add_link_header(manifest)


def _add_link_header(manifest):
    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not manifest_cache.get(manifest):
                _set_manifest_cache(manifest)

            response = flask.make_response(func(*args, **kwargs))
            response.headers['Link'] = manifest_cache[manifest]

            return response

        return wrapper

    return decorator


def _set_manifest_cache(manifest):
    global manifest_cache
    with open(manifest) as push_manifest:
        push_urls = json.loads(push_manifest.read())

        # JDAV 11-JAN-2017 Start from second char `[1:]` to avoid double slash
        # i.e., https://mysite.com/ + /some-url = http://mysite.com//some-url
        link_header_value = ['<{host}{url}>; rel=preload; as={type}'.format(
            host=flask.request.url_root,
            url=url[1:],
            type=metadata['type']) for url, metadata in six.iteritems(push_urls)]

        manifest_cache[manifest] = ','.join(link_header_value)
