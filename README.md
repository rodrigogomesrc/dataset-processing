# dataset-processing

Functions to process images to create a cohesive dataset


## Check Resolutions

The script `check_resolutions.py` allows you to check if images in a specified folder have the same resolution.

### Code Overview

The script consists of the following functions:

1. **get_images_resolutions(path):**
    - Retrieves the resolutions of images in the specified `path` and prints the resolution of each image.

2. **check_if_resolutions_are_equal(resolution_list):**
    - Checks if all resolutions in the provided list are equal.

3. **print_resolutions(resolution_list):**
    - Prints the resolutions from the given list.

### How to Run the Script

Execute the script by running the following command in the terminal:

```bash
python3 check_resolutions.py <folder_path>
```

`<folder_path>`: Path to the folder containing the images you want to check.

### Example execution
```bash
python check_resolutions.py /path/to/images_folder
```

This command will print the resolutions of each image in the specified folder and indicate whether all images have the same resolution.

## Change resolution

The script `change_resolutions.py` allows you to change the resolution of a collection of images in a specified folder.

### Code Overview

The script consists of the following functions:

1. **change_resolution(image, width, height):**
    - Takes an input image and resizes it to the specified width and height.

2. **save_images_with_new_resolution(current_path, new_path, width, height, name):**
    - Iterates through images in the given `current_path`, resizes them using `change_resolution()`, and saves the new images to the `new_path` with a specified name pattern.

3. **create_directory_if_not_exists(path):**
    - Checks if the directory at the given `path` exists and creates it if not.

### How to Run the Script

Execute the script by running the following command in the terminal:

```bash
python3 change_resolutions.py <source_folder_path> <destination_folder_path> <image_width> <image_height> <output_name_pattern>
```

`<source_folder_path>`: Path to the folder containing the original images.
`<destination_folder_path>`: Path where the resized images will be saved.
`<image_width>`: Desired width for the resized images.
`<image_height>`: Desired height for the resized images.
`<output_name_pattern>`: Prefix for the names of the resized images.

### Example execution

```bash
python change_resolutions.py /path/to/original_images /path/to/destination_images 800 600 resized
```

This command will resize images from the "original_images" folder to a resolution of 800x600 and save them in the "destination_images" folder with names like "resized_0_(800x600).jpg".


## Create Dataset from Folders

The script `create_dataset_from_folders.py` allows you to organize images from subfolders into a dataset.

### Code Overview

The script consists of the following functions:

1. **create_dataset(path, new_path):**
    - Retrieves images from subfolders in the specified `path` and organizes them into a dataset in the `new_path`. It also generates labels for each image.

2. **save_labels_to_csv_file(labels, new_path):**
    - Saves the generated labels to a CSV file in the specified `new_path`.

### How to Run the Script

Execute the script by running the following command in the terminal:

```bash
python3 create_dataset_from_folders.py <source_folder_path> <destination_folder_path>
```

`<source_folder_path>`: Path to the folder containing subfolders with images.
`<destination_folder_path>`: Path where the dataset will be created.

### Example execution

```bash
python create_dataset_from_folders.py /path/to/source_folder /path/to/destination_folder
```


This command will organize images from subfolders within "source_folder" into a dataset in the "destination_folder/data" directory. It will also generate a labels CSV file named "labels.csv" in the "destination_folder" directory.

## Sample and Copy

The script `sample_and_copy.py` allows you to sample and copy images from one folder to another.

### Code Overview

The script consists of the following functions:

1. **`move_sample(current_path, dest_path, quantity, jump_files, to_rename=True):`**
    - Samples a specified quantity of images from the `current_path` and moves them to the `dest_path`. It provides an option to rename the sampled images.
  
2. **`get_random_name():`**
    - Generates a random name using UUID for renaming sampled images.

### How to Run the Script

Execute the script by running the following command in the terminal:

```bash
python3 sample_and_copy.py <source_folder_path> <destination_folder_path> <sample_quantity> <to_rename>
```

`<source_folder_path>`: Path to the folder containing images to sample.
`<destination_folder_path>`: Path where the sampled images will be copied.
`<sample_quantity>`: Number of images to sample.
`<to_rename>`: Boolean flag (0 or 1) to indicate whether to rename the sampled files.

### Example execution

```bash
python sample_and_copy.py /path/to/source_folder /path/to/destination_folder 5 1
```

This command will sample 5 images from the "source_folder", rename them, and move them to the "destination_folder".


## Sample and Copy from Subfolders

The script `sample_and_copy_from_subfolders.py` allows you to sample and copy images from subfolders to a destination folder.

### Code Overview

The script consists of the following functions:

1. **`get_all_subfolders_name(path):`**
    - Retrieves the names of all subfolders in the specified `path`.

2. **Main Script:**
    - Accepts command-line arguments to specify the source folder (`<path>`), destination folder (`<new_path>`), sample quantity (`<qtd>`), jump size (`<jump>`), and whether to rename files (`<rename>`).
    - Calls the `move_sample` function from `sample_and_copy.py` to perform the sampling and copying.

### How to Run the Script

Execute the script by running the following command in the terminal:

```bash
python3 sample_and_copy_from_subfolders.py <source_folder_path> <destination_folder_path> <sample_quantity> <jump_size> <rename>
```

`<source_folder_path>`: Path to the folder containing subfolders with images.
`<destination_folder_path>`: Path where the sampled images will be copied.
`<sample_quantity>`: Number of images to sample from each subfolder.
`<jump_size>`: Distance between sampled images in each subfolder.
`<rename>`: Boolean flag (0 or 1) to indicate whether to rename the sampled files.

### Example execution

```bash
python sample_and_copy_from_subfolders.py /path/to/source_folder /path/to/destination_folder 5 2 1
```

This command will sample 5 images from each subfolder, with a jump of 2 between sampled images, and rename the sampled files in the "destination_folder".

## Rename Images

The script `rename_images.py` allows you to rename images in a specified folder.

### Code Overview

The script consists of the following function:

1. **`rename_images(path, basename):`**
    - Renames images in the specified `path` using a provided `basename` and an index.

### How to Run the Script

Execute the script by running the following command in the terminal:

```bash
python3 rename_images.py <folder_path> <new_basename>
```

`<folder_path>`: Path to the folder containing images to be renamed.
`<new_basename>`: New base name for renaming the images.

### Example execution

```bash
python rename_images.py /path/to/image_folder new_name
```

This command will rename all images in the "image_folder" by appending an index to the specified new_name.



