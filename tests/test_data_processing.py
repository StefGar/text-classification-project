import pytest
from src.data_preprocessing import limpiar_texto

def test_limpiar_texto():
    texto_entrada = "Hola @usuario, visita http://example.com 😊 #hashtag"
    texto_limpio = limpiar_texto(texto_entrada)
    esperado = "hola visita hashtag"  # Resultado esperado
    assert texto_limpio == esperado, f"Se esperaba '{esperado}', pero se obtuvo '{texto_limpio}'"
