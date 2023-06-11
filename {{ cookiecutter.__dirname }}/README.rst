{%- set repo_name = 'MicroPython_' -%}
{%- set full_repo_name = "jposada202020" + "/" + repo_name -%}
{%- set pypi_name = cookiecutter.library_name|lower|replace("_", "-")|replace(" ", "-") -%}
{%- set docs_url = 'https://micropython-' + cookiecutter.library_name | lower | replace(" ", "-") | replace("_", "-") + '.readthedocs.io/en/latest/' -%}

Introduction
============

{% if cookiecutter.sphinx_docs | lower in ["yes", "y"] %}
.. image:: https://readthedocs.org/projects/micropython-{{ cookiecutter.library_name | lower | replace(" ", "-") | replace("_", "-") }}/badge/?version=latest
{%- if cookiecutter.target_bundle == 'Adafruit' %}
    :target: {{ docs_url }}
{%- else %}
    :target: {{ docs_url }}
{%- endif %}
    :alt: Documentation Status
{% endif %}

.. image:: https://img.shields.io/pypi/v/micropython-{{ pypi_name }}.svg
    :alt: latest version on PyPI
    :target: https://pypi.python.org/pypi/micropython-{{ pypi_name }}

.. image:: https://static.pepy.tech/personalized-badge/micropython-{{ pypi_name }}?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Pypi%20Downloads
    :alt: Total PyPI downloads
    :target: https://pepy.tech/project/micropython-{{ pypi_name }}

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

{% if cookiecutter.library_description != "" %}
    {{- cookiecutter.library_description }}
{% else %}
.. todo:: Describe what the library does.
{% endif %}

Installing with mip
====================
To install using mpremote

.. code-block:: shell

    mpremote mip install github:jposada202020/MicroPython_{{ cookiecutter.__libname | upper }}

To install directly using a WIFI capable board

.. code-block:: shell

    mip install github:jposada202020/MicroPython_{{ cookiecutter.__libname | upper }}


Installing Library Examples
============================

If you want to install library examples:

.. code-block:: shell

    mpremote mip install github:jposada202020/MicroPython_{{ cookiecutter.__libname | upper }}/examples.json

To install directly using a WIFI capable board

.. code-block:: shell

    mip install github:jposada202020/MicroPython_{{ cookiecutter.__libname | upper }}/examples.json


Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/micropython-{{ cookiecutter.library_name }}/>`_.
To install for current user:

.. code-block:: shell

    pip3 install micropython-{{ cookiecutter.library_name }}

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install micropython-{{ cookiecutter.library_name }}

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install micropython-{{ cookiecutter.library_name }}


Usage Example
=============

Take a look at the examples directory

Documentation
=============
API documentation for this library can be found on `Read the Docs <{{ docs_url }}>`_.

