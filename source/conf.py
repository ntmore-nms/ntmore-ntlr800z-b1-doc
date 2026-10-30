import datetime
import os
import sys
from pathlib import Path

import sphinx_rtd_theme
import sphinx_fontawesome

project = 'NTLR800Z-B1'
copyright = '2026,NTmore All rights reserved, nms-service@ntmore.kr'
author = 'jclee@ntmore.kr'
release = '1.0'

extensions = ['sphinx_fontawesome']

templates_path = ['_templates']
exclude_patterns = []

language = 'ko'

html_title = " ".join([project, release, "Documentation"])
html_short_title = "NTmore NTLR800Z-B1"
html_logo = "images/logo-only-50f.png"
html_favicon = 'images/favicon.png'

#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
#html_static_path = ['_static']

html_theme_options = {
    'prev_next_buttons_location': 'bottom',
    'style_nav_header_background': '#404040',
    'navigation_depth':'-1',
}

html_last_updated_fmt = '%B %d, %Y'

# conf.py 파일
html_css_files = [
    'css/custom.css', # 경로에 맞게 수정
]

rst_prolog = """
.. role:: red
   :class: red-text
.. role:: blue
   :class: blue-text
"""

# source/conf.py 맨 아랫줄에 복사해서 붙여넣으세요.

latex_engine = 'xelatex'
latex_logo = 'images/logo.png'
latex_elements = {
    'fontpkg': r'''
\setmainfont{NanumMyeongjo}
\setsansfont{NanumGothic}
\setmonofont{NanumGothicCoding}
''',
    'preamble': r'''
\usepackage{fontspec}
\usepackage{kotex}

''',
}
