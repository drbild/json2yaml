#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from os.path import join as pjoin

setup(
    name = 'json2yaml',
    version = '1.2.0',
    author = 'David R. Bild',
    author_email = 'david@davidbild.org',
    keywords = 'yaml json converter ordered order preserving',
    url = 'https://github.com/drbild/json2yaml',
    description = 'Convert JSON to YAML or vice versa, while'
                  ' preserving the order of associative arrays.',
    classifiers = [
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ],
    scripts = [
        pjoin('bin', 'json2yaml'),
        pjoin('bin', 'yaml2json')
    ],
    install_requires = [
        'pyyaml',
        'pyaml',
        'docopt'
    ]
)
