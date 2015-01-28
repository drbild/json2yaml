#!/usr/bin/env python

import os, sys, subprocess, re
from os.path import join as pjoin

try:
    from setuptools import setup, Command
    from setuptools.command.sdist import sdist as _sdist
except ImportError:
    from distutils.core import setup, Command
    from distutils.command.sdist import sdist as _sdist

VERSION_PY = """
# This file is originally generated from Git information by running 'setup.py
# version'. Distribution tarballs contain a pre-generated copy of this file.
__version__ = '%s'
"""

def update_version_py():
    if not os.path.isdir(".git"):
        print "This does not appear to be a Git repository."
        return
    try:
        p = subprocess.Popen(["git", "describe", "--dirty", "--always"],
                             stdout=subprocess.PIPE)
    except EnvironmentError:
        print "unable to run git, leaving json2yaml/_version.py alone"
        return
    stdout = p.communicate()[0]
    if p.returncode != 0:
        print "unable to run git, leaving json2yaml/_version.py alone"
        return
    # we use tags like "v0.5", so strip the prefix
    assert stdout.startswith("v")
    ver = stdout[len("v"):].strip()
    f = open(pjoin('json2yaml', '_version.py'), 'w')
    f.write(VERSION_PY % ver)
    f.close()
    print "set _version.py to '%s'" % ver

def get_version():
    try:
        f = open(pjoin('json2yaml', '_version.py'))
    except EnvironmentError:
        return None
    for line in f.readlines():
        mo = re.match("__version__ = '([^']+)'", line)
        if mo:
            ver = mo.group(1)
            return ver
    return None

class Version(Command):
    description = "update _version.py from Git repo"
    user_options = []
    boolean_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        update_version_py()
        print "Version is now", get_version()

class sdist(_sdist):
    def run(self):
        update_version_py()
        # unless we update this, the sdist command will keep using the old
        # version
        self.distribution.metadata.version = get_version()
        return _sdist.run(self)

setup(
    name = 'json2yaml',
    version = get_version(),
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
    packages = [
        'json2yaml'
    ],
    scripts = [
        pjoin('bin', 'json2yaml'),
        pjoin('bin', 'yaml2json')
    ],
    install_requires = [
        'pyyaml',
        'pyaml',
        'docopt'
    ],
    cmdclass = {
        "version": Version,
        "sdist": sdist
    }
)
