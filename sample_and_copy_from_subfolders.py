from sample_and_copy import move_sample
import os
import sys


def get_all_subfolders_name(path):
    return os.listdir(path)


if __name__ == '__main__':
    path = sys.argv[1]
    new_path = sys.argv[2]
    qtd = int(sys.argv[3])
    jump = int(sys.argv[4])
    rename = int(sys.argv[4])
    if rename == 0:
        rename = False
    else:
        rename = True

    subfolders = get_all_subfolders_name(path)
    for subfolder in subfolders:
        current_path = os.path.join(path, subfolder)
        print("current folder: ", current_path)
        dest_path = os.path.join(new_path)
        move_sample(current_path, dest_path, qtd, jump, rename)

