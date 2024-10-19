#!/usr/bin/env python
import os
import sys


# This file is only used if you use `make publish` or
# explicitly specify it as your config file.


sys.path.append(os.curdir)
from pelicanconf import *


SITEURL = "https://ujuc.github.io"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
FEED_ALL_RSS = "feeds/rss.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

GOOGLE_ANALYTICS = "G-X9EBSXCBTS"
GOOGLE_ADSENSE = "ca-pub-1014314833699403"

BMC_CODE = "8967ktT"

# Comment Services
UTTERANCES = True
GISCUS = True
REPO_NAME = "ujuc/ujuc.github.io"
REPO_ID = "MDEwOlJlcG9zaXRvcnkzMzA2MTA2NQ=="
GISUS_CATEGORY = "General"
GISUS_CATEGORY_ID = "MDE4OkRpc2N1c3Npb25DYXRlZ29yeTMyMDM5MjEy"
