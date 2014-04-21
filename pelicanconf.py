#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniele Sluijters'
SITENAME = 'Puppet a day'
SITEURL = ''
SITESUBTITLE = 'crowdsourced community blog'

TIMEZONE = 'UTC'

GITHUB_URL = 'https://github.com/puppet-a-day/puppet-a-day.github.io'

DEFAULT_LANG = 'en'
LOCALE=['en_GB', 'en_US']
MD_EXTENSIONS = (['codehilite(css_class=highlight)','extra', 'headerid'])

FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'

MENUITEMS = (
        ('Archives', 'archives'),
        ('Authors', 'authors'),
        ('Categories', 'categories'),
        ('Tags', 'tags'),
        )

COVER_IMG_URL = 'data/sidebar.jpg'

DEFAULT_PAGINATION = 0
DEFAULT_ORPHANS = 0
SUMMARY_MAX_LENGTH = 50
TYPOGRIFY = True
THEME = 'themes/puppet-a-day'

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'blog'

OUTPUT_PATH = 'output/'
PATH = 'content/'
ARTICLE_DIR = 'blog/'
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
LICENSE = ('CC Attribution-ShareAlike 4.0 International',
            'http://creativecommons.org/licenses/by-sa/4.0/',
            )
PLUGIN_PATH = 'plugins'
PLUGINS = ['gravatar']
STATIC_PATHS = [
    'extra/CNAME',
    'data',
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path':'CNAME'},
}
