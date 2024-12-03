import pytest
from src.feature_extraction import vectorizar_textos

def test_vectorizar_textos():
    textos = ["hola mundo", "aprendiendo python"]
    X, vectorizer = vectorizar_textos(textos)
    assert X.shape[0] == 2, "Debe haber una fila por texto"
    assert len(vectorizer.get_feature_names_out()) > 0, "El vectorizador debe generar características"
