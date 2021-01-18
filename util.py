"""A general utility file with standard utility functions"""
import os
import sqlite3
from fastai.vision.all import load_learner
from init_db import db_name

CONFIDENCE_THRESHOLD = 0.65
image_classifier = load_learner("image_classifier.pkl")


def get_character_prediction(image_path: str) -> str:
    """Gets the image classifier result from the model's output"""
    prediction = image_classifier.predict(image_path)
    class_idx = prediction[1].item()
    confidence_score = prediction[2][class_idx].item()

    if confidence_score < CONFIDENCE_THRESHOLD:
        return None
    
    return prediction[0].split("_")[0]


def get_repository_images(character: str, image_folder: str) -> list:
    """Gets the character's images from the repository"""
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT file_path 
            FROM image_repo 
            WHERE name = ?
        """, (character,))
    
    image_paths = cur.fetchall()
    full_image_paths = []

    for image_path in image_paths:
        full_image_path = os.path.join(image_folder, image_path[0])
        full_image_paths.append(full_image_path)
    
    return full_image_paths
