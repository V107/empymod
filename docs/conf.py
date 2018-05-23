#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
from empymod import __version__

sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ------------------------------------------------

# The Sphinx extension.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'numpydoc',
    'sphinxcontrib.napoleon',
]
numpydoc_show_class_members = False

# The templates path.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'empymod'
copyright = u'2016-{}, Dieter Werthmüller'.format(time.strftime("%Y"))
author = 'Dieter Werthmüller'

# |version| and |release|.
#
# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx.
language = None

# |today| format.
today_fmt = '%d %B %Y'

# List of patterns to ignore, relative to source directory.
exclude_patterns = ['_build', 'PermissionToRelicenseFilters.txt',
                    'LaTeX', '../tests']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'alabaster'

# Theme options.
description = 'An open-source full 3D electromagnetic modeller for 1D VTI '
description += 'media in Python'
html_theme_options = {
    'description': description,
}

# HTML static path
html_static_path = ['_static']

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/logo-empymod-plain.png'

# Favicon of the docs.
html_favicon = '_static/favicon.ico'

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'searchbox.html',
    ]
}

# Output file base name for HTML help builder.
htmlhelp_basename = 'empymoddoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'empymod.tex', 'empymod Documentation',
     'Dieter Werthmüller', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'empymod', 'empymod Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'empymod', 'empymod Documentation',
     author, 'empymod', description,
     'Electromagnetic geophysical modelling'),
]
