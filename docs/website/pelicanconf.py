#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from typing import List, NamedTuple

AUTHOR = 'ElectrumSV Developers'
SITENAME = 'ElectrumSV Website'
SITEURL = ''

THEME = "theme"

PATH = "content"
PAGE_PATHS = [ "pages" ]
ARTICLE_PATHS = [ "articles" ]
STATIC_PATHS = [
    "download",
    "release.json",
]

ARTICLE_SAVE_AS = 'articles/{date:%Y}/{slug}.html'
ARTICLE_URL = 'articles/{date:%Y}/{slug}.html'

TEMPLATE_PAGES = {
    "download.html": "download.html",
}

TIMEZONE = 'Pacific/Auckland'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = "%Y/%m/%d %I:%M %p"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

class DownloadFileEntry(NamedTuple):
    class_name: str
    title: str
    text: str
    file_name: str
    size_text: str

class DownloadEntry(NamedTuple):
    version: str
    release_date: str
    article_link: str
    files: List[DownloadFileEntry]

DOWNLOAD_LATEST = DownloadEntry("1.3.11", "2020/11/30", "https://medium.com/@roger-taylor/electrumsv-1-3-11-6f09f2aaed94", [
    DownloadFileEntry("fab fa-apple", "MacOS downloads", "MacOS", "ElectrumSV-1.3.11.dmg","30.1 MB"),
    DownloadFileEntry("fab fa-windows", "Windows downloads", "Windows", "ElectrumSV-1.3.11.exe", "26.4 MB"),
    DownloadFileEntry("fab fa-windows", "Windows downloads", "Windows", "ElectrumSV-1.3.11-portable.exe", "26.4 MB"),
    DownloadFileEntry("fas fa-code", "Other downloads", "Source code", "ElectrumSV-1.3.11.tar.gz", "7.3 MB"),
    DownloadFileEntry("fas fa-code", "Other downloads", "Source code", "ElectrumSV-1.3.11.zip", "7.6 MB"),
    DownloadFileEntry("fas fa-book", "Documentation", "HTML", "ElectrumSV-1.3.11-docs.zip", "11.5 MB"),
])

DOWNLOADS_OLDER = [
    DownloadEntry("1.3.10", "2020/11/19", "https://medium.com/@roger-taylor/electrumsv-1-3-10-f0a60d031d81", [
        DownloadFileEntry("fab fa-apple", "MacOS downloads", "MacOS", "ElectrumSV-1.3.10.dmg","30.1 MB"),
        DownloadFileEntry("fab fa-windows", "Windows downloads", "Windows", "ElectrumSV-1.3.10.exe", "26.4 MB"),
        DownloadFileEntry("fab fa-windows", "Windows downloads", "Windows", "ElectrumSV-1.3.10-portable.exe", "26.4 MB"),
        DownloadFileEntry("fas fa-code", "Other downloads", "Source code", "ElectrumSV-1.3.10.tar.gz", "7.3 MB"),
        DownloadFileEntry("fas fa-code", "Other downloads", "Source code", "ElectrumSV-1.3.10.zip", "7.6 MB"),
        DownloadFileEntry("fas fa-book", "Documentation", "HTML", "ElectrumSV-1.3.10-docs.zip", "11.5 MB"),
    ]),
    DownloadEntry("1.3.9", "2020/11/16", "https://medium.com/@roger-taylor/electrumsv-1-3-9-50c39bc7ef68", [
        DownloadFileEntry("fab fa-apple", "MacOS downloads", "MacOS", "ElectrumSV-1.3.9.dmg","30.3 MB"),
        DownloadFileEntry("fab fa-windows", "Windows downloads", "Windows", "ElectrumSV-1.3.9.exe", "26.4 MB"),
        DownloadFileEntry("fab fa-windows", "Windows downloads", "Windows", "ElectrumSV-1.3.9-portable.exe", "26.4 MB"),
        DownloadFileEntry("fas fa-code", "Other downloads", "Source code", "ElectrumSV-1.3.9.tar.gz", "7.3 MB"),
        DownloadFileEntry("fas fa-code", "Other downloads", "Source code", "ElectrumSV-1.3.9.zip", "7.6 MB"),
        DownloadFileEntry("fas fa-book", "Documentation", "HTML", "ElectrumSV-1.3.9-docs.zip", "11.5 MB"),
    ]),
    DownloadEntry("1.3.8", "2020/11/09", "https://medium.com/@roger-taylor/electrumsv-1-3-8-e07700fb9058", [
        DownloadFileEntry("fab fa-apple", "MacOS downloads", "MacOS", "ElectrumSV-1.3.8.dmg","31.5 MB"),
        DownloadFileEntry("fab fa-windows", "Windows downloads", "Windows", "ElectrumSV-1.3.8.exe", "26.9 MB"),
        DownloadFileEntry("fab fa-windows", "Windows downloads", "Windows", "ElectrumSV-1.3.8-portable.exe", "26.9 MB"),
        DownloadFileEntry("fas fa-code", "Other downloads", "Source code", "ElectrumSV-1.3.8.tar.gz", "7.3 MB"),
        DownloadFileEntry("fas fa-code", "Other downloads", "Source code", "ElectrumSV-1.3.8.zip", "7.5 MB"),
        DownloadFileEntry("fas fa-book", "Documentation", "HTML", "ElectrumSV-1.3.8-docs.zip", "11.5 MB"),
    ]),
    DownloadEntry("1.3.7", "2020/10/08", "https://medium.com/@roger.taylor/electrumsv-1-3-7-8b3833343bd3", [
        DownloadFileEntry("fab fa-apple", "MacOS downloads", "MacOS", "ElectrumSV-1.3.7.dmg","31.5 MB"),
        DownloadFileEntry("fab fa-windows", "Windows downloads", "Windows", "ElectrumSV-1.3.7.exe", "27.0 MB"),
        DownloadFileEntry("fab fa-windows", "Windows downloads", "Windows", "ElectrumSV-1.3.7-portable.exe", "27.0 MB"),
        DownloadFileEntry("fas fa-code", "Other downloads", "Source code", "ElectrumSV-1.3.7.tar.gz", "6.5 MB"),
        DownloadFileEntry("fas fa-code", "Other downloads", "Source code", "ElectrumSV-1.3.7.zip", "6.7 MB"),
        DownloadFileEntry("fas fa-book", "Documentation", "HTML", "ElectrumSV-1.3.7-docs.zip", "11.3 MB"),
    ]),
    DownloadEntry("1.3.6", "2020/09/03", "https://medium.com/@roger.taylor/electrumsv-1-3-6-a1f429bb1391", [
        DownloadFileEntry("fab fa-apple", "MacOS downloads", "MacOS", "ElectrumSV-1.3.6.dmg","31.3 MB"),
        DownloadFileEntry("fab fa-windows", "Windows downloads", "Windows", "ElectrumSV-1.3.6.exe", "27.1 MB"),
        DownloadFileEntry("fab fa-windows", "Windows downloads", "Windows", "ElectrumSV-1.3.6-portable.exe", "27.1 MB"),
        DownloadFileEntry("fas fa-code", "Other downloads", "Source code", "ElectrumSV-1.3.6.tar.gz", "4.2 MB"),
        DownloadFileEntry("fas fa-code", "Other downloads", "Source code", "ElectrumSV-1.3.6.zip", "4.4 MB"),
    ]),
]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
