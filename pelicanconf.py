#!/usr/bin/env python
from pendulum import today


AUTHOR = "ujuc"
SITENAME = "잘 밤에 쓸데없는 생각하기"
SITESUBTITLE = "Anythink, Everythink!"
SITEURL = "https://ujuc.github.io"
START_YEAR = 2012
END_YEAR = today(tz="Asia/Seoul").year

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

MENU = (
    ("Blog", "/", "inbox"),
    ("Archive", "/archives.html", "archive"),
    ("Tags", "/tags.html", "tags"),
    ("Categories", "/categories.html", "folder-open"),
)

SOCIAL = (
    ("Github", "https://github.com/ujuc", "github"),
    ("Linkin", "https://kr.linkedin.com/in/sungjinkang", "linkedin"),
    ("X", "https://x.com/ujuc", "x-twitter"),
)

LINKS = ()

DEFAULT_PAGINATION = 5
STATIC_PATHS = ["img", "misc"]
DISPLAY_PAGES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = "clean/"

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
        "markdown.extensions.md_in_html": {},
        "markdown.extensions.tables": {},
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {
            "css_class": "highlight"
        },
        "markdown.extensions.meta": {},
        "markdown.extensions.nl2br": {},
        "markdown.extensions.sane_lists": {},
        "markdown.extensions.smarty": {},
        "markdown.extensions.toc": {},
        "markdown.extensions.wikilinks": {},
    },
    "output_format": "html5",
}

# Plugins
PLUGIN_PATHS = []

PLUGINS = []
