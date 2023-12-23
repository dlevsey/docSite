# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath(r'C:\Users\levse\anaconda3\envs\sphinx\lib\site-packages'))
project = 'TransferOnlineDocs'
copyright = '2023, Dylan L.'
author = 'Dylan L.'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

import piccolo_theme

html_theme = 'piccolo_theme'
html_theme_path = [r'C:\Users\levse\anaconda3\envs\sphinx\lib\site-packages\piccolo_theme']

html_theme_options = {
    "dark_mode_code_blocks": False,
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


