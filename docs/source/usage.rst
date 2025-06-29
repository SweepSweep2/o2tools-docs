Usage
=====

.. _installation:

Installation
------------

To use O2Tools, first install it using pip:

.. code-block:: console

   (.venv) $ pip install o2tools

OJN Files
---------

To parse OJN files, make a new ``OJN()`` class, with the OJN file path as a parameter. Example:

.. ojn_example_1:: python

   ojn_file = OJN("o2ma100.ojn")

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']
