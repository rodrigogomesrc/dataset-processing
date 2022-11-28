import os
import sys
from sample_and_copy_from_subfolders import get_all_subfolders_name
from change_resolutions import create_directory_if_not_exists


def create_dataset(path, new_path):
    subfolders = get_all_subfolders_name(path)
    labels = []
    label_id = 0
    labels.append("id,filename,class")
    create_directory_if_not_exists(new_path)
    create_directory_if_not_exists(os.path.join(new_path, "data"))
    for subfolder in subfolders:
        filenames = os.listdir(os.path.join(path, subfolder))
        for filename in filenames:
            print("moving file: ", filename, " to: ", new_path)
            label = str(label_id) + "," + str(filename) + "," + str(subfolder)
            labels.append(label)
            label_id += 1
            complete_path = os.path.join(path, subfolder, filename)
            new_complete_path = os.path.join(new_path, "data/" + str(filename))
            os.rename(complete_path, new_complete_path)

    save_labels_to_csv_file(labels, new_path)


def save_labels_to_csv_file(labels, new_path):
    with open(os.path.join(new_path, "labels.csv"), "w") as file:
        for label in labels:
            file.write(label + "\n")


if __name__ == '__main__':
    path = sys.argv[1]
    new_path = sys.argv[2]
    create_dataset(path, new_path)
