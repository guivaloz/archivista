AUTHOR = "guivaloz"
SITENAME = "Demostracion de Archivista"
SITEURL = "http://127.0.0.1:8000"

PATH = "content"

ARTICLE_PATHS = ["apuntes", "blog", "presentaciones"]
PAGE_PATHS = []
STATIC_PATHS = ["favicon.ico"]

DEFAULT_PAGINATION = False
USE_FOLDER_AS_CATEGORY = False
RELATIVE_URLS = True

DEFAULT_LANG = "es"
TIMEZONE = "America/Mexico_City"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)
