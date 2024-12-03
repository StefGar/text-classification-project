import pandas as pd
from src.data_preprocessing import limpiar_texto
from src.feature_extraction import vectorizar_textos
from src.model_training import entrenar_modelo
from src.evaluation import evaluar_modelo
from src.predict import predecir

def flujo_principal():
    # 1. Cargar datos
    datos = pd.read_csv("data/raw/tweets.csv")
    datos['texto_limpio'] = datos['texto'].apply(limpiar_texto)

    # 2. Vectorizar datos
    X, vectorizer = vectorizar_textos(datos['texto_limpio'])
    y = datos['tema']

    # 3. Entrenar modelo
    modelo = entrenar_modelo(X, y)

    # 4. Evaluar modelo
    evaluar_modelo(modelo, X, y)

if __name__ == "__main__":
    flujo_principal()
