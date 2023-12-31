## import os
## import sys
## sys.path.insert(0, os.path.abspath("_themes"))
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'German Emigration Records'
#copyright = "MIT License"
copyright = "Creative Commons Attribution-NonCommercial 4.0 International Public License"
author = 'Kurt Krueckeberg'
release = '0.8'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_immaterial']

myst_enable_extensions = [
  "colon_fence", "deflist"
]

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'readme.md']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_immaterial'

extensions.append("sphinx_immaterial")

# material theme options (see theme.conf for more information)
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
        "edit": "material/file-edit-outline",
    },
#    "site_url": "https://jbms.github.io/sphinx-immaterial/",
#    "repo_url": "https://github.com/jbms/sphinx-immaterial/",
#    "repo_name": "Sphinx-Immaterial",
    "edit_uri": "blob/main/docs",
    "globaltoc_collapse": True,
    "features": [
        "navigation.expand",
        # "navigation.tabs",
        # "toc.integrate",
        "navigation.sections",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        # "navigation.tracking",
        # "search.highlight",
        "search.share",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "light-green",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "deep-orange",
            "accent": "lime",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            },
        },
    ],
    "toc_title_is_page_title": True,
    # BEGIN: social icons
}

# Options for sphinx_material
#html_theme_options = {
#   'base_url': 'http://kurt-krueckeberg.io/',
#   'repo_url': 'https://github.com/kurt-krueckeberg/kurt-krueckeberg.github.io/',
#   'html_minify': True,
#   'css_minify': True,
#   'logo_icon': '&#xe869',
#   'globaltoc_depth': 2,
##    "color_primary": "blue",
##    "color_accent": "cyan",
##    "theme_color": "#2196f3",
##    "version_dropdown": True,
##    "table_classes": ["plain"]
#}

html_static_path = ['_static']

html_css_files = [
    'kurt-style.css',
]
