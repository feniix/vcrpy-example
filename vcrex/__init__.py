#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function

import requests

import logging
import sys

__version__ = "0.0.1"

logger = logging.getLogger(__name__)

def main(args=None):
    if args is None:
        args = sys.argv[1:]

if __name__ == "__main__":
    sys.exit(main())
