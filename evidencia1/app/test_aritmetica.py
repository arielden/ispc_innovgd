import aritmetica

def test_suma():
    assert aritmetica.sumar(10.5, 5.3) == 15.8, "Error en suma de números positivos"
    assert aritmetica.sumar(-1.2, 1.2) == 0.0, "Error en suma de al menos un negativo"
    assert aritmetica.sumar(0, 0) == 0.0, "Error en suma de nulos"

def test_resta():
    assert aritmetica.restar(10.5, 5.3) == 5.2, "Error en resta de positivos"
    assert aritmetica.restar(-1.2, 1.2) == -2.4, "Error en resta de al menos un negativo"
    assert aritmetica.restar(0, 0) == 0.0, "Error en resta de nulos"

def test_division():
    assert aritmetica.dividir(10, 2) == 5.0, "Error en división"
    assert aritmetica.dividir(9, 3) == 3.0, "Error en división, segundo caso"
    assert aritmetica.dividir(5, 0) is None, "Error al dividir por cero: No está manejando la división por cero"

def test_multiplicacion():
    assert aritmetica.multiplicar(10, 5) == 50.0, "Error en multiplicación de positivos"
    assert aritmetica.multiplicar(-1.2, 1.5) == -1.8, "Error en multiplicación entre negativo y positivo"
    assert aritmetica.multiplicar(-2.0, -2.0) == 4.0, "Error en multiplicación entre negativo y negativo"
    assert aritmetica.multiplicar(0, 10) == 0.0, "Error en multiplicacion por cero"

def test_suma_n_numeros():
    assert aritmetica.sumar_n(1.2, 2.3, 3.4) == 6.9, "Error en suma de positivos"
    assert aritmetica.sumar_n(0, 0, 0) == 0.0, "Error en suma de ceros"
    assert aritmetica.sumar_n(-1, 1, 2) == 2.0, "Error en suma que contiene al menos un negativo"

def test_promedio_n_numeros():
    assert aritmetica.promedio_n(1.2, 2.3, 3.4) == 2.3, "Error en promedio de positivos"
    assert aritmetica.promedio_n(0, 0, 0) == 0.0, "Error en promedio de ceros"
    assert aritmetica.promedio_n(-1, 1, 2) == 0.67, "Error en promedio de al menos un negativo"

if __name__ == "__main__":
    test_suma()
    test_resta()
    test_division()
    test_multiplicacion()
    test_suma_n_numeros()
    test_promedio_n_numeros()
    print("Todos los test pasaron exitosamente!")
