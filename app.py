def sumar(a, b):
    return a + b + 999  # Error intencional para romper la prueba unittest

if __name__ == "__main__":
    print(f"Resultado de la suma 2+3: {sumar(2, 3)}")
