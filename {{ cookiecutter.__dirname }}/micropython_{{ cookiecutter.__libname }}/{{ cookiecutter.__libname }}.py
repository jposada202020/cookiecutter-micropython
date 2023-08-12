# SPDX-FileCopyrightText: Copyright (c) {% now 'utc', '%Y' %} Jose D. Montoya
#
# SPDX-License-Identifier: MIT
"""
`{{ cookiecutter.library_name | lower | replace(" ", "_") }}`
================================================================================

{% if cookiecutter.library_description != "" %}
    {{- cookiecutter.library_description }}
{% else %}
.. todo:: Describe what the library does.
{% endif %}

* Author: Jose D. Montoya


"""

from micropython import const
from micropython_{{ cookiecutter.__libname }}.i2c_helpers import CBits, RegisterStruct

try:
    from typing import Tuple
except ImportError:
    pass


__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/jposada202020/MicroPython_{{ cookiecutter.library_name | upper }}.git"


class {{ cookiecutter.library_name | upper }}:
    """Driver for the {{ cookiecutter.library_name | upper }} Sensor connected over I2C.

    :param ~machine.I2C i2c: The I2C bus the {{ cookiecutter.library_name | upper }} is connected to.
    :param int address: The I2C device address. Defaults to :const:`0x69`

    :raises RuntimeError: if the sensor is not found

    **Quickstart: Importing and using the device**

    Here is an example of using the :class:`{{ cookiecutter.library_name | upper }}` class.
    First you will need to import the libraries to use the sensor

    .. code-block:: python

        from machine import Pin, I2C
        from micropython_{{ cookiecutter.library_name}} import {{ cookiecutter.library_name}}

    Once this is done you can define your `machine.I2C` object and define your sensor object

    .. code-block:: python

        i2c = I2C(1, sda=Pin(2), scl=Pin(3))
        {{ cookiecutter.library_name }} = {{ cookiecutter.library_name}}.{{ cookiecutter.library_name | upper }}(i2c)

    Now you have access to the attributes

    .. code-block:: python

    """

    def __init__(self, i2c, address: int = xxx) -> None:
        self._i2c = i2c
        self._address = address

        if self._device_id != xxx:
            raise RuntimeError("Failed to find {{ cookiecutter.library_name | upper }}")
