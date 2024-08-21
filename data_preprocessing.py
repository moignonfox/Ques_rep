import nltk
from nltk.corpus import stopwords
from nltk. tokenize import  word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

def remove_stopwords(text):
    stop_words = set(stopwords.words('french'))
    words = word_tokenize(text)
    filtered_text = [word for word in words if word.lower() not in stop_words]
    return ' '.join (filtered_text)

text = "ceci est un exemple de texte avec des mots non pertinents comme et  ou, mais."
clean_text = remove_stopwords(text)
print(clean_ text)