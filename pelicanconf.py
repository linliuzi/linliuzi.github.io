#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'schnee'
SITENAME = u'jrayty'
SITEURL = 'http://linliuzi.github.io'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'
ARCHIVES_URL = 'archives.html'
ARTICLE_URL = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('my sina blog', 'http://blog.sina.com.cn/u/2310559855'),
          ('google', 'http://www.google.com'),)

DEFAULT_PAGINATION = 10

THEME = r'D:\Program Files\github install\pelican-themes-master\pelican-themes-master\bootstrap2'

DISQUS_SITENAME = 'schnee27'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
