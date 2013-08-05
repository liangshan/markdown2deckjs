# -*- coding: utf-8 -*-

from setuptools import setup

setup (
    name = "m2d",
    version = "1.0.dev",

    install_requires = [
        'markdown==2.3.1',
        'jinja2==2.7',
        'elementtree'
    ],

    author = "liangshan",
    description = "makedown 2 deckjs",
    url = "https://github.com/liangshan/markdown2deckjs"
)
