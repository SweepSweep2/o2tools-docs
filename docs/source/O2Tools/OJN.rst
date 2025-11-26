OJN Documentation
------------------------------

``class OJN(ojn_file: bytes)``
~~~~

Useful tools for OJN files.

Sources:

* https://open2jam.wordpress.com/the-ojn-documentation

Attributes
^^^^

``ojn_file (bytes)``: Raw bytes of the OJN file.

----

``header (OjnHeader)``: Parsed header of the OJN file.

----

``note_data (OjnNoteData)``: The note data of the OJN file (all difficulties).

----

``thumbnail (bytes)``: The 8x8 BMP thumbnail of the OJN file.

----

``cover (bytes)``: The cover image of the OJN file.

Functions
^^^^

``def get_header(self) -> OjnHeader``

    NOTE: If you are trying to get the header using this, please use ``OJN.header``.

Parses the header of the OJN file and returns an ``OjnHeader`` object.

Source: https://open2jam.wordpress.com/the-ojn-documentation

:Returns: An ``OjnHeader`` object that has all the information from the header.
:Return Type: ``OjnHeader``

----

``def parse_notes(self) -> OjnNoteData``

    NOTE: If you are trying to get the note data using this, please use ``OJN.note_data``.

Parses the notes section of the OJN file and returns an ``OjnNoteData`` object.

Source: https://open2jam.wordpress.com/2010/10/05/the-notes-section

:Returns: An ``OjnNoteData`` object that has all the note data.
:Return Type: ``OjnNoteData``

----

``def get_thumbnail(self) -> bytes``

    NOTE: If you are trying to get the thumbnail using this, please use ``OJN.thumbnail``.

Gets the thumbnail (8x8 BMP) of the OJN.

Source: https://open2jam.wordpress.com/the-ojn-documentation

:Returns: A ``bytes`` object that contains the BMP.
:Return Type: ``bytes``

----

``def get_cover(self) -> bytes``

    NOTE: If you are trying to get the cover using this, please use ``OJN.cover``.

Gets the cover of the OJN.

Source: https://open2jam.wordpress.com/the-ojn-documentation

:Returns: A ``bytes`` object that contains the cover.
:Return Type: ``bytes``

``def make_file(file_path: str, header: OjnHeader, notes: OjnNoteData, cover: bytes, thumbnail: bytes) -> OJN``
~~~~

Assembles an OJN file from an ``OjnHeader``, ``OjnNoteData``, cover, and thumbnail.

Source: https://open2jam.wordpress.com/the-ojn-documentation

----

Parameters:

    :file_path (str): The path to the file that the function will create.
    :header (OjnHeader): The header in the form of an ``OjnHeader`` object.
    :notes (OjnNoteData): The notes in the form of an ``OjnNoteData`` object.
    :cover (bytes): The JPG cover of the OJN.
    :thumbnail (bytes): The 8x8 BMP thumbnail of the OJN.

    :Returns: An ``OJN`` object that contains the file that was just created.
    :Return Type: ``OJN``