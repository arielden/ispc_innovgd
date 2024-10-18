# aritmetica.py

def sumar(a: float, b: float) -> float:
    """
    Suma de dos números reales (float)
    Devuelve la suma entre dos números ingresados
    """
    return round(a + b, 2)

def restar(a: float, b: float) -> float:
    """
    Resta de dos números reales (float)
    Devuelve la resta del primer número menos el segundo
    """
    return round(a - b, 2)

def dividir(a: float, b: float) -> float:
    """
    División de dos números reales (float)
    Devuelve la división del primer número sobre el segundo
    """
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        return None
    return round(resultado, 2)

def multiplicar(a: float, b: float) -> float:
    """
    Multiplicación de dos números reales (float)
    Devuelve el producto de dos números reales
    """
    return round(a * b, 2)

def sumar_n(*args: float) -> float:
    """
    Suma de n números reales (float)
    Puede recibir cualquier cantidad de números, devuelve la suma de todos.
    """
    if not args:
        raise ValueError("Ingresar al menos un número.")
    return round(sum(args), 2)

def promedio_n(*args: float) -> float:
    """
    Promedio de n número reales (float)
    Puede recibir una cantidad variable de números.
    Devuelve el promedio de los mismos.
    """
    if not args:
        raise ValueError("Ingresar al menos un número.")
    return round(sum(args) / len(args), 2)
