"""
File: test/test.py

"""
import unittest

import flask
from flask_http2_push import http2push


class FlaskHttp2PushTest(unittest.TestCase):

    def setUp(self):
        self.app = flask.Flask(__name__)
        self.client = self.app.test_client()

        with self.app.test_request_context():
            @self.app.route('/default-manifest')
            @http2push()
            def default_manifest():
                return ''

            @self.app.route('/custom-manifest')
            @http2push('test/custom_manifest.json')
            def custom_manifest():
                return ''

    def test_default_push_manifest(self):
        """
        It should use by default a file called push_manifest.json
        located at the root of the project.
        """

        response = self.client.get('/default-manifest')
        self.assertEqual(response.headers.get('Link'),
                         '<http://localhost/scripts/some_file.js>; rel=preload; as=script')

    def test_custom_push_manifest(self):
        """It should use the user specified push manifest"""

        response = self.client.get('/custom-manifest')
        self.assertEqual(response.headers.get('Link'),
                         '<http://localhost/styles/some_style.css>; rel=preload; as=style')

    def test_multiple_files_manifest(self):
        """It should create one link header with all the dependencies in it"""
        self.skipTest('todo')
