Building
=====

.. _building:

What You'll Need
------------

* O2Tools Source Code
* build (dependency)

Building O2Tools
-------------

First, clone the repository:

.. code-block:: console

   $ git clone https://github.com/SweepSweep2/o2tools.git

Inside the root of the project (where pyproject.toml is located), run:

.. code-block:: console

   $ python -m build

This will generate the following files (inside the dist directory):

* A .tar.gz source archive
* A .whl (wheel) binary distribution

Run the following command (in the dist directory):

.. code-block:: console

   $ pip install [name of wheel file].whl

O2Tools should now be successfully installed.