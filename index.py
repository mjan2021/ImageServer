from flask import Flask, render_template,  send_from_directory
import os

app = Flask(__name__)

# Define the folder where your images are stored
IMAGE_FOLDER = os.path.join('static', 'images')
# IMAGE_FOLDER = 'I:\Downloads\Pictures\Rome'

@app.route('/')
def index():
    # Get a list of image files in the folder
    image_files = [ f for f in os.listdir(IMAGE_FOLDER)]

    # Render the HTML template with the list of image files
    return render_template('index.html', image_files=image_files)


@app.route('/<image_id>')
def serve_image(image_id):
    # Serve an individual image file based on the image_id (filename)
    filename = f"{image_id}.jpg" or f'{image_id}.png'  # Assuming the filename corresponds to the image_id
    return send_from_directory(IMAGE_FOLDER, filename)


if __name__ == '__main__':
    app.run(debug=True)
