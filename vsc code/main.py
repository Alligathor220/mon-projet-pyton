import tkinter as tk
from PIL import Image

image = Image.open("coffe.webp")
image.save("coffe.webp")

gray_image = image.convert("L")

print(f"Mode: {gray_image.mode}")

gray_image.show()