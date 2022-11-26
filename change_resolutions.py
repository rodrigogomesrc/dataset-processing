import cv2
import sys
from read_images import read_images
import os


def change_resolution(image, width, height):
    return cv2.resize(image, (width, height))


def save_images_with_new_resolution(images, new_path, width, height, name):
    create_directory_if_not_exists(new_path)
    for i, image in enumerate(images):
        image_path = new_path + "/" + name + "_" + str(i) + "_(" + str(width) + "x" + str(height) + ")" + '.jpg'
        print("saving image: ", image_path)
        new_image = change_resolution(image, width, height)
        cv2.imwrite(image_path, new_image)


def create_directory_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == '__main__':
    current_path = sys.argv[1]
    new_path = sys.argv[2]
    image_width = int(sys.argv[3])
    image_height = int(sys.argv[4])
    name = sys.argv[5]
    original_images = read_images(current_path)
    save_images_with_new_resolution(original_images, new_path, image_width, image_height, name)
