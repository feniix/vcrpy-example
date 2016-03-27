#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function

import logging
import sys

import requests

__version__ = "0.0.1"

logger = logging.getLogger(__name__)

def google_body():
    return requests.get("https://www.google.com")

def main(args=None):
    if args is None:
        args = sys.argv[1:]

if __name__ == "__main__":
    sys.exit(main())
