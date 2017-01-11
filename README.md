# flask-http2-push
[![Build Status](https://travis-ci.org/jdaroesti/flask-http2-push.svg?branch=master)](https://travis-ci.org/jdaroesti/flask-http2-push)
[![pypi](https://img.shields.io/pypi/v/flask-http2-push.svg)](https://pypi.python.org/pypi/flask-http2-push)

***

**Bottom line**: A Flask extension to add HTTP2 server push to your application.

***

This is a drop in library for doing HTTP2 server push with a Flask application. It 
needs a server that supports HTTP2 push, like Google Appengine or Cloudfare.
Once added to your Flask application it will generate the necessary headers
for server push to work.

## Getting started

To install run: 
```bash
pip install flask-http2-push
```

## Usage
You need to create a `push_manifest.json` file (can be named anything you want)
that contains the files you want to push (Appengine currently has a limit of 10 files). 
The file format is very easy:

```json
{
    "/path/to/file-to-push.js": {
        "type": "script",
        "weight": 1
    },
    "/path/to/file-to-push.css": {
        "type": "style",
        "weight": 1
    },
    "/path/to/file-to-push.woff2": {
        "type": "font",
        "weight": 1
    },
    "/path/to/file-to-push.html": {
        "type": "document",
        "weight": 1
    },
}
```

There is a library for automatically generating the file. You can find
it here (https://www.npmjs.com/package/http2-push-manifest).

Once you have your manifest file, you can use the library in your flask 
view functions like so:

```python
import flask
from flask_http2_push import http2push

app = flask.Flask(__name__)

@app.route('/')
@http2push()
def main():
    return 'hello, world!'
```

This will try to find a file named `push_manifest.json` at the root of the
project. If you would like to name the manifest differently or use another
location, you can specify it in the decorator:


```python
@app.route('/')
@http2push('static/my_manifest.json')
def main():
    return 'hello, world!'
```


## Running the tests
```bash
pip install -r requirements.txt
nosetests
```

## Aknowledgements

This library is inspired by the Google Appengine HTTP2 push library (https://github.com/GoogleChrome/http2push-gae).
The explainer document contained within that repo is a very good read if
you want to further explore how HTTP2 push works (https://github.com/GoogleChrome/http2push-gae/blob/master/EXPLAINER.md)

## License

MIT license. See LICENSE.txt for full info.