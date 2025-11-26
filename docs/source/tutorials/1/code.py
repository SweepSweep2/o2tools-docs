import o2tools

file_path = input("Enter the path of your OJN file: ")

with open(file_path, "rb") as f:
    ojn_file = o2tools.ojn.OJN(f.read())
    property = input("Enter the name of the value you want to change: ")
    new_value = input("Enter the new value: ")
    print("Changing...")

    try:
        new_value = int(new_value)
    except ValueError:
        try:
            new_value = float(new_value)
        except ValueError:
            new_value = new_value.encode("ISO-8859-1")

    setattr(ojn_file.header, property, new_value)
    o2tools.ojn.make_file(file_path, ojn_file.header, ojn_file.note_data, ojn_file.cover, ojn_file.thumbnail)

    print("Changed!")