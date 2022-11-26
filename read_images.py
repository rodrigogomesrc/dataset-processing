import cv2
import os


def read_images(path):
    images = []
    file_names = os.listdir(path)
    for file_name in file_names:
        input_path = os.path.join(path, file_name)
        img = cv2.imread(input_path)
        if img is not None:
            images.append(img)

    return images


if __name__ == '__main__':
    pass
