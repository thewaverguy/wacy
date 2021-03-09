#!/bin/bash
rm -r ./dist

# create a python package
python3 setup.py sdist bdist_wheel
