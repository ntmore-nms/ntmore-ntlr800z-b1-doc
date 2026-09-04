import datetime
import os
import sys
from pathlib import Path

import sphinx_rtd_theme
import sphinx_fontawesome

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'NTmore NMS'
copyright = '2023,2024,NTmore All rights reserved, nms-service@ntmore.kr'
author = 'jclee@ntmore.kr'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_fontawesome']

templates_path = ['_templates']
exclude_patterns = []

language = 'ko'

html_title = " ".join([project, release, "Documentation"])
html_short_title = "NTmore NMS"
html_logo = "images/logo-only-50f.png"
html_favicon = 'images/favicon.png'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'prev_next_buttons_location': 'bottom',
    'style_nav_header_background': '#404040',
    'navigation_depth':'-1',
}

html_last_updated_fmt = '%B %d, %Y'
