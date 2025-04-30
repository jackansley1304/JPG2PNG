import os
from tkinter import Tk, Button, filedialog, messagebox
from PIL import Image

def convert_images(file_paths):
    for file_path in file_paths:
        try:
            img = Image.open(file_path)

            ext = os.path.splitext(file_path)[1].lower()
            if ext in ['.jpg', '.jpeg']:
                # Convert JPG to PNG
                img = img.convert("RGB")  # Ensure no palette mode
                new_path = os.path.splitext(file_path)[0] + '.png'
                img.save(new_path, 'PNG', optimize=True)
                print(f"Converted to PNG: {new_path}")

            elif ext == '.png':
                # Convert PNG to JPG
                img = img.convert("RGB")  # JPG does not support alpha
                new_path = os.path.splitext(file_path)[0] + '.jpg'
                img.save(new_path, 'JPEG', quality=95, optimize=True)
                print(f"Converted to JPG: {new_path}")

            else:
                print(f"Unsupported format: {file_path}")

        except Exception as e:
            print(f"Failed to convert {file_path}: {e}")

def browse_and_convert():
    file_paths = filedialog.askopenfilenames(
        title="Select JPG or PNG files",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )
    if file_paths:
        convert_images(file_paths)
        messagebox.showinfo("Done", "Conversion complete!")

# GUI setup
root = Tk()
root.title("JPG ↔ PNG Converter")
root.geometry("300x120")

Button(root, text="Select Images to Convert", command=browse_and_convert, padx=10, pady=10).pack(pady=30)

root.mainloop()

