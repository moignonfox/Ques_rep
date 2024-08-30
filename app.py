from flask import Flask, render_template, request, redirect, url_for
import os
import re
import chardet
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
CLEANED_FOLDER = 'cleaned/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CLEANED_FOLDER'] = CLEANED_FOLDER

# Télécharger les ressources nécessaires pour le traitement du texte
nltk.download('stopwords')
nltk.download('wordnet')

# Initialiser les outils de nettoyage
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('french'))  # Utiliser 'english' pour l'anglais


# Fonction de nettoyage du texte
def clean_text(text):
    # Conversion en minuscules
    text = text.lower()

    # Suppression des caractères spéciaux et ponctuation
    text = re.sub(r'\W', ' ', text)

    # Suppression des stop words
    words = text.split()
    words = [word for word in words if word not in stop_words]

    # Lemmatisation
    words = [lemmatizer.lemmatize(word) for word in words]

    # Reconstruire le texte nettoyé
    cleaned_text = ' '.join(words)
    return cleaned_text


# Nettoyer le fichier téléchargé
def detect_encoding(filepath):
    with open(filepath, 'rb') as file:
        result = chardet.detect(file.read())
        return result['encoding']

def clean_uploaded_file(filepath, cleaned_filepath):
    encoding = detect_encoding(filepath)
    with open(filepath, 'r', encoding=encoding, errors='ignore') as file:
        text = file.read()

    cleaned_text = clean_text(text)
    with open(cleaned_filepath, 'w', encoding='utf-8') as cleaned_file:
        cleaned_file.write(cleaned_text)

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
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            cleaned_filepath = os.path.join(app.config['CLEANED_FOLDER'], 'cleaned_' + file.filename)

            # Enregistrer le fichier téléchargé
            file.save(filepath)

            # Nettoyer le fichier
            clean_uploaded_file(filepath, cleaned_filepath)

            return f'Fichier téléchargé et nettoyé : {file.filename}'


if __name__ == '__main__':
    app.run(debug=True)
