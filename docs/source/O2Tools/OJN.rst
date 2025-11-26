OJN Documentation
------------------------------

Useful tools for OJN files.

Sources:

* https://open2jam.wordpress.com/the-ojn-documentation

``class NoteEvent()``
~~~~

The NoteEvent class.

Source: https://open2jam.wordpress.com/2010/10/05/the-notes-section

Parameters
^^^^

* ``value (int)``: Padding/Reference to the sample on the OJM file.
* ``volume (int)``: The volume to play the sample on. Goes from 1 to 15, and 0 is the max volume.
* ``pan (int)``: The panning of the sample. 1 to 7 is left to center, 0 or 8 is center, 9 to 15 is center to right.
* ``note_type (int)``:
 * 0 = normal note,
 * 2 = start of long note,
 * 3 = end of long note,
 * 4 = OGG sample trigger.

----

``class PackageHeader()``
~~~~

The PackageHeader class.

Source: https://open2jam.wordpress.com/2010/10/05/the-notes-section

Parameters
^^^^

* ``measure (int)``: The measure in which the events inside this package will appear.
* ``channel (int)``:
 * 0 = measure fraction
 * 1 = BPM change
 * 2 = note on 1st lane
 * 3 = note on 2nd lane
 * 4 = note on 3rd lane
 * 5 = note on 4th lane
 * 6 = note on 5th lane
 * 7 = note on 6th lane
 * 8 = note on 7th lane
 * 9 and onwards - autoplay sample
* ``event_count (int)``: The number of events inside this package.

----

``class OjnNoteData()``
~~~~

The OjnNoteData class.

Source: https://open2jam.wordpress.com/2010/10/05/the-notes-section

Layout:

.. code-block:: python

   {(measure, channel): [event_count, NoteEvent, NoteEvent, etc.]}

Example:

.. code-block:: python

   {(3, 4): [4, NoteEvent(0, 0, 0, 0), NoteEvent(0, 0, 0, 0), NoteEvent(5, 0, 0, 2), NoteEvent(6, 0, 0, 3)]}

Parameters
^^^^

* ``note_data_easy (dict)``: Note data for the easy difficulty
* ``note_data_normal (dict)``: Note data for the medium difficulty
* ``note_data_hard (dict)``: Note data for the hard difficulty

----

``class OjnHeader()``
~~~~

The OjnHeader class.

Source: https://open2jam.wordpress.com/the-ojn-documentation

Parameters
^^^^

* ``song_id (int)``: The ID of the song, usually the same ID as in the name of the file.
* ``signature (bytes)``: Magic number to identify the files (usually ojn<null>)
* ``encode_version (float)``: The OJN encode version (usually 2.9)
* ``genre (int)``: A number that represents the genre of the song. All genres are in the GENRE_LIST constant.
* ``bpm (float)``: The song BPM (changing this will not affect the song speed).
* ``easy_level (int)``: The level of the easy difficulty.
* ``normal_level (int)``: The level of the medium difficulty.
* ``hard_level (int)``: The level of the hard difficulty.
* ``easy_event_count (int)``: The amount of events in the easy difficulty.
* ``normal_event_count (int)``: The amount of events in the medium difficulty.
* ``hard_event_count (int)``: The amount of events in the hard difficulty.
* ``easy_note_count (int)``: The amount of notes in the easy difficulty.
* ``normal_note_count (int)``: The amount of notes in the medium difficulty.
* ``hard_note_count (int)``: The amount of notes in the hard difficulty.
* ``easy_measure_count (int)``: The amount of measures in the easy difficulty.
* ``normal_measure_count (int)``: The amount of measures in the medium difficulty.
* ``hard_measure_count (int)``: The amount of measures in the hard difficulty.
* ``easy_package_count (int)``: The amount of packages in the easy difficulty.
* ``normal_package_count (int)``: The amount of packages in the medium difficulty.
* ``hard_package_count (int)``: The amount of packages in the hard difficulty.
* ``old_encode_version (int)``: Unused encode version that got superseded by encode_version.
* ``old_song_id (int)``: Unused song ID (most likely changed because this one is only a short)
* ``old_genre (bytes)``: Old genre string before they switched to the number-based genre system.
* ``bmp_size (int)``: The size (in bytes) of the thumbnail image.
* ``old_file_version (int)``: Old (?) version of the file. Needs more research.
* ``title (bytes)``: The title of the song.
* ``artist (bytes)``: The artist of the song.
* ``noter (bytes)``: The noter of the chart.
* ``ojm_file (bytes)``: The corresponding OJM file.
* ``cover_size (int)``: The size (in bytes) of the cover image.
* ``easy_time (int)``: The duration (in seconds) of the easy difficulty.
* ``normal_time (int)``: The duration (in seconds) of the medium difficulty.
* ``hard_time (int)``: The duration (in seconds) of the hard difficulty.
* ``easy_note_offset (int)``: The offset of the note section for the easy difficulty.
* ``normal_note_offset (int)``: The offset (in bytes) of the note section for the medium difficulty.
* ``hard_note_offset(int)``: The offset (in bytes) of the note section for the hard difficulty.
* ``cover_offset (int)``: The offset (in bytes) of the cover image.

