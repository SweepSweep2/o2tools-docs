Tutorial 1 - OJN Header Changer
-------------------------------

In this tutorial, we will write a simple program that will ask for an OJN file, ask for what we want to change with the header, and edit the file with these changes.

The program will look something like this:

.. image:: https://github.com/SweepSweep2/o2tools-docs/blob/main/docs/source/tutorial1/tut1gif1.gif

General Layout
--------------

Let's make the general layout of this program.

We want the program to do the following:

- Ask the user for the file
- Open up the file
- Ask the user for the property they want to change
- Ask the user for the value they want to set it to
- Get the header of the current file and replace the property with the value the user specified
- Overwrite the file with a new file, and set it up with the modified header and original note data

Program Structure
-----------------

Let's begin making the program.

Here is the structure of the program (no logic added):

.. codeblock:: python

  import o2tools

  ojn_file = o2tools.ojn.OJN(input("Enter your OJN file: "))
  property = input("Enter the name of the value you want to change: ")
  new_value = input("Enter the new value: ")
  print("Changing...")

  # change the ojn here

  print("Changed!")

We will go through this code one by one so you understand everything.

====

``ojn_file = o2tools.ojn.OJN(input("Enter your OJN file: "))``

Here, we ask the user for the path to the OJN file and open it. ``OJN()``'s only parameter is the file path, which is why we can feed the input directly into ``OJN()``.

====

.. codeblock:: python

  property = input("Enter the name of the value you want to change: ")
  new_value = input("Enter the new value: ")
  print("Changing...")

  # change the ojn here

  print("Changed!")

The rest of the file is just collecting more data from the user, which we dont need to go over.

Changing the Property
---------------------

Next, we need to change the property. We could go through a lot of if statements to see what the user put, but that is lazy and inefficient. Instead, we can use the ``setattr()`` function.

.. codeblock:: python

  import o2tools

  ojn_file = o2tools.ojn.OJN(input("Enter your OJN file: "))
  new_property = input("Enter the name of the value you want to change: ")
  new_value = input("Enter the new value: ")
  print("Changing...")

  setattr(ojn_file.header, new_property, new_value)

  print("Changed!")

====

We only added one line, ``setattr(ojn_file.header, new_property, new_value)``. This line gets the attribute in ojn_file.header (``OjnHeader`` class) from a string (``new_property``), and sets the attribute to ``new_value``.

====

To test if this is working, put this code below the ``setattr()`` function:

.. codeblock:: python

  print(getattr(ojn_file.header, new_property))

====

``getattr()`` works similar to ``setattr()``, but this time gets the attribute instead of setting it.

====

You should be seeing something like this in the console:

.. codeblock:: text

  Enter your OJN file: o2ma105.ojn
  Enter the name of the value you want to change: song_id
  Enter the new value: 33
  Changing...
  33
  Changed!

If you see this, good job! If you don't, make sure to read the previous code very carefully.

Modifying the File
------------------

To assemble everything into a file, you would usually need to make a new file (overwrite the file in this case) and start adding all of the header values and note data to it. Luckily, O2Tools already has a function for this, called ``make_file()``.

You can either call ``o2tools.ojn.make_file()``, or ``o2tools.make_file()``. Both work the same, but because we are working with OJN files, we are going to use ``o2tools.ojn.make_file()``.

====

Let's add this to the code:

.. codeblock:: python

  import o2tools
    
  ojn_file = o2tools.ojn.OJN(input("Enter your OJN file: "))
  new_property = input("Enter the name of the value you want to change: ")
  new_value = input("Enter the new value: ")
  print("Changing...")
    
  setattr(ojn_file.header, new_property, new_value)
  o2tools.ojn.make_file(ojn_file.ojn_file_path, ojn_file.header, ojn_file.note_data)
    
  print("Changed!")

====

``o2tools.ojn.make_file(ojn_file.ojn_file_path, ojn_file.header, ojn_file.note_data)``

This function makes a new file with the name in the first parameter (``ojn_file.ojn_file_path``, which is what the user specified in the first input statement).

The header in the second parameter(``ojn_file.header``, as we changed the header directly).

And the note data in the third parameter (``ojn_file.note_data``, we didnt do anything to the note data so it stays the same).

====

Technically, you are done now!

But we still need to add error checking, as the user can enter the wrong type, and it is impossible to type bytes.

Error Checking
--------------

Here is the full, complete code for this program:

.. codeblock:: python

  import o2tools
  
  ojn_file = o2tools.ojn.OJN(input("Enter your OJN file: "))
  new_property = input("Enter the name of the value you want to change: ")
  new_value = input("Enter the new value: ")
  print("Changing...")
  
  try:
      new_value = int(new_value)
  except ValueError:
      try:
          new_value = float(new_value)
      except ValueError:
          new_value = new_value.encode("ISO-8859-1")
  
  setattr(ojn_file.header, new_property, new_value)
  o2tools.ojn.make_file(ojn_file.ojn_file_path, ojn_file.header, ojn_file.note_data)
  
  print("Changed!")

====

.. codeblock:: python

  try:
      new_value = int(new_value)
  except ValueError:
      try:
          new_value = float(new_value)
      except ValueError:
          new_value = new_value.encode("ISO-8859-1")

This looks a bit hard to explain, so I think it's better if we step through to see whats happening.

====

.. codeblock:: python

  try:
      new_value = int(new_value)

We try to convert the value the user inputted into an integer.

====

.. codeblock:: python

  except ValueError:
      try:
          new_value = float(new_value)

If it fails, try to convert it into a float.

====

.. codeblock:: python

  except ValueError:
      new_value = new_value.encode("ISO-8859-1")

And finally, if that fails, convert it into a bytes object (with encoding ISO-8859-1).

Challenge
---------

You may have realized something about this code: it doesn't check if the property the user specified is an actual property.

If you want an extra challenge, add checks that make sure the property that the user puts in is valid.

Conclusion
----------

You have written your first O2Tools program! You have done the following:

- Edit the OJN's header
- Construct an OJN file
- Converted user input into the right type
- Made an easy to use program to automate everything

As you can tell, this can get pretty easy to learn, as the actual process of parsing these files are all done by O2Tools and not the user.

If you want to learn more, you can go to the next tutorial, or check out the documentation for both the file formats and O2Tools.

You can also download the python file here.
