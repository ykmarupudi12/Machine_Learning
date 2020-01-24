import os
import sys
from PIL import Image, ImageFilter

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.mkdirs(directory)

for image in os.listdir(path):
    clean_name = os.path.split()
    img = Image.open(f'{path},{filename}')
    img.save(f'{directory}/{clean_name}.png', 'png')
    print('alldone')