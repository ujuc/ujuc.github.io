#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "ujuc"
SITENAME = "잘 밤에 쓸데없는 생각하기..."
SITESUBTITLE = "Anythink, Everythink!"
SITEURL = "https://ujuc.github.io"

USER_LOGO_URL = "img/logo.jpg"

PATH = "content"

TIMEZONE = "Asia/Seoul"

DEFAULT_LANG = "ko"
DEFAULT_DATE_FORMAT = "%y. %m. %d."

LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_PATHS = ["blog"]
ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

MENUITEMS = (
    ("Blog", "/", "fa-inbox"),
    ("Archive", "/archives.html", "fa-archive"),
    ("Tags", "/tags.html", "fa-tags"),
    ("Categories", "/categories.html", "fa-folder-open"),
)

SOCIAL = (
    ("Github", "https://github.com/ujuc", "fa-github-alt"),
    ("Linkin", "https://kr.linkedin.com/in/sungjinkang", "fa-linkedin-in"),
)

LINKS = ()

DEFAULT_PAGINATION = 5
STATIC_PATHS = ["img", "misc"]
DISPALY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = "clean/"

# Address
EMAIL_ADDRESS = "ujuc@ujuc.kr"
GITHUB_ADDRESS = "https://github.com/ujuc"
SO_ADDRESS = "https://stackoverflow.com/users/978762/sungjin-gang"
TWITTER_ADDRESS = "https://twitter.com/ujuc"

AUTHORS = {}

# Code
PYGMENTS_RST_OPTIONS = {"linenos": "table"}

# markdwon toc
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.abbr": {},
        "markdown.extensions.attr_list": {},
        "markdown.extensions.def_list": {},
        "markdown.extensions.fenced_code": {},
        "markdown.extensions.footnotes": {},
        "markdown.extensions.tables": {},
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.nl2br": {},
        "markdown.extensions.sane_lists": {},
        "markdown.extensions.smarty": {},
        "markdown.extensions.toc": {},
    },
    "output_format": "html5",
}

# Plugins
PLUGIN_PATHS = []

PLUGINS = []
