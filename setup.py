#!/usr/bin/env python

import sys
sys.path.insert(0, 'Pymacs')
from version import package, version
del sys.path[0]

from distutils.core import setup

setup(name=package,
      version=version,
      description='Interface between Emacs LISP and Python.',
      author='Fran�ois Pinard',
      author_email='pinard@iro.umontreal.ca',
      url='http://www.iro.umontreal.ca/~pinard',
      scripts=['pymacs-services', 'rebox'],
      packages=['Pymacs'])
