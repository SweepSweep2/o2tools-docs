OPI Documentation
------------------------------

Useful tools for OPI files.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/OPIParser.cs (licensed under the MIT License)

``class OpiHeader()``
~~~~

The OpiHeader class.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/OPIParser.cs (licensed under the MIT License)

Parameters
^^^^

* ``file_type (int)``: Type of file.
* ``file_count (int)``: The amount of files in the OPI.

----

``class OpiFile()``
~~~~

The OpiFile class.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/OPIParser.cs (licensed under the MIT License)

Parameters
^^^^

* ``unk_int (int)``: Unknown data.
* ``file_name (bytes)``: Name of the file.
* ``offset (int)``: Offset of the file in the OPI file.
* ``size_1 (int)``: If this is the biggest size, it is the size of the file.
* ``size_2 (int)``: If this is the biggest size, it is the size of the file.
* ``unk_bytes (bytes)``: Unknown data.
* ``data (bytes)``: The file.

``class OPI()``
~~~~

The OPI file class.

Attributes
^^^^

* ``opi_file (bytes)``: Raw bytes of the OPI file.
* ``header (OpiHeader)``: Parsed header of the OPI file.
* ``files (list)``: The files of the OPI stored in the ``OpiFile`` object.

----

Parameters
^^^^

* ``opi_file (bytes)``: Raw bytes of the OPI file.

----

Functions
^^^^

``def get_header(self) -> OpiHeader``

* NOTE: If you are trying to get the header using this, please use ``OPI.header``.

Parses the header of the OPI file and returns an ``OpiHeader`` object.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/OPIParser.cs (licensed under the MIT License)

:Returns: An ``OpiHeader`` object that has all the information from the header.
:Return Type: ``OpiHeader``

----

``def get_files(self) -> list``

* NOTE: If you are trying to get the files using this, please use OPI.files.

Gets the files of the OPI file.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/OPIParser.cs (licensed under the MIT License)

:Returns: A list that has all the files in the form of OpiFiles.
:Return Type: list

----

``def make_file(file_path: str, header: OpiHeader, files: list) -> OPI``
~~~~

* NOTE: This will not make a 1:1 replica of the file, as it leaves out unnecessary bytes and sorts the files by their offsets.

Assembles an OPI file based off of an ``OpiHeader`` object, and a list containing all the files in the form of an ``OpiFile`` object.

It's also an OPI optimizer because it removes padding bytes.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/OPIParser.cs (licensed under the MIT License)

Parameters
^^^^

* ``file_path (str)``: The file path of the new OPI file.
* ``header (OpiHeader)``: The header of the new OPI file.
* ``files (list)``: A list of files in the new OPI file.

:Returns: The OPI file in the form of the ``OPI`` class.
:Return Type: ``OPI``