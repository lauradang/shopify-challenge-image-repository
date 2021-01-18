"""Functions that initialize database with image path names and titles"""
import os
import sqlite3

images_dir = os.path.join("static", "images")
simpsons_characters = os.listdir(images_dir)
db_name = "image_repo.db"


def insert_character_file_paths(character: str):
    """Inserts the file paths for a given character to DB"""
    dir_path = os.path.join(images_dir, character)
    
    for _file in os.listdir(dir_path):
        file_path = os.path.join(character, _file)
        values = (character, file_path)

        with sqlite3.connect(db_name) as conn:
            cur = conn.cursor()
            cur.execute("INSERT OR IGNORE INTO image_repo VALUES(null, ?, ?)", values)
            conn.commit()


def seed_db() -> None:
    """Seed database with Simpsons images and their file paths"""
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS image_repo (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT, 
                file_path TEXT UNIQUE
            )
        """)
        conn.commit()

    for character in simpsons_characters:
        insert_character_file_paths(character)
