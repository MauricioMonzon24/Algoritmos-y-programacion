#Definir un programa que devuelva la superficie de un rectángulo de lados de longitud 3 y 2.

def superficieRectangulo(base: int, altura: int):
    # Pre: toma dos variables, base  y otra para la altura 
    # Post: Devuelve el resultado del area de un rectangulo: (base * altura)
    resultado = (base * altura)
    print(resultado)

superficieRectangulo(2, 3)