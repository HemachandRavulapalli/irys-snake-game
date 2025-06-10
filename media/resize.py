from PIL import Image
import os

folder = '.'  # Use current folder instead of 'media'
size = (20, 20)

for file in os.listdir(folder):
    if file.endswith('.gif'):
        filepath = os.path.join(folder, file)
        img = Image.open(filepath)
        img = img.resize(size)
        img.save(filepath)
