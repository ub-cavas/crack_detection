# import os
# import cv2

# data_root = 'datasets/CrackLS315'
# image_dir = os.path.join(data_root, 'images')

# images_files = [os.path.splitext(f)[0] for f in os.listdir(image_dir) if f.endswith('.jpg')]

# with open(os.path.join(data_root, 'train.txt'), 'w') as f:
#     for image_file in images_files:
#         f.write(f"{image_file}\n")

# print("train.txt created successfully")

# # def create_mask(img_dir, mask_dir, threshold = 100):
# #     img = cv2.imread(img_dir, cv2.IMREAD_GRAYSCALE)
# #     edges = cv2.Canny(img, threshold1=threshold, threshold2=threshold*2)
# #     _, mask = cv2.threshold(edges, 127, 255, cv2.THRESH_BINARY)
# #     cv2.imwrite(mask_dir, mask)

# # img_dir = 'datasets/CrackLS315/images'
# # mask_dir = 'datasets/CrackLS315/masks'

# # for image_file in os.listdir(img_dir):
# #     if image_file.endswith('.jpg'):
# #         image_path = os.path.join(img_dir, image_file)
# #         mask_path = os.path.join(mask_dir, os.path.splitext(image_file)[0] + '.png')
# #         create_mask(image_path, mask_path)

# # print("Masks generated successfully!")

# import os
# import random
# from glob import glob

# # Set the dataset directories
# image_dir = 'datasets/CrackLS315/images'
# mask_dir = 'datasets/CrackLS315/masks'

# # Get all image and mask files
# image_files = glob(os.path.join(image_dir, '*.jpg'))
# mask_files = glob(os.path.join(mask_dir, '*.png'))

# # Check if image and mask files match
# assert len(image_files) == len(mask_files), "The number of images and masks should be equal."

# # Get the base filenames without extensions for both images and masks
# image_basenames = [os.path.basename(image).replace('.jpg', '') for image in image_files]
# mask_basenames = [os.path.basename(mask).replace('.png', '') for mask in mask_files]

# # Ensure all mask files have a corresponding image file
# assert sorted(image_basenames) == sorted(mask_basenames), "Image and mask filenames do not match."

# # Shuffle the data
# combined = list(zip(image_files, mask_files))
# random.shuffle(combined)
# image_files, mask_files = zip(*combined)

# # Split into training and validation sets (80% train, 20% val)
# train_size = int(0.8 * len(image_files))
# train_images = image_files[:train_size]
# val_images = image_files[train_size:]

# # Create 'train.txt' and 'val.txt'
# with open('train.txt', 'w') as train_file:
#     for image in train_images:
#         train_file.write(f"{image}\n")

# with open('val.txt', 'w') as val_file:
#     for image in val_images:
#         val_file.write(f"{image}\n")

# print("train.txt and val.txt files created successfully.")

import torch

torch.cuda.empty_cache()

import gc
# del variables
gc.collect()

