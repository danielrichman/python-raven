This is a compatibility wrapper around
`python-ucam-webauth <https://github.com/danielrichman/python-ucam-webauth>`_
only, to avoid conflicting with the `raven` package.

This package exposes `ucam_webauth.raven` as `raven`. This is how the library
used to be packaged, pre v0.9. You should ideally depend on `python-ucam-webauth`
and import `ucam_webauth.raven` directly.

Other links
===========

* `python-ucam-webauth package <https://pypi.org/project/python-ucam-webauth/>`_
* `source on github <https://github.com/danielrichman/python-raven>`_
