# 1)_  Definir un programa que calcule el perímetro del rectángulo siendo x el lado más corto
print('Parte 1')
def perimetro_rectangulo(lado: int):
    # Pre: recibe un variable que se corresponde al lado más corto del rectángulo
    # Post: primero multiplicada (2 * lado) para formar el lado más largo del rectangulo y devuelve el perímetro 
    perimetro = 6 * lado 
    print('El perimetro de un rectángulo de base', lado, 'y lado ', 2*lado, 'es: ', perimetro)

perimetro_rectangulo(1)
perimetro_rectangulo(2)
perimetro_rectangulo(3)

print('')
print('Parte2')

# 2)_ Definir un programa que calcule la superficie del rectángulo siendo x la longitud del lado más corto.

def superficie_rectangulo(h: int):
    # Pre: Recibe un entero que se coresponde al lado más corto del rectángulo 
    # Pots: Devuelve la superficie de un rectángulo 
    superficie = h * h * 2 
    print('La superficie de un rectángulo de base', h, 'y lado ', 2*h, 'es: ', superficie)

superficie_rectangulo(1)
superficie_rectangulo(2)
superficie_rectangulo(3)