from sklearn.metrics import classification_report, accuracy_score

def evaluar_modelo(modelo, X_test, y_test):
    y_pred = modelo.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
