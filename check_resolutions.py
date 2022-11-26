import sys
import os
import cv2


def get_images_resolutions(path):
    file_names = os.listdir(path)
    resolution_list = []
    for file_name in file_names:
        input_path = os.path.join(path, file_name)
        img = cv2.imread(input_path)
        if img is not None:
            print("resolution of image: ", file_name, " is: ", img.shape)
            resolution_list.append(img.shape)
    return resolution_list


def check_if_resolutions_are_equal(resolution_list):
    return len(set(resolution_list)) == 1


def print_resolutions(resolution_list):
    for resolution in resolution_list:
        print(resolution)


if __name__ == '__main__':
    directory = sys.argv[1]
    if not directory:
        print('Please provide a directory')
        sys.exit(1)

    resolutions = get_images_resolutions(directory)
    #print_resolutions(resolutions)
    print("Images have the same resolution: ", check_if_resolutions_are_equal(resolutions))
