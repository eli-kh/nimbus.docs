# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Nimbus'
copyright = '2021, Cogniteam'
author = 'Cogniteam'

release = '0.1'
version = '0.1.0'

# -- General configuration

html_theme_options = {
    'logo_only': True,
    # ...
}
html_logo = "../img/nimbus-logo.png"

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_dark_mode'

# user starts in dark mode
default_dark_mode = True

# -- Options for EPUB output
epub_show_urls = 'footnote'
