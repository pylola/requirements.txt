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

PyPI (fortunately) does not allow `requirements.txt` as a package name, so that
case is handled already.
