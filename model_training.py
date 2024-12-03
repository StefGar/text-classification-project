from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

def entrenar_modelo(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = MultinomialNB()
    modelo.fit(X_train, y_train)
    return modelo
