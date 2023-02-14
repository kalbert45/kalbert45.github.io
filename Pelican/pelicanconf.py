AUTHOR = 'Albert Kim'
SITENAME = 'Albert Kim Games'
SITEURL = 'http://localhost:8000'
SITELOGO = 'images/icons/profile.png'
SITETITLE = 'Albert Kim'
FAVICON = 'images/icons/favicon.ico'

PATH = 'content'

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = 'themes/Flex'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('github', '#'),
          ('itch', '#'),
           ('steam', '#'),
           ('youtube', '#'))

STATIC_PATHS = ['images', 'extra']

# Main Menu Items
MAIN_MENU = True
MENUITEMS = (('Games', '/games'),('About', '/about'))

# Code highlighting the theme
PYGMENTS_STYLE = 'friendly'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
