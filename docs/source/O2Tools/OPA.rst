OPA Documentation
------------------------------

Useful tools for OPA files.

This has the same functionality as OPI files.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/OPIParser.cs (licensed under the MIT License)

``class OpaHeader()``
~~~~

The OpaHeader class.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/OPIParser.cs (licensed under the MIT License)

Parameters
^^^^

* ``file_type (int)``: Type of file.
* ``file_count (int)``: The amount of files in the OPA.

----

``class OpaFile()``

The OpaFile class.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/OPIParser.cs (licensed under the MIT License)

Parameters
^^^^

* ``unk_int (int)``: Unknown data.
* ``file_name (bytes)``: Name of the file.
* ``offset (int)``: Offset of the file in the OPA file.
* ``size_1 (int)``: If this is the biggest size, it is the size of the file.
* ``size_2 (int)``: If this is the biggest size, it is the size of the file.
* ``unk_bytes (bytes)``: Unknown data.
* ``data (bytes)``: The file.

``class OPA()``
~~~~

The OPA file class.

Attributes
^^^^

* ``opa_file (bytes)``: Raw bytes of the OPA file.
* ``header (OpaHeader)``: Parsed header of the OPA file.
* ``files (list)``: The files of the OPA stored in the ``OpaFile`` object.

----

Parameters
^^^^

* ``opa_file (bytes)``: Raw bytes of the OPA file.

----

Functions
^^^^

``def get_header(self) -> OpaHeader``

* NOTE: If you are trying to get the header using this, please use ``OPA.header``.

Parses the header of the OPA file and returns an ``OpaHeader`` object.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/OPIParser.cs (licensed under the MIT License)

:Returns: An ``OpaHeader`` object that has all the information from the header.
:Return Type: ``OpaHeader``

----

``def get_files(self) -> list``

* NOTE: If you are trying to get the files using this, please use OPA.files.

Gets the files of the OPA file.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/OPIParser.cs (licensed under the MIT License)

:Returns: A list that has all the files in the form of OpaFiles.
:Return Type: list

----

``def make_file(file_path: str, header: OpaHeader, files: list) -> OPA``
~~~~

* NOTE: This will not make a 1:1 replica of the avatar file, as it leaves out unnecessary bytes and sorts the files by their offsets.

Assembles an OPA file based off of an ``OpaHeader`` object, and a list containing all the files in the form of an ``OpaFile`` object.

It's also an OPA optimizer because it removes padding bytes.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/OPIParser.cs (licensed under the MIT License)

Parameters
^^^^

* ``file_path (str)``: The file path of the new OPA file.
* ``header (OpaHeader)``: The header of the new OPA file.
* ``files (list)``: A list of files in the new OPA file.

:Returns: The OPA file in the form of the ``OPA`` class.
:Return Type: ``OPA``