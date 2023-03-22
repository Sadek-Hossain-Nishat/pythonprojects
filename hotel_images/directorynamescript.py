import os
from tkinter import PhotoImage

base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'user.png')
print(image_path)
photo = PhotoImage(file=image_path)