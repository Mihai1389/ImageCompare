# populate_database.py
import os
import sqlite3
from image_processing import extract_features

def populate_database(folder_path):
    conn = sqlite3.connect('images.db')
    c = conn.cursor()

    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(folder_path, filename)
            descriptors = extract_features(image_path)
            c.execute("INSERT INTO images (path, descriptors) VALUES (?, ?)", (image_path, descriptors.tobytes()))
            print(f"Inserted: {filename}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    folder_path = 'path_to_your_image_folder'  # Replace with your image folder path
    populate_database(folder_path)