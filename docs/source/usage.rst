Usage
=====

.. _installation:

Installation
------------

To use O2Tools, either build it, or install it using pip:

.. code-block:: console

   (.venv) $ pip install o2tools

If you want to build it, follow the instructions here.

Using O2Tools
-------------

Most of the functions do not exist when you run the code ``import o2tools``. Instead, you must import the module containing those tools.

For example, if you want to get the OJM tools, you must use something along these lines:

.. code-block:: python

   import o2tools

   ojm_file = o2tools.ojm.OJM("o2ma200.ojm")

Or, if you want only a certain file type in your code you can use something along these lines:

.. code-block:: python

   from o2tools import ojm

   ojm_file = ojm.OJM("o2ma200.ojm")

Getting the Files
-----------------

There aren't really good ways to get the files from O2Jam, but there are some websites I would recommend you use:

- https://nnty.fun/downloads/game/o2jam/MEGA/

All the websites mentioned are 100% safe to use.

This package is dependent on O2Jam Client 1.8 and O2Jam Server 1.8, other versions of O2Jam may not work. (we are still adding support!)

OJN Files
---------

To parse OJN files, make a new ``OJN()`` class, with the OJN file path as a parameter. Example:

.. code-block:: python

   import o2tools
   ojn_file = o2tools.ojn.OJN("o2ma100.ojn")

Now, to get data from it, in this case the note data, we just get a variable from it:

.. code-block:: python

   note_data = ojn_file.note_data

This won't return something like a list, but instead an OjnNoteData object, which is as follows:

.. code-block:: python

   @dataclasses.dataclass
   class OjnNoteData:
      note_data_easy: dict
      note_data_normal: dict
      note_data_hard: dict

There are much more classes just like this one, which you can check out in the OJN, OJM, etc. sections.

====

If you want the full documentation on the OJN section of O2Tools, check out the O2Tools OJN Documentation.

If you want the full documentation on how OJN files work, check out the OJN Documentation.

OJM Files
---------

To parse OJM files, make a new ``OJM()`` class, with the OJM file path as a parameter. Example:

.. code-block:: python

   import o2tools
   ojm_file = o2tools.ojm.OJM("o2ma250.ojm")

To extract the data from it, in this case the header, we get another variable from it:

.. code-block:: python

   header = ojm_file.header

This will give us an OjmHeader object.

Making New Files
----------------

As of right now, making OJM files in the OMC/OJM type is not implemented. If you want to implement it, contribute to the `O2Tools Github repository <https://github.com/SweepSweep2/o2tools>`_.

====

To make a new OJN file, you can call the function ``make_file()`` like this:

.. code-block:: python

   import o2tools

   ojn_file = ojn.OJN("o2ma150.ojn")
   new_ojn_file = ojn.make_file("o2ma200.ojn", ojn_file.header, ojn_file.note_data)

This will make a new OJN file called ``o2ma200.ojn`` with the exact same data as ``o2ma150.ojn``.

Continue
--------

You can follow tutorials on how to create O2Tools programs. Here are some that are good for beginners:

- :doc:'tutorial1.rst'
- tut2
- tut3

You can also read the documentation on how these file formats work here.
