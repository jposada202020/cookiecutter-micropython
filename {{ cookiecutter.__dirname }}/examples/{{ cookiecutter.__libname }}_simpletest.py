# SPDX-FileCopyrightText: Copyright (c) {% now 'utc', '%Y' %} Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_{{ cookiecutter.library_name}} import {{ cookiecutter.library_name}}

i2c = I2C(sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
xxx = {{cookiecutter.library_name}}.{{ cookiecutter.library_name | upper }}(i2c)

while True:

    time.sleep(0.5)