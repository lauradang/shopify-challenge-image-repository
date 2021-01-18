"""Image repository search endpoints"""
import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from init_db import seed_db
from util import get_character_prediction, get_repository_images

seed_db()
HOMEPAGE = "index.html"

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_FOLDER = "static"
IMAGE_FOLDER = os.path.join(STATIC_FOLDER, "images")
STYLE_FOLDER = os.path.join(STATIC_FOLDER, "style")

app.config["UPLOAD_FOLDER"] = IMAGE_FOLDER
app.config["STYLE_FOLDER"] = STYLE_FOLDER


@app.route("/")
def home():
    """Home endpoint"""
    return render_template(HOMEPAGE)


@app.route("/upload", methods=["POST"])
def upload_file():
    """Search for similar images via image upload"""
    uploaded_file = request.files["file"]

    if uploaded_file.filename != "":
        uploaded_file.save(uploaded_file.filename)
        character_prediction = get_character_prediction(uploaded_file.filename)
        os.remove(uploaded_file.filename)
        image_paths = get_repository_images(character_prediction, app.config["UPLOAD_FOLDER"])

        return render_template(HOMEPAGE, image_paths=image_paths)
    
    return redirect(url_for("home"))
