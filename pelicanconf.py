#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ujuc'
SITENAME = '잘 밤에 쓸데없는 생각하기...'
SITESUBTITLE = 'Anythink, Everythink!'
SITEURL = 'http://ujuc.github.io'

USER_LOGO_URL = 'img/logo.jpg'

PATH = 'content'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'ko'
DEFAULT_DATE_FORMAT = '%Y. %m. %d. %a'

LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_PATHS = ['blog']
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

MENUITEMS = [
	('blog', '/'),
	('Tags', '/tags.html'),
	('Categories', '/categories.html'),
	('Email', 'mailto:ujuc@ujuc.kr'),
	('Github', 'https://github.com/ujuc'),
]

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5
STATIC_PATHS = ['img', 'misc']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
TYPOGRIFY = True
THEME = "theme/svbhack/"

# Address
EMAIL_ADDRESS = 'ujuc@ujuc.kr'
GITHUB_ADDRESS = 'https://github.com/ujuc'
SO_ADDRESS = 'http://stackoverflow.com/users/978762/sungjin-gang'
TWITTER_ADDRESS = 'https://twitter.com/ujuc'

# Theme seeting
BS3_URL = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css'
BS3_JS = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js'
BS3_THEME = 'https://bootswatch.com/sandstone/bootstrap.min.css'

AUTHORS = {
}
