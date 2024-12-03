import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def limpiar_texto(texto):
    texto = re.sub(r'http\S+', '', texto)
    texto = re.sub(r'@\w+', '', texto)
    texto = re.sub(r'[^\w\s]', '', texto)
    texto = texto.lower()
    palabras = word_tokenize(texto)
    palabras = [lemmatizer.lemmatize(p) for p in palabras if p not in stop_words]
    return ' '.join(palabras)
