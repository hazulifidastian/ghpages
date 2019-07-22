#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hazuli Fidastian'
SITENAME = 'Hazuli Fidastian'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#  LINKS = (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)

# Social widget
#  SOCIAL = (('You can add links in your config file', '#'),
#            ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'documents']

PORT = 8080

# Uncomment following line if you want document-relative URLs when developing
#  RELATIVE_URLS = True

THEME = 'theme'

MENUITEMS = (('Beranda', '/'), ('Stori', '/stories-id.html'),
             ('Kontak', '/contact-id.html'))

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

INDEX_SAVE_AS = 'stories-id.html'

YEAR_ARCHIVE_SAVE_AS = 'stories/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'stories/{date:%Y}/{date:%b}/index.html'
