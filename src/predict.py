def predecir(modelo, vectorizer, nuevos_textos):
    nuevos_vectores = vectorizer.transform(nuevos_textos)
    return modelo.predict(nuevos_vectores)
