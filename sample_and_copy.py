import sys
import os
from change_resolutions import create_directory_if_not_exists
import uuid


def move_sample(current_path, dest_path, quantity, jump_files, to_rename=True):
    create_directory_if_not_exists(dest_path)
    file_names = os.listdir(current_path)
    for i, file_name in enumerate(file_names):
        if jump_files > 0:
            jump_files -= 1
            continue

        if i == quantity:
            break
        input_path = os.path.join(current_path, file_name)
        if to_rename:
            new_file_name = get_random_name() + ".jpg"
        else:
            new_file_name = file_name
        output_path = os.path.join(dest_path, new_file_name)
        print("moving file: ", file_name, " to: ", new_file_name)
        os.rename(input_path, output_path)


def get_random_name():
    return str(uuid.uuid4())


if __name__ == '__main__':
    path = sys.argv[1]
    new_path = sys.argv[2]
    qtd = int(sys.argv[3])
    rename = int(sys.argv[4])
    jump = int(sys.argv[4])
    if rename == 0:
        rename = False
    else:
        rename = True
    move_sample(path, new_path, qtd, jump, rename)
