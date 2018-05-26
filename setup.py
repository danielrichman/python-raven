import os.path
from setuptools import setup, Extension

filename = os.path.join(os.path.dirname(__file__), 'description.rst')
with open(filename) as f:
    long_description = f.read()

setup(
    name = "python-raven",
    version = "0.9.2.1",
    packages = ["raven"],
    install_requires = ["setuptools", "python-ucam-webauth"],
    extras_require = {"flask_glue": ["Flask"]},

    author = "Daniel Richman",
    author_email = "main@danielrichman.co.uk",
    description = "Compatability wrapper around python-ucam-webauth",
    long_description = long_description,
    license="BSD-2-Clause",
    keywords = "Raven Cambridge ucam-webauth",
    url = "http://github.com/danielrichman/python-raven",

    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: "
                    "CGI Tools/Libraries",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ]
)
