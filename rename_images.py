import sys
import os


def rename_images(path, basename):
    file_names = os.listdir(path)
    for i, file_name in enumerate(file_names):
        input_path = os.path.join(path, file_name)
        new_file_name = basename + "_" + str(i)
        output_path = os.path.join(path, new_file_name)
        print("renaming file: ", file_name, " to: ", new_file_name)
        os.rename(input_path, output_path)


if __name__ == '__main__':
    directory = sys.argv[1]
    name = sys.argv[2]
    rename_images(directory, name)

