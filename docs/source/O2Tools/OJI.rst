OJI Documentation
------------------------------

Useful tools for OJI files.

Same as OJTs and OJSs.

Sources:

* https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSData.cs (licensed under the MIT License)
* https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSFrame.cs (licensed under the MIT License)

``class OjiHeader()``
~~~~

The OjiHeader class.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSData.cs (licensed under the MIT License)

Parameters
^^^^

* ``file_format (int)``: Type of file.
* ``color_format (int)``: The color format of the OJI (in big endian).
* ``frame_count (int)``: The amount of frames in the OJI.

----

``class OjiFrame()``
~~~~

The OjiFrame class.

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

``class OJI()``
~~~~

The OJI file class.

Sources:

* https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSData.cs (licensed under the MIT License)
* https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSFrame.cs (licensed under the MIT License)

Attributes
^^^^

* ``oji_file (bytes)``: The raw bytes of the OJI file.
* ``header (OjiHeader)``: The header of the OJI file in the ``OjiHeader`` type.
* ``frames (list)``: A list containing all the frames in the ``OjiFrame`` type.

----

Parameters
^^^^

* ``oji_file (bytes)``: Raw bytes of the OJI file.

----

Functions
^^^^

``def get_header(self) -> OjiHeader``

* NOTE: If you are trying to get the header using this, please use ``OJI.header``.

Parses the header of the OJI file and returns an ``OjiHeader`` object.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSData.cs (licensed under the MIT License)

:Returns: An ``OjiHeader`` object that has all the information from the header.
:Return Type: ``OjiHeader``

----

``def get_frames(self) -> list``

* NOTE: If you are trying to get the frames using this, please use ``OJI.frames``.

Gets the frames of the OJI file and returns a list containing all the frames in the ``OjiFrame`` format.

Source: https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSFrame.cs (licensed under the MIT License)

:Returns: A ``list`` that has all the frames in the ``OjiFrame`` format.
:Return Type: ``list``

``def make_file(file_path: str, header: OjiHeader, frames: list) -> OJI``
~~~~

Assembles an OJI file based off of an ``OjiHeader`` object, and a list containing all the frames in the form of an ``OjiFrame`` object.

Sources:

* https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSData.cs (licensed under the MIT License)
* https://github.com/Estrol/X3Solo/blob/master/Estrol.X3Solo/Parser/Data/OJSFrame.cs (licensed under the MIT License)

Parameters
^^^^

* ``file_path (str)``: The file path of the new OJI file.
* ``header (OjiHeader)``: The header of the new OJI file.
* ``frames (list)``: A list of all the frames in the new OJI file.

----

:Returns: The OJI file in the form of the ``OJI`` class.
:Return Type: ``OJI``