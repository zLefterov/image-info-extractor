from PIL import Image

img = Image.open('./image1.jpeg')

print(img.mode)
print(img.format)
print(img.size)
