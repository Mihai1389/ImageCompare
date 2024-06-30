# database_setup.py
# import sqlite3

# def create_database():
#     conn = sqlite3.connect('images.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS images (
#                  id INTEGER PRIMARY KEY,
#                  path TEXT,
#                  descriptors BLOB)''')
#     conn.commit()
#     conn.close()

# if __name__ == "__main__":
#     create_database()


# database_setup.py
# import sqlite3
# import os

# def create_database():
#     conn = sqlite3.connect('images.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS images (
#                  id INTEGER PRIMARY KEY,
#                  path TEXT,
#                  descriptors BLOB)''')
#     conn.commit()
#     conn.close()

# def insert_images():
#     conn = sqlite3.connect('images.db')
#     c = conn.cursor()

#     # List of image paths to insert into the database
#     image_path = r'c:\Users\user\Downloads\database\image (1).png'


#     for path in image_paths:
#         # Check if image already exists in database
#         c.execute("SELECT id FROM images WHERE path=?", (path,))
#         result = c.fetchone()
#         if result:
#             print(f"Image '{path}' already exists in the database.")
#         else:
#             # Insert image path into the database
#             c.execute("INSERT INTO images (path) VALUES (?)", (path,))
#             print(f"Inserted image: {path}")

#     conn.commit()
#     conn.close()

# if __name__ == "__main__":
#     create_database()
#     insert_images()

# database_setup.py
import sqlite3

def create_database():
    conn = sqlite3.connect('images.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS images (
                 id INTEGER PRIMARY KEY,
                 path TEXT,
                 descriptors BLOB)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
