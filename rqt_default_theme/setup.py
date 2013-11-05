#!/usr/bin/env python

from os import system
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

print("Running PyRCC generator for rqt_default_theme Qt resources...")
system("pyrcc5 themes/tango/theme.qrc -o resource/tango_rc.py")

d = generate_distutils_setup(
    packages=['rqt_default_theme'],
    package_dir={'': 'src'}
)

setup(**d)
