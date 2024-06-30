# app.py
# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk
# from image_processing import compare_with_database

# class ImageComparerApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Image Comparer")
        
#         self.label = tk.Label(master, text="Upload an image to compare:")
#         self.label.pack()
        
#         self.upload_button = tk.Button(master, text="Upload Image", command=self.upload_image)
#         self.upload_button.pack()
        
#         self.result_label = tk.Label(master, text="")
#         self.result_label.pack()
    
#     def upload_image(self):
#         file_path = filedialog.askopenfilename()
#         if file_path:
#             image = Image.open(file_path)
#             image.thumbnail((300, 300))
#             photo = ImageTk.PhotoImage(image)
            
#             self.image_label = tk.Label(image=photo)
#             self.image_label.image = photo
#             self.image_label.pack()
            
#             similarity_score = compare_with_database(file_path)
#             self.result_label.config(text=f"Similarity Score: {similarity_score}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ImageComparerApp(root)
#     root.mainloop()

# app.py
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import sqlite3
from image_processing import extract_features, compare_images

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
            image = Image.open(file_path)
            image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(image)

            self.image_label = tk.Label(image=photo)
            self.image_label.image = photo
            self.image_label.pack()

            similarity_score = self.compare_with_database(file_path)
            if similarity_score > 0:
                self.result_label.config(text=f"Similarity Score: {similarity_score}")
            else:
                self.result_label.config(text="No similar images found.")

    def compare_with_database(self, image_path):
        conn = sqlite3.connect('images.db')
        c = conn.cursor()
        c.execute("SELECT path, descriptors FROM images")
        rows = c.fetchall()
        conn.close()

        best_score = 0
        best_image_path = None
        query_descriptors = extract_features(image_path)
        for row in rows:
            stored_image_path, stored_descriptors = row
            stored_descriptors = np.frombuffer(stored_descriptors, dtype=np.uint8).reshape(-1, 32)
            score = compare_images(query_descriptors, stored_descriptors)
            if score > best_score:
                best_score = score
                best_image_path = stored_image_path
        
        # Return best match image path or score
        return best_score

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageComparerApp(root)
    root.mainloop()
