import sys
from read_images import read_images


def get_images_resolutions(path):
    images = read_images(path)
    resolution_list = []
    for image in images:
        resolution_list.append(image.shape)
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
