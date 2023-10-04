from flask import Flask, render_template,  send_from_directory
import os
import glob
app = Flask(__name__)

# Define the folder where your images are stored
# IMAGE_FOLDER = os.path.join('static', 'images')
ROOT_IMAGE_FOLDER = '/Volumes/NAS-Disk-1/'
IMAGE_FOLDER = '/Volumes/NAS-Disk-1/**/*.jpg'

@app.route('/')
def index():
    # Get a list of image files in the folder
    # image_files = [ f for f in os.listdir(IMAGE_FOLDER)]
    image_files = [ f for f in glob.glob(IMAGE_FOLDER)]

    # Render the HTML template with the list of image files
    return render_template('index.html', image_files=image_files)



@app.route('/<path:image_path>')
def serve_image(image_path):
    # Serve an individual image file based on the image_path (filename or subfolder/filename)
    image_file = os.path.join(ROOT_IMAGE_FOLDER, image_path)
    
    if os.path.exists(image_file):
        return send_from_directory(ROOT_IMAGE_FOLDER, image_path)
    else:
        return "Image not found", 404



if __name__ == '__main__':
    app.run(debug=True)
