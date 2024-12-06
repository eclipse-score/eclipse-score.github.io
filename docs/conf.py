# *******************************************************************************
# Copyright (c) 2024 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0
#
# SPDX-License-Identifier: Apache-2.0
# *******************************************************************************

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "SCORE"
copyright = "2024, Score"
author = "SCORE committers"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ["_templates"]

numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"  #  "alabaster"
# html_theme_options = {"page_width": "auto", "body_max_width": "1500"}

html_static_path = ["_assets"]
html_css_files = [
    "css/score.css",
]

html_theme_options = {
    "external_links": [
        {"name": "Docs", "url": "https://eclipse-score.github.io/score/"},
        {
            "name": "Eclipse",
            "url": "https://projects.eclipse.org/projects/automotive.score",
        },
    ],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/eclipse-score",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        }
    ],
    "use_edit_page_button": True,  # https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/source-buttons.html#add-an-edit-button
    "collapse_navigation": True,
    "logo": {
        "text": "Eclipse SCORE",
    },
}

html_context = {
    # "github_url": "https://github.com", # or your GitHub Enterprise site
    "github_user": "eclipse-score",
    "github_repo": "eclipse-score.github.io",
    "github_version": "main",
    "doc_path": "docs",
}

# Shows no left sidebar for single files
# Woraround for bug: https://github.com/pydata/pydata-sphinx-theme/issues/1662#issuecomment-1913672649
html_sidebars = {"get_involved": []}
