from setuptools import setup

VERSION = '0.0.2'


setup(
    name='flask-http2-push',
    version=VERSION,
    url='https://github.com/jdaroesti/flask-http2-push',
    license='MIT',
    author='David Aroesti',
    author_email='david@aroesti.me',
    description="A Flask extension to add http2 server push to your application.",
    download_url='https://github.com/jdaroesti/flask-http2-push/releases/tag/v' + VERSION,
    long_description=__doc__,
    py_modules=['flask_http2_push'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    keywords='flask http2 push',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
