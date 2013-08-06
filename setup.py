import os.path
from setuptools import setup, Extension

filename = os.path.join(os.path.dirname(__file__), 'description.rst')
with open(filename) as f:
    long_description = f.read()

rsamodule = Extension('ucam_webauth.rsa',
                      sources=['ucam_webauth/rsa.c'],
                      libraries=["ssl", "crypto"])

setup(
    name = "python-raven",
    version = "0.4",
    packages = ["raven", "ucam_webauth"],
    package_data = {"raven": ["keys/pubkey*"]},
    ext_modules = [rsamodule],
    install_requires = ["setuptools"],
    extras_require = {"flask_glue": ["Flask"]},
    tests_require = ["nose", "Flask"],
    test_suite = 'nose.collector',

    author = "Daniel Richman",
    author_email = "main@danielrichman.co.uk",
    description = "Ucam-webauth and Raven application agent in Python",
    long_description = long_description,
    license="GNU Lesser General Public License Version 3",
    keywords = "Raven Cambridge ucam-webauth",
    url = "http://github.com/danielrichman/python-raven",

    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2"
    ]
)

# python setup.py test
# python setup.py build_sphinx sdist upload upload_sphinx
