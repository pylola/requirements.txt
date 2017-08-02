[![PyPI](https://img.shields.io/badge/downloads-enough-ff69b4.svg)](https://pypi.python.org/pypi?name=requirements-dev.txt)

# requirements.txt

This is a safeguard against typos when running `pip install -r requirements-dev.txt`.
If you leave out the `-r` by accident, this package will cause your installation
to abort.

    $ pip install requirements-dev.txt
    Collecting requirements-dev.txt
    Installing collected packages: requirements-dev.txt
      Running setup.py install for requirements-dev.txt ... error
        Complete output from command:
        running install
        It looks like you meant to type `pip install -r requirements-dev.txt`,
        but you left out the `-r` by accident. Aborting installation.


## Why?

If we had no such package on PyPI, you could accidentally install a package 
installed with the name of your requirements file. A malicious user could
register a package that would mimic proper installation process and also
launch anny arbitrary code.


PyPI (fortunately) does not allow `requirements.txt` as a package name, so that
case is handled already. All forbidden package names that are 
[hardcoded in PyPI source code](https://bitbucket.org/pypa/pypi/src/76e6e7117e388fa6748d2410576c12e09d875318/webui.py?fileviewer=file-view-default#webui.py-2297)
are:

* `requirements.txt`
* `rrequirements.txt`
* `requirements-txt`
* `rrequirements-txt`

But it obviously does not cover all popular cases. This is why this sources
are distributed on PyPI under few popular names that are not forbidden by PyPI:

* `requirements-dev.txt`
* `requirements-dev`
* `requirements-test.txt`
* `requirements-test`


## Did it ever happen?

Yeah. Typo squatting happens on PyPI from time to time. This project is the
best example of that. Previous version of `requirements.txt` actually did
something more than aborting its installation. It provided a specially
crafted `setup.py` script that could:

* look on your filesystem to find a requirements file you intended to install
* install all packages in another pip subprocess
* display output that would mimick normal installation process

Newer versions of pip completely swallow all output of package installation
script but this behavior can be easily bypassed - at least on OS X and Linux.
Also runtime version switch (to `0.0.0`) allowed to install this package over 
and over becasue there was always newer version available on PyPI. If something 
went wrong (especially on Windows) it resulted in crypting and rude error message.

Nothing harmful. Actually useful sometimes. At least in my personal opinion. 
Anyway my sense of usability and humour 
[was contested by some people](https://github.com/pylola/requirements.txt/issues/1).
This is why `requirements.txt` will longer install other packages and always
exit with error code during installation. This is mostly thanks to pull-request
from @aanand and [his points](https://github.com/pylola/requirements.txt/pull/2).
I may not agree with all of them but I respect people's PRs.

Nevertheless, some additional messages may be displayed during installation 
attempt. You know... It was made for fun.

If you are interested in hacks included in previous version of this package
refer to `contested-sense-of-humour` branch or `end-of-fun` tag in this 
project's [repository](https://github.com/pylola/requirements.txt).
