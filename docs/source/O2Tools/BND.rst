BND Documentation
------------------------------

Useful tools for BND files.

``class BndHeader()``
~~~~

The BndHeader class.

Parameters
^^^^

* ``signature (bytes)``: The signature of the BND file.
* ``object_count (int)``: The amount of objects in the BND file.

----

``class BndObject()``
~~~~

The BndObject class.

Parameters
^^^^

* ``start_x (int)``: The ``start_x`` of the object.
* ``start_y (int)``: The ``start_y`` of the object.
* ``end_x (int)``: The ``end_x`` of the object.
* ``end_y (int)``: The ``end_y`` of the object.

----

``class BND()``
~~~~

The BND file class.

Attributes
^^^^

* ``bnd_file (bytes)``: Raw bytes of the BND file.
* ``header (BndHeader)``: Parsed header of the BND file.
* ``objects (list)``: All the objects in the BND file stored as ``BndObjects``.

----

Parameters
^^^^

* ``bnd_file (bytes)``: Raw bytes of the BND file.

----

Functions
^^^^

``def get_header(self) -> BndHeader``

* NOTE: If you are trying to get the header using this, please use ``BND.header``.

Parses the header of the BND file and returns a ``BndHeader`` object.

:Returns: A ``BndHeader`` object that has all the information from the header.
:Return Type: ``BndHeader``

----

``def get_objects(self) -> list``

* NOTE: If you are trying to get the objects using this, please use ``BND.objects``.

Gets all the objects from the BND file.

:Returns: A ``list`` containing all the objects in the BND file in the form of a ``BndObject`` object.
:Return Type: ``list``

----

``def make_file(file_path: str, header: BndHeader, objects: list) -> BND``
~~~~

Assembles a BND file based off of an ``BndHeader`` object, and a list containing all the objects in the form of a ``BndObject`` object.

Parameters
^^^^

* ``file_path (str)``: The path of the file that will be made/written to.
* ``header (BndHeader)``: The header of the new BND file.
* ``objects (list)``: A list containing all the objects that will be in the new BND file.

----

:Returns: The BND file in the form of the ``BND`` class.
:Return Type: ``BND``