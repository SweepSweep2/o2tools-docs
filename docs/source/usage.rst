Usage
=====

.. _installation:

Installation
------------

To use O2Tools, either build it, or install it using pip:

.. code-block:: console

   (.venv) $ pip install o2tools

If you want to build it, follow the instructions for building.

Using O2Tools
-------------

Most of the functions do not exist when you run the code ``import o2tools``. Instead, you must import the module containing those tools.

For example, if you want to get the OJM tools, you must use something along these lines:

.. code-block:: python

   import o2tools

   with open("o2ma200.ojm", "rb") as f:
       ojm_file = o2tools.ojm.OJM(f.read())

Or, if you want only a certain file type in your code you can use something along these lines:

.. code-block:: python

   from o2tools import ojm

   with open("o2ma200.ojm", "rb") as f:
       ojm_file = ojm.OJM(f.read())

Below are some examples on how you would read certain data types.

OJN Files
---------

To parse OJN files, make a new ``OJN()`` class, with the OJN data as a parameter. Example:

.. code-block:: python

   import o2tools

   with open("o2ma100.ojn", "rb") as f:
       ojn_file = o2tools.ojn.OJN(f.read())

Now, to get data from it, in this case the note data, we just get a variable from it:

.. code-block:: python

   note_data = ojn_file.note_data

This won't return something like a list, but instead an OjnNoteData object, which is as follows:

.. code-block:: python

   class OjnNoteData:
      note_data_easy: dict
      note_data_normal: dict
      note_data_hard: dict

There are much more classes just like this one, which you can check out in the OJN, OJM, etc. sections.

----

If you want to see how to parse a certain data type, and see what you can do with it, check out it's appropriate documentation.

The parsing should be almost the same as this example, however they have different data and functions you can use.

Making New Files
----------------

As of right now, making OJM files in the OMC/OJM type is not implemented. If you want to implement it, contribute to the `O2Tools Github repository <https://github.com/SweepSweep2/o2tools>`_.

====

To make a new OJN file, you can call the function ``make_file()`` like this:

.. code-block:: python

   import o2tools

   with open("o2ma150.ojn", "rb") as f:
       ojn_file = ojn.OJN(f.read())
       new_ojn_file = ojn.make_file("o2ma200.ojn", ojn_file.header, ojn_file.note_data)

This will make a new OJN file called ``o2ma200.ojn`` with the exact same data as ``o2ma150.ojn``.

This also applies to all other data types except for OJM/OMC type OJM files. (M30 is accepted)

Continue
--------

You can follow tutorials on how to create O2Tools programs. Here are some that are good for beginners:

- :doc:'tutorial1.rst'
- tut2
- tut3