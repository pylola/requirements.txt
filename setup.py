# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools.command.install import install

import os


class AbortInstall(install):
    def run(self):
        raise SystemExit(
            "It looks like you meant to type "
            "`pip install -r requirements-dev.txt`, but you left out the `-r` "
            "by accident. Aborting installation."
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
    name='requirements-dev.txt',
    version="0.0.7",
    author='Michał Jaworski',
    author_email='swistakm@gmail.com',
    description='Safeguard against one particullar "pip install" typo',
    long_description=read_md(README),
    url='https://github.com/pylola/requirements.txt',
    include_package_data=True,

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
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
