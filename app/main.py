import os


def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file = parts[1]
    file_copy = parts[2]

    if not os.path.exists(source_file):
        return

    if source_file == file_copy:
        return

    with open(source_file, "r") as file_out, open(file_copy, "w") as file_in:
        file_in.write(file_out.read())
