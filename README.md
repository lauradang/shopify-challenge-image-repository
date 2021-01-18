# Shopify Challenge: Image Repository

## Preview

![](readme_images/ui_preview.png)

## Summary

Thank you for considering my coding challenge submission for the role of Backend Developer at Shopify.

The theme of my image repository are images from the main characters in the Simpsons including Homer, Marge, Bart, and Lisa. 

Feature chosen:
- Search for images of a character via uploading an image of that same character
  - Fine-tuned a convolutional neural network (Resnet) to classify an image with either Homer, Marge, Bart, or Lisa on Kaggle dataset (Please see my [Kaggle notebook](https://github.com/lauradang/simpson-image-repository/blob/main/simpsons-fastai.ipynb) for details)
    - API has a confidence threshold, so the program is able to distinguish if there is no Simpsons character in the photo, thus returning 0 results
  - Receives image via `POST` request from user form
  - Classification/Prediction is used to query the SQLite database and retrieve the images of the predicted characterr

## How to Run

1. Install the necessary dependencies listed in `requirements.txt`. I recommend using a virtual environment manager such as [virtualenv](https://virtualenv.pypa.io/en/latest/) to install the dependencies via `pip install requirements.txt`.

2. Run `flask run`.

3. Open browser and go to link that the flask application is running on. The link should be given in the terminal shortly after running step 2.

4. Try it out! Upload a picture of one of these characters to display the character's images from the repository.
