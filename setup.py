#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from setuptools import find_packages, setup

_version_file = open(os.path.join(os.path.dirname(__file__), 'version.py'))
VERSION = re.compile(r"^VERSION = '(.*?)'", re.S).match(_version_file.read()).group(1)

setup(
    name="plctools",
    version=VERSION,
    author="Polyconseil",
    author_email="opensource+plctools@polyconseil.fr",
    description="Collection of tools to manipulate a PLC.",
    license="BSD",
    keywords="modbus",
    url="https://github.com/polyconseil/plctools",
    packages=find_packages(),
    long_description="",
    install_requires=[
        'pylibmodbus',
    ],
    entry_points={
        'console_scripts': [
            'plc_dump = plc_dump:main',
            'plc_load = plc_load:main',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python 3",
    ],
    test_suite='',
    include_package_data=True,
)
