#!/usr/bin/env python

import setuptools

# compatibility file for the old setup.py package format
# this is just a shim for loading pyproject.toml
if __name__ == "__main__":
    setuptools.setup()