----

``class OJN()``
~~~~

The OJN file class.

Parameters
^^^^
* ``ojn_file (bytes)``: Raw bytes of the OJN file.

Attributes
^^^^

* ``ojn_file (bytes)``: Raw bytes of the OJN file.
* ``header (OjnHeader)``: Parsed header of the OJN file.
* ``note_data (OjnNoteData)``: The note data of the OJN file (all difficulties).
* ``thumbnail (bytes)``: The 8x8 BMP thumbnail of the OJN file.
* ``cover (bytes)``: The cover image of the OJN file.

Functions
^^^^

``def get_header(self) -> OjnHeader``

* NOTE: If you are trying to get the header using this, please use ``OJN.header``.

Parses the header of the OJN file and returns an ``OjnHeader`` object.

Source: https://open2jam.wordpress.com/the-ojn-documentation

:Returns: An ``OjnHeader`` object that has all the information from the header.
:Return Type: ``OjnHeader``

----

``def parse_notes(self) -> OjnNoteData``

* NOTE: If you are trying to get the note data using this, please use ``OJN.note_data``.

Parses the notes section of the OJN file and returns an ``OjnNoteData`` object.

Source: https://open2jam.wordpress.com/2010/10/05/the-notes-section

:Returns: An ``OjnNoteData`` object that has all the note data.
:Return Type: ``OjnNoteData``

----

``def get_thumbnail(self) -> bytes``

* NOTE: If you are trying to get the thumbnail using this, please use ``OJN.thumbnail``.

Gets the thumbnail (8x8 BMP) of the OJN.

Source: https://open2jam.wordpress.com/the-ojn-documentation

:Returns: A ``bytes`` object that contains the BMP.
:Return Type: ``bytes``

----

``def get_cover(self) -> bytes``

* NOTE: If you are trying to get the cover using this, please use ``OJN.cover``.

Gets the cover of the OJN.

Source: https://open2jam.wordpress.com/the-ojn-documentation

:Returns: A ``bytes`` object that contains the cover.
:Return Type: ``bytes``

----

``def make_file(file_path: str, header: OjnHeader, notes: OjnNoteData, cover: bytes, thumbnail: bytes) -> OJN``
~~~~

Assembles an OJN file from an ``OjnHeader``, ``OjnNoteData``, cover, and thumbnail.

Source: https://open2jam.wordpress.com/the-ojn-documentation

----

Parameters:

* ``file_path (str)``: The path to the file that the function will create.
* ``header (OjnHeader)``: The header in the form of an ``OjnHeader`` object.
* ``notes (OjnNoteData)``: The notes in the form of an ``OjnNoteData`` object.
* ``cover (bytes)``: The JPG cover of the OJN.
* ``thumbnail (bytes)``: The 8x8 BMP thumbnail of the OJN.

----

:Returns: An ``OJN`` object that contains the file that was just created.
:Return Type: ``OJN``

----

``def get_header(ojn_file: bytes) -> OjnHeader``
~~~~

Parses the header of the OJN file and returns an OjnHeader object.

Source: https://open2jam.wordpress.com/the-ojn-documentation

----

Parameters:

* ``ojn_file (bytes)``: The raw bytes of the OJN file.

----

:Returns: An OjnHeader object that has all the information from the header.
:Return Type: OjnHeader
