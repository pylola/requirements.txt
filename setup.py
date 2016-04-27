# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools.command.install import install

import os

# this is quic and dirty solution to ease multi-name distribution on PyPI
try:
    from requirements_txt import package_name
except ImportError:
    package_name = 'requirements-dev.txt'


class AbortInstall(install):
    def run(self):
        raise SystemExit(
            "It looks like you meant to type "
            "`pip install -r %s`, but you left out the `-r` "
            "by accident. Aborting installation." % package_name
        )


try:
    from pypandoc import convert

    def read_md(f):
        return convert(f, 'rst')

except ImportError:
    convert = None
    print(
        "warning: pypandoc module not found, could not convert Markdown to RST"
    )

    def read_md(f):
        return open(f, 'r').read()  # noqa

README = os.path.join(os.path.dirname(__file__), 'README.md')


setup(
    name=package_name,
    version="1.0.0",
    author='Michał Jaworski',
    author_email='swistakm@gmail.com',
    description='Safeguard against one particullar "pip install" typo',
    long_description=read_md(README),
    url='https://github.com/pylola/requirements.txt',
    include_package_data=True,
    py_modules=['requirements_txt'],
    cmdclass={'install': AbortInstall},

    license="BSD",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
