 
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'Aucun fichier sélectionné'
        file = request.files['file']
        if file.filename == '':
            return 'Aucun fichier sélectionné'
        if file:
            filepath = os.path.join('uploads', file.filename)
            file.save(filepath)
            return f'Fichier téléchargé : {file.filename}'

if __name__ == '__main__':
    app.run(debug=True)
