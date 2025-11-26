OJM Documentation
------------------------------

Useful tools for OJM files.

Sources:

* https://open2jam.wordpress.com/the-ojm-documentation
* https://github.com/open2jamorg/open2jam/blob/master/tools/ojm_dumper/OJMDumper.java (Licensed under the Artistic License 2.0)
* https://github.com/Estrol/O2Game/blob/master/Game/src/Data/OJM.cpp (Licensed under the MIT License)

``class OJM()``
~~~~

The OJM file class.

Sources:

* https://github.com/open2jamorg/open2jam/blob/master/tools/ojm_dumper/OJMDumper.java (Licensed under the Artistic License 2.0)
* https://github.com/Estrol/O2Game/blob/master/Game/src/Data/OJM.cpp (Licensed under the MIT license)
* https://open2jam.wordpress.com/the-ojm-documentation

Attributes
^^^^

* ``ojm_file (bytes)``: Raw bytes of the OJM file.
* ``header (either M30Header or OMCHeader)``: Parsed header of the OJM file.
* ``samples (list)``: All the samples in the OJM file put together in a list in either the ``M30Sample`` or ``OMCSample`` format.

Parameters
^^^^

* ``ojm_file (bytes)``: Raw bytes of the OJM file.

Functions
^^^^

``def get_m30_header(self) -> M30Header``

* NOTE: If you are trying to get the header using this, please use OJM.header.

* NOTE: This is only for the M30 type of OJM file! If the file is an OMC/OJM type, this will not work.

Gets the M30 header of the OJM file.

Source: https://open2jam.wordpress.com/the-ojm-documentation

:Returns: A ``M30Header`` object that has the header.
:Return Type: ``M30Header``

----

``def get_omc_header(self) -> OMCHeader``

* NOTE: If you are trying to get the header using this, please use OJM.header.
* NOTE: This is only for the OMC/OJM type of OJM file! If the file is an M30 type, this will not work.

Gets the OMC/OJM header of the OJM file.

Source: https://open2jam.wordpress.com/the-ojm-documentation

:Returns: An ``OMCHeader`` object that has the header.
:Return Type: ``OMCHeader``

----

``def get_header(self)``

* NOTE: If you are trying to get the header using this, please use OJM.header.

Gets the header of the OJM file. This is best if you don't know what type the OJM is.

Source: https://open2jam.wordpress.com/the-ojm-documentation

:Returns: Either a ``M30Header`` object or an ``OMCHeader`` object that has the header. Can also return ``None`` if the signature is invalid.
:Return Type: ``M30Header/OMCHeader/None``

----

``def extract_m30_samples(self) -> list``

* NOTE: If you are trying to get the samples using this, please use ``OJM.samples``.

Gets the samples of the M30 OJM file.

Sources:

* https://open2jam.wordpress.com/the-ojm-documentation
* https://github.com/Estrol/O2Game/blob/master/Game/src/Data/OJM.cpp (Licensed under the MIT license)

:Returns: A ``list`` with all the samples in the form of ``M30Sample`` objects.
:Return Type: ``list``

----

``def extract_omc_samples(self) -> list``

* NOTE: If you are trying to get the samples using this, please use ``OJM.samples``.

Gets the samples of the OJM file. (OMC/OJM)

Uses a stupid encryption and stupid arrangement logic, but I implemented it so you don't have to worry about it. You're welcome.

Sources:

* https://open2jam.wordpress.com/the-ojm-documentation
* https://github.com/Estrol/O2Game/blob/master/Game/src/Data/OJM.cpp (Licensed under the MIT license)
* https://github.com/open2jamorg/open2jam/blob/master/tools/ojm_dumper/OJMDumper.java (Licensed under the Artistic License 2.0)

:Returns: A ``list`` with all the samples in the form of ``OMCSampleWAV`` or ``OMCSampleOGG``.
:Return Type: ``list``

----

``def extract_samples(self) -> list``

* NOTE: If you are trying to get the samples using this, please use ``OJM.samples``.

Gets the samples of the OJM file. (OMC/OJM/M30)

Sources:

* https://open2jam.wordpress.com/the-ojm-documentation
* https://github.com/Estrol/O2Game/blob/master/Game/src/Data/OJM.cpp (Licensed under the MIT license)
* https://github.com/open2jamorg/open2jam/blob/master/tools/ojm_dumper/OJMDumper.java (Licensed under the Artistic License 2.0)

:Returns: A ``list`` with all the samples in the form of either ``OMCSampleWav``, ``OMCSampleOGG``, or ``M30Sample``. Can also return an empty list if the signature is invalid.
:Return Type: ``list``

``class M30Sample()``
~~~~

The M30Sample class.

Source: https://open2jam.wordpress.com/the-ojm-documentation

Parameters
^^^^

