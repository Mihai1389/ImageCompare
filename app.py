# app.py
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from image_processing import store_image, compare_with_database

class ImageComparerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Comparer")

        self.label = tk.Label(master, text="Upload an image to compare:")
        self.label.pack()

        self.upload_button = tk.Button(master, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            # Copy the uploaded image to a folder for storing images
            image_filename = os.path.basename(file_path)
            stored_image_path = os.path.join('stored_images', image_filename)
            os.makedirs('stored_images', exist_ok=True)
            store_image(file_path, stored_image_path)

            image = Image.open(file_path)
            image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(image)

            self.image_label = tk.Label(image=photo)
            self.image_label.image = photo
            self.image_label.pack()

            similarity_score = self.compare_with_database(stored_image_path)
            if similarity_score > 0:
                self.result_label.config(text=f"Similarity Score: {similarity_score}")
            else:
                self.result_label.config(text="No similar images found.")

    def compare_with_database(self, stored_image_path):
        similarity_score = compare_with_database(stored_image_path)
        return similarity_score

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageComparerApp(root)
    root.mainloop()
