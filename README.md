# python-raven - Ucam-webauth and Raven application agent in Python

This is a compatibility wrapper around
[python-ucam-webauth](https://github.com/danielrichman/python-ucam-webauth)
only, to avoid conflicting with the `raven` package.

This package exposes `ucam_webauth.raven` as `raven`. You should ideally depend
on `python-ucam-webauth` and import `ucam_webauth.raven` directly.
