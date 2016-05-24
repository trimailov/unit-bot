unit-bot
========

Unit conversion bot for reddit (`/u/unit-conversion-bot <https://www.reddit.com/u/unit-conversion-bot>`__).

Why?
====

Because there are more than one unit system at this time, so people who are accustomed to one (e.g. Imperial) write and understand it better than another (e.g. metric).

This bot will try to find values of some units posted on reddit and will identify them and convert them to units from another system.

TO DOs
======

- [x] Convert speed (mph, kph, m/s)
- [ ] Convert length (miles, yards, inches, meters, centimeters)
- [ ] Convert weight (pounds, ounces, stones, kilograms)
- [ ] Convert power (horsepower, watt)
- [ ] Convert energy (Calorie, Joule)
- [ ] Convert torque (pound foot, Newton metre)

Install and use
===============

Create ``creds.py`` file in ``unit_bot/`` directory.

Example of ``creds.py``:

.. code-block:: python

    USERNAME = 'my-bot'
    PASSWORD = 'hunter2'

    USER_AGENT = 'unit bot'

Run it:

.. code-block:: bash

    make
    make run # or `run_no_reply`
