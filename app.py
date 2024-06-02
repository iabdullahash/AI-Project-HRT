from flask import Flask, render_template, request, redirect, url_for, send_file
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # 32MB limit



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
     if 'photo' in request.files:
        photo = request.files['photo']
        photo.save('uploads/' + photo.filename)
        return 'Photo uploaded successfully'
     return 'No file uploaded'





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