* ``sample_name (bytes)``: Name of the sample.
* ``sample_size (int)``: Size of the sample.
* ``codec_code (int)``: either 0 (background sound, note type 4, M###), or 5 (normal sound, W###).
* ``unk_fixed (int)``: Unknown data.
* ``unk_music_flag (int)``: Unknown data. Possibly a music flag.
* ``ref (int)``: The corresponding number on the OJN.
* ``unk_zero (int)``: Unknown data.
* ``pcm_samples (int)``: The amount of PCM samples on the ogg.
* ``sample (bytes)``: The full ogg sample.

``class M30Header()``
~~~~

The M30Header class.

Sources:

* https://open2jam.wordpress.com/the-ojm-documentation
* https://github.com/Estrol/O2Game/blob/master/Game/src/Data/OJM.cpp (Licensed under the MIT license)

Parameters
^^^^

* ``signature (bytes)``: File signature.
* ``file_format_version (int)``: Version of the OJM.
* ``encryption_flag (int)``:
 * 1: scramble1,
 * 2: scramble2,
 * 4: decode,
 * 8: decrypt,
 * 16: nami,
 * 32: 0412
* ``sample_count (int)``: Amount of samples on the OJM file.
* ``samples_offset (int)``: Offset that the samples begin at.
* ``payload_size (int)``: Size of the file (without header)
* ``padding (int)``: Padding(?)

``class OMCSampleOGG()``
~~~~

The OMCSampleOGG class.

Source: https://open2jam.wordpress.com/the-ojm-documentation

Parameters
^^^^

* ``sample_name (bytes)``: Name of the sample.
* ``sample_size (int)``: The size (in bytes) of the sample.
* ``sample_data (bytes)``: The raw OGG data of the sample.

``class OMCSampleWav()``
~~~~

The OMCSampleWav class.

Source: https://open2jam.wordpress.com/the-ojm-documentation

Parameters
^^^^

* ``sample_name (bytes)``: Name of the sample.
* ``audio_format (int)``: Format of the wav audio.
* ``channels_count (int)``: Amount of channels in the wav.
* ``sample_rate (int)``: Sample rate of the wav.
* ``block_align (int)``: Block align of the wav.
* ``bits_per_sample (int)``: Bits per sample of the wav.
* ``unk_data (int)``: Unknown data.
* ``chunk_size (int)``: Size of the raw wav data.
* ``wav_data (bytes)``: The raw wav data (without header)
* ``final_wav (bytes)``: The raw wav data (with header)

``class OMCHeader()``
~~~~

The OMCHeader class.

Source: https://open2jam.wordpress.com/the-ojm-documentation

Parameters
^^^^

* ``signature (bytes)``: File signature.
* ``wav_count (int)``: Amount of wav samples.
* ``ogg_count (int)``: Amount of ogg samples.
* ``wav_start (int)``: Offset of wav samples.
* ``ogg_start (int)``: Offset of ogg samples.
* ``file_size (int)``: Size of the file.

``def make_m30_file(file_path: str, header: M30Header, samples: list) -> OJM``
~~~~

Assembles an OJM file of the M30 type from a M30Header, and a list containing the samples in the format of M30Sample.

Parameters
^^^^

* ``file_path (str)``: The path to the file that the function will create.
* ``header (M30Header)``: The header in the form of an ``M30Header`` object.
* ``samples (list)``: A list containing all the samples, each sample in the ``M30Sample`` format.

----

:Returns: An ``OJM`` object that contains the file that was just created.
:Return Type: ``OJM``

``def make_file(file_path: str, header, samples: list)``
~~~~

* NOTE: Calling this function on an OMC/OJM type OJM file will raise a NotImplemented error.

Assembles an OJM file form a header, and a list containing the samples.

Parameters
^^^^

* ``file_path (str)``: The path to the file that the function will create.
* ``header``: The header of the OJM
* ``samples (list)``: A list containing all the samples, each sample in the ``M30Sample`` format.

----

:Returns: An ``OJM`` object that contains the file that was just created.
:Return Type: ``OJM``

``def xor_decrypt(data: bytes, xor: bytes) -> bytes``
~~~~

XORs data based on a 4 byte key.

Usually found in the M30 file type.

Source: https://open2jam.wordpress.com/the-ojm-documentation (modified so you can use any key)

Parameters
^^^^

* ``data (bytes)``: A ``bytes`` object with the encrypted data.
* ``xor (bytes)``: A ``bytes`` object with the XOR key.

----

:Returns: A ``bytes`` object that has the unencrypted data.
:Return Type: ``bytes``

``def rearrange(data: bytes) -> bytes``
~~~~

Rearranges data based on certain logic.

Usually found in the OMC/OJM file type.

Sources:

* https://github.com/open2jamorg/open2jam/blob/master/tools/ojm_dumper/OJMDumper.java (Licensed under the Artistic License 2.0)
* https://github.com/Estrol/O2Game/blob/master/Game/src/Data/OJM.cpp (Licensed under the MIT license)

Parameters
^^^^

* ``data (bytes)``: A bytes object with the arranged data.

----

:Returns: A bytes object that has the rearranged data.
:Return Type: bytes

``def acc_xor(data: bytes, acc_key_byte: int, acc_counter: int) -> list``
~~~~

Decrypts bytes using acc_xor (but it's stupid so it's not actually xor)

Usually found in the OMC/OJM file type.

Sources:

* https://github.com/open2jamorg/open2jam/blob/master/tools/ojm_dumper/OJMDumper.java (Licensed under the Artistic License 2.0)
* https://github.com/Estrol/O2Game/blob/master/Game/src/Data/OJM.cpp (Licensed under the MIT license)

Parameters
^^^^

* ``data (bytes)``: A ``bytes`` object with the encrypted data.
* ``acc_key_byte (int)``: Needs documentation.
* ``acc_counter (int)``: Needs documentation.

----

:Returns: A ``list`` object that contains the new ``acc_key_byte``, the new ``acc_counter``, and the unencrypted data.
:Return Type: ``list``