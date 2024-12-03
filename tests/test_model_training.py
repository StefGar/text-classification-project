import pytest
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

def test_entrenar_modelo():
    # Datos simulados
    textos = ["hola mundo", "aprendiendo python", "hola python"]
    etiquetas = ["saludo", "programación", "saludo"]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(textos)
    
    modelo = MultinomialNB()
    modelo.fit(X, etiquetas)
    
    prediccion = modelo.predict(vectorizer.transform(["hola"]))
    assert prediccion[0] == "saludo", "El modelo debe clasificar correctamente"
