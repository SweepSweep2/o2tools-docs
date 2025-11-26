OJN List Documentation
------------------------------

This is not 100% finished! There are dates and some unknown bytes at the end of only some OJN list files that seem to be completely ignored.

If you know how the data for OJN List files are handled, you can contribute at https://github.com/SweepSweep2/o2tools

Useful tools for OJN List files.

``class OjnListHeader()``
~~~~

The ``OjnListHeader`` class.

Parameters
^^^^

* ``ojn_count (int)``: Amount of OJNs in the OJN list.

----

``class OJNList()``
~~~~

The OJN List file class.

Attributes
^^^^

* ``ojn_list_file (bytes)``: Raw bytes of the OJN List file.
* ``header (OjnListHeader)``: Parsed header of the OJN List file.
* ``ojns (list)``: All the OJN headers in the OJN List file, stored as ``OjnHeaders`` ``(o2tools.ojn.OjnHeader)``.

----

Parameters
^^^^

* ``ojn_list_file (bytes)``: Raw bytes of the OJN List file.

----

Functions
^^^^

``def get_header(self) -> OjnListHeader``

* NOTE: If you are trying to get the header using this, please use ``OJNList.header``.

Parses the header of the OJN List file and returns an ``OjnListHeader`` object.

:Returns: An ``OjnListHeader`` object that has all the information from the header.
:Return Type: ``OjnListHeader``

----

``def get_ojns(self) -> list``

* NOTE: If you are trying to get the OJNs using this, please use ``OJNList.ojns``.

Gets all the OJN headers in the file and stores them as ``OjnHeaders`` ``(o2tools.ojn.OjnHeader)`` inside a list.

:Returns: A ``list`` that has all the headers in the ``OjnHeader`` format.
:Return Type: ``list``

``def make_file(file_path: str, header: OjnListHeader, ojns: list) -> OJNList``
~~~~

* NOTE: Some OJN Lists have dates at the end of them, which O2Tools currently does not support. That means the OJN Lists generated might not work in some versions of O2Jam.

Assembles an OJN List file based off of an ``OjnListHeader`` object, and a list containing all the OJN headers in the form of an ``OjnHeader`` object ``(o2tools.ojn.OjnHeader)``.

:Returns: The OJN List file in the form of the ``OJNList`` class.
:Return Type: ``OJNList``