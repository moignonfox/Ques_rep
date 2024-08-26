import re


import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
#nltk.download('all')


lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('french'))

def clean_text(text):

    text =text.lower()

    text = re.sub(r'\W', ' ', text)


    words = text.split()
    words = [word for word in words if word not in stop_words]

    words = [lemmatizer.lemmatize(word) for word in words]

    cleaned_text = ' '.join(words)
    return cleaned_text

def clean_text_file(input_path, output_path):
    with open(input_path, 'r', encoding = 'utf-8') as file:
        text = file.read()
        cleaned_text = clean_text(text)
        with open (output_path, 'w', encoding='utf8') as output_file:
            output_file.write(cleaned_text)


clean_text_file(r'C:\Users\moign\Ques_rep\File_converted\Le probleme a trois corps - Liu Cixin.txt', r'C:\Users\moign\Ques_rep\Clean_text\Le probleme a trois corps - Liu Cixin.txt' )