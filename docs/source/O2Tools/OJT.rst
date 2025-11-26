OJT Documentation
------------------------------

Useful tools for OJT files.

Same as OJSs and OJIs.

Sources:

* https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSData.cs (licensed under the MIT License)
* https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSFrame.cs (licensed under the MIT License)

``class OjtHeader()``
~~~~

The OjtHeader class.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSData.cs (licensed under the MIT License)

Parameters
^^^^

* ``file_format (int)``: Type of file.
* ``color_format (int)``: The color format of the OJT (in big endian).
* ``frame_count (int)``: The amount of frames in the OJT.

----

``class OjtFrame()``
~~~~

The OjtFrame class.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSFrame.cs (licensed under the MIT License)

Parameters
^^^^

* ``transparent_color (int)``: The transparent color of the frame in the format BGR555.
* ``x (int)``: X position of the frame.
* ``y (int)``: Y position of the frame.
* ``width (int)``: Width of the frame.
* ``height (int)``: Height of the frame.
* ``offset (int)``: Offset of the frame.
* ``size (int)``: Size of the frame.
* ``unk (int)``: Unknown data.
* ``data (bytes)``: Data of the frame.
* ``bmp_file (bytes)``: BMP file.

----

``class OJT()``
~~~~

The OJT file class.

Sources:

* https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSData.cs (licensed under the MIT License)
* https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSFrame.cs (licensed under the MIT License)

Attributes
^^^^

* ``ojt_file (bytes)``: The raw bytes of the OJT file.
* ``header (OjtHeader)``: The header of the OJT file in the ``OjtHeader`` type.
* ``frames (list)``: A list containing all the frames in the ``OjtFrame`` type.

----

Parameters
^^^^

* ``ojt_file (bytes)``: Raw bytes of the OJT file.

----

Functions
^^^^

``def get_header(self) -> OjtHeader``

* NOTE: If you are trying to get the header using this, please use ``OJT.header``.

Parses the header of the OJT file and returns an ``OjtHeader`` object.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSData.cs (licensed under the MIT License)

:Returns: An ``OjtHeader`` object that has all the information from the header.
:Return Type: ``OjtHeader``

----

``def get_frames(self) -> list``

* NOTE: If you are trying to get the frames using this, please use ``OJT.frames``.

Gets the frames of the OJT file and returns a list containing all the frames in the ``OjtFrame`` format.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSFrame.cs (licensed under the MIT License)

:Returns: A ``list`` that has all the frames in the ``OjtFrame`` format.
:Return Type: ``list``

``def make_file(file_path: str, header: OjtHeader, frames: list) -> OJT``
~~~~

Assembles an OJT file based off of an ``OjtHeader`` object, and a list containing all the frames in the form of an ``OjtFrame`` object.

Sources:

* https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSData.cs (licensed under the MIT License)
* https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSFrame.cs (licensed under the MIT License)

Parameters
^^^^

* ``file_path (str)``: The file path of the new OJT file.
* ``header (OjtHeader)``: The header of the new OJT file.
* ``frames (list)``: A list of all the frames in the new OJT file.

----

:Returns: The OJT file in the form of the ``OJT`` class.
:Return Type: ``OJT``