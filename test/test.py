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

    def test_default_push_manifest(self):
        """
        It should use by default a file called push_manifest.json
        located at the root of the project.
        """

        with self.app.test_request_context():
            @self.app.route('/')
            @http2push()
            def default_push_manifest():
                return ''

        with self.app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.headers.get('Link'),
                             '<http://localhost/scripts/push_manifest_example.js>; rel=preload; as=script')

    def test_custom_push_manifest(self):
        """It should use the user specified push manifest"""
        self.skipTest('todo')

    def test_multiple_files_manifest(self):
        """It should create one link header with all the dependencies in it"""
        self.skipTest('todo')
