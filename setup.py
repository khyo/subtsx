# Copyright (c) 2023 Kyle Howen
# All Rights Reserved.

import os, re, platform
from setuptools import setup


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

VERSION = re.findall(r"\d+", read("subtsx", "version.py"))

setup(
    name='subtsx',
    version='{}.{}.{}'.format(*VERSION),
    description='TSX Gui Platform',
    packages=['subtsx'],
    entry_points = {
        'console_scripts': [
            'subtsx=subtsx.cmdline:main'
        ]},
    install_requires=[
        'subelectron @ git+https://github.com/khyo/subelectron.git@dev#egg=subelectron',
    ],
    include_package_data=True,
    package_data={'': ['**/*.ts', "**/*.js", "**/*.json", "**/*.html", "**/*.css", "**/*.ico", "**/*.png", "**/*.py"]},
    license='UNLICENSED',
    url='https://github.com/khyo/subtsx.git',
    author='Kyle Howen',
    author_email='kyle.howen@subinitial.com',
    keywords="tsx typescript gui electron subprocess",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
    ]
)
