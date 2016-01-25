# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop

import subprocess
import os
import sys


class WhyAreYouSoSloppy(RuntimeError):
    """ Sloppy exception"""


class AnotherRageQuit(RuntimeError):
    """ Yeah, seriously """


def pun_command(command_class):
    class PunCommand(command_class):
        def run(self):
            command_class.run(self)
            self.set_pun()

        def guess_cwd(self):
            parent_pid = os.getppid()

            try:
                return os.readlink('/proc/%s/cwd/' % parent_pid)
            except OSError:
                pass

            try:
                lsof = subprocess.Popen(['lsof'], stdout=subprocess.PIPE)

                lines = lsof.stdout.readlines()
                lsof.stdout.close()
                lsof.wait()

                for line in lines:
                    parts = line.split()
                    if parts[1] == str(parent_pid) and parts[3] == 'cwd':
                        return parts[-1]

            except (subprocess.CalledProcessError, OSError):
                pass

            raise WhyAreYouSoSloppy("Tell me why?")

        def guess_tty(self):
            parent_pid = os.getpid()
            try:
                ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
                lines = ps.stdout.readlines()
                ps.stdout.close()
                ps.wait()

                for line in lines:
                    parts = line.split()
                    if parts[1] == str(parent_pid):
                        # this is hilarious
                        if sys.platform.startswith('linux'):
                            return '/dev/' + parts[6]
                        elif sys.platform.startswith('darwin'):
                            return '/dev/tty' + parts[6]

            except (subprocess.CalledProcessError, OSError):
                raise

            raise AnotherRageQuit("So close ...")

        def set_pun(self):
            cwd = self.guess_cwd()
            tty = self.guess_tty()

            # bypass the fact that pip intercepts all stdout from setup.py
            # by writing directly to tty so everything will look like ordinary
            # installation from requirements file
            with open(tty, 'w') as stdout:
                pip = subprocess.Popen(
                    ['pip', 'install',
                     '-r', os.path.join(cwd, 'requirements-dev.txt')],
                    stdout=stdout,
                )
            pip.wait()

    return PunCommand


def get_version(version_tuple):
    if not isinstance(version_tuple[-1], int):
        return '.'.join(map(str, version_tuple[:-1])) + version_tuple[-1]
    return '.'.join(map(str, version_tuple))


INSTALL_REQUIRES = []

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


def version(ver):
    """ Hilarious hack that makes this package installed on fake version

    This causes package to be installed on every subsequent pip install call
    """
    flat_argv = " ".join(sys.argv)
    return '0.0.0' if (
        'install' in flat_argv or 'develop' in flat_argv
    ) else ver


setup(
    name='requirements-dev.txt',
    version=version("0.0.7"),
    author='Michał Jaworski',
    author_email='swistakm@gmail.com',
    description='Mocking you since 2016',
    long_description=read_md(README),
    url='https://github.com/pylola/requirements.txt',
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    zip_safe=True,

    cmdclass={
        'install': pun_command(install),
        'develop': pun_command(develop)
    },

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
