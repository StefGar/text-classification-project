from sklearn.feature_extraction.text import TfidfVectorizer

def vectorizar_textos(textos, max_features=5000):
    vectorizer = TfidfVectorizer(max_features=max_features)
    X = vectorizer.fit_transform(textos)
    return X, vectorizer
