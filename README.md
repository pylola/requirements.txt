Ever did a mistake to `pip install` in the terminal when installing packages
from `requirements.txt` file like following?

    $ pip install requirements.txt
    Collecting requirements.txt
      Could not find a version that satisfies the requirement requirements.txt (from versions: )
    No matching distribution found for requirements.txt

Now you wont. Thanks to some nasty hacks and tricks there is a package on PyPI
that handles that. It finds the desired requirements file and installs it in
your current environment.

    echo "gevent" > requirements-dev.txt
    pip install requirements-dev.txt

This package was made only for trolling so do not expect it to work. It may
work on Linux and Mac OS X but was not extensively tested. Also this is only
a one-shot fix. Once you did the mistake it will try to fix it but once 
installed this package is installed will not help you anymore.

PyPI (fortunately) does not allow to upload package named `requirements.txt` so the
only supported name is currently a `requirements-dev.txt`. It still should be
quite popular though.
