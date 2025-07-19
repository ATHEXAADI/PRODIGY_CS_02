# Develop a single image encryption tool using pixel manipulation. you can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt image. 

from tkinter import Tk, filedialog, Button, Label
from PIL import Image
import os

# Encryption/Decryption key
KEY = 123

def encrypt_decrypt_image(filepath, mode):
    # Open the image
    img = Image.open(filepath)
    img = img.convert('RGB')
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # XOR each pixel with the key
            r_new = r ^ KEY
            g_new = g ^ KEY
            b_new = b ^ KEY

            pixels[i, j] = (r_new, g_new, b_new)

    # Save the new image
    file_base, file_ext = os.path.splitext(filepath)
    if mode == "encrypt":
        new_path = f"{file_base}_encrypted{file_ext}"
    else:
        new_path = f"{file_base}_decrypted{file_ext}"
    
    img.save(new_path)
    return new_path

def open_file(mode):
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if filepath:
        result_path = encrypt_decrypt_image(filepath, mode)
        status_label.config(text=f"{mode.title()}ed Image Saved:\n{result_path}")

# GUI
root = Tk()
root.title("Image Encryptor/Decryptor")
root.geometry("400x200")

Label(root, text="Image Encryption Tool", font=("Arial", 16)).pack(pady=10)

Button(root, text="Encrypt Image", command=lambda: open_file("encrypt"), width=20).pack(pady=5)
Button(root, text="Decrypt Image", command=lambda: open_file("decrypt"), width=20).pack(pady=5)

status_label = Label(root, text="", wraplength=380, fg="green")
status_label.pack(pady=10)

root.mainloop()
