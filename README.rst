Introduction
============


This cookiecutter creates a project structure for micropython libraries for my personal use. Nevertheless, you could replace the github user with you own.
It is Hard coded ATM


Cookiecutter Usage
===================

.. code-block:: bash

  # The first time
  pip install cookiecutter~=2.1


Then, fill in the prompts and accomplish some post generation cleanup:

Prompts
--------

* ``library_name`` - Shortest name for the library.
* ``library_description`` - Write a sentence describing the purpose of this library 
* ``sphinx_docs`` - Should the Sphinx based documentation be included in your repo? If so, enter ``y`` or ``yes`` to include the setup.py. For Adafruit libraries this defaults to Yes.


.. note::

    If you wish to use the Release feature on GitHub to upload libraries to PyPI, you will need to
    add your PyPI token to the repository secrets.  Set a secret named ``PYPI_USERNAME`` to
    ``__token__`` and a secret named ``PYPI_PASSWORD`` to your API token with the proper scope.
    Never share your API token anyone!


