# image_processing.py
# import cv2
# import numpy as np
# import sqlite3

# def extract_features(image_path):
#     image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#     orb = cv2.ORB_create()
#     keypoints, descriptors = orb.detectAndCompute(image, None)
#     return keypoints, descriptors

# def store_image(image_path):
#     keypoints, descriptors = extract_features(image_path)
#     conn = sqlite3.connect('images.db')
#     c = conn.cursor()
#     c.execute("INSERT INTO images (path, descriptors) VALUES (?, ?)", (image_path, descriptors.tobytes()))
#     conn.commit()
#     conn.close()

# def compare_images(descriptors1, descriptors2):
#     bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#     matches = bf.match(descriptors1, descriptors2)
#     matches = sorted(matches, key=lambda x: x.distance)
#     return len(matches)

# def compare_with_database(image_path):
#     conn = sqlite3.connect('images.db')
#     c = conn.cursor()
#     c.execute("SELECT path, descriptors FROM images")
#     rows = c.fetchall()
#     conn.close()

#     best_score = 0
#     for row in rows:
#         stored_image_path, stored_descriptors = row
#         stored_descriptors = np.frombuffer(stored_descriptors, dtype=np.uint8).reshape(-1, 32)
#         _, descriptors = extract_features(image_path)
#         score = compare_images(descriptors, stored_descriptors)
#         if score > best_score:
#             best_score = score
#     return best_score

# image_processing.py
# image_processing.py

import cv2
import numpy as np
import sqlite3

def extract_features(image_path):
    """
    Extracts features (descriptors) from an image using ORB.
    
    Parameters:
    - image_path (str): Path to the image file.
    
    Returns:
    - descriptors: Descriptors (feature vectors) corresponding to the keypoints.
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(image, None)
    return descriptors

def compare_images(descriptors1, descriptors2):
    """
    Compares two sets of descriptors using a feature matching algorithm (Brute Force).
    
    Parameters:
    - descriptors1: Descriptors of the first image.
    - descriptors2: Descriptors of the second image.
    
    Returns:
    - score (int): Number of matches found between the descriptors.
    """
    if descriptors1 is None or descriptors2 is None:
        return 0
    
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)
    matches = sorted(matches, key=lambda x: x.distance)
    return len(matches)

def store_image(image_path, stored_image_path):
    """
    Copies the image file to a specified directory for storing images and stores its descriptors in the database.
    
    Parameters:
    - image_path (str): Path to the original image file.
    - stored_image_path (str): Path where the image file will be copied for storage.
    """
    descriptors = extract_features(image_path)
    conn = sqlite3.connect('images.db')
    c = conn.cursor()
    c.execute("INSERT INTO images (path, descriptors) VALUES (?, ?)", (stored_image_path, descriptors.tobytes()))
    conn.commit()
    conn.close()

def compare_with_database(stored_image_path):
    """
    Compares a stored image with images stored in the database based on feature matching.
    
    Parameters:
    - stored_image_path (str): Path to the stored image file to compare.
    
    Returns:
    - best_score (int): Best similarity score (number of matches) found with any image in the database.
    """
    conn = sqlite3.connect('images.db')
    c = conn.cursor()
    c.execute("SELECT path, descriptors FROM images")
    rows = c.fetchall()
    conn.close()

    best_score = 0
    query_descriptors = extract_features(stored_image_path)
    for row in rows:
        stored_image_path, stored_descriptors = row
        stored_descriptors = np.frombuffer(stored_descriptors, dtype=np.uint8).reshape(-1, 32)
        score = compare_images(query_descriptors, stored_descriptors)
        if score > best_score:
            best_score = score
    
    return best_score

