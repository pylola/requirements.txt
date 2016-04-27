#!/usr/bin/env bash

PACKAGE_NAMES="
    requirements-dev.txt
    requirements-test.txt
    requirements-dev
    requirements-tests
"

for name in $PACKAGE_NAMES
do
    echo "package_name = \"$name\"" > requirements_txt.py
    if [ $(python setup.py --name) == $name ]
    then
        echo "distributing $(python setup.py --name)"
        python setup.py register
        python setup.py sdist

    else
       echo "distribution and package name mismatch, abort"
       exit 1
    fi
done

echo "You are ready to distribute:"
echo "    $ twine upload dist/*"
