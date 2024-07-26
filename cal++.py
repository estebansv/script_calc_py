def sumar(a, b):
    """Función que retorna la suma de dos números"""
    return a + b

def restar(a, b):
    """Función que retorna la resta de dos números"""
    return a - b
    
def mul(a, b):
    """Función que retorna la Multip. de dos números"""
    return a * b

def div(a, b):
    """Función que retorna la División de dos números"""
    return a / b


def mod(a, b):
    """Función que retorna el modulo de dos números"""
    return a % b

def expo(a, b):
    """Función que retorna lel exponente de dos números"""
    return a ** b

def ejecutar():
    """Función principal que utiliza match-case"""
    #numero de v = vueltas

    v=0 
    while v < 1:
        v+=1
        print("\n\tOpciones:")
        print("1. Sumar dos números")
        print("2. Restar dos números")
        print("3. Multiplicación de dos números")
        print("4. División de dos números")
        print("5. Modulo de dos números")
        print("6. Exponente de dos números")
        print("7. Ejecutar las 6 operaciones en bucle infinito")
        print("8. Salir❌\n")

        try:
            # Captura la opción elegida por el usuario
            opcion = int(input("Elige una opción: "))

            # Verifica si el usuario quiere salir
            if opcion == 8:
                print("Saliendo del programa...\n👋 👋")
                break
            
            # Solicita números al usuario solo si la opción es 1 o 2
            if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5 or opcion == 6:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))

            # Utiliza match-case para ejecutar las operaciones
            match opcion:
                case 1:
                    resultado = sumar(a, b)
                    print(f"La suma de {a} y {b} es {round(resultado,2)}.\n")
                
                case 2:
                    resultado = restar(a, b)
                    print(f"La resta de {a} y {b} es {resultado}.\n")

                case 3:
                    resultado = mul(a, b)
                    print(f"La Multiplicacion de {a} y {b} es {resultado}.\n")

                case 4:
                    resultado = div(a, b)
                    print(f"La divicion de {a} y {b} es {resultado}.\n")

                case 5:
                    resultado = mod(a, b)
                    print(f"El modulo de {a} y {b} es {resultado}.\n")

                case 6:
                    resultado = expo(a, b)
                    print(f"El exponente de {a} y {b} es {resultado}.\n")

                case 7:
                    # Bucle infinito ejecutando suma y resta
                    print("Ejecutando todas las opciones en bucle infinito (Presiona Ctrl+C para salir):\n")
                    
                    while True:
                        print("Operacion sumar")
                        a = float(input("Ingresa el primer número: "))
                        b = float(input("Ingresa el segundo número: "))
                        suma = sumar(a, b)
                        print(f"La suma de {a} y {b} es {suma}.\n")

                        print("Operacion restar")
                        a = float(input("Ingresa el primer número: "))
                        b = float(input("Ingresa el segundo número: "))
                        resta = restar(a, b)
                        print(f"La resta de {a} y {b} es {resta}.\n")

                        print("Operacion Multiplicar")
                        a = float(input("Ingresa el primer número: "))
                        b = float(input("Ingresa el segundo número: "))
                        mt = mul(a, b)
                        print(f"La resta de {a} y {b} es {mt}.\n")

                        print("Operacion Dividir")
                        a = float(input("Ingresa el primer número: "))
                        b = float(input("Ingresa el segundo número: "))
                        dv = div(a, b)
                        print(f"La resta de {a} y {b} es {dv}.\n")

                        print("Operacion Modulo")
                        a = float(input("Ingresa el primer número: "))
                        b = float(input("Ingresa el segundo número: "))
                        md = mod(a, b)
                        print(f"La resta de {a} y {b} es {md}.\n")

                        print("Operacion Exponente")
                        a = float(input("Ingresa el primer número: "))
                        b = float(input("Ingresa el segundo número: "))
                        xp = expo(a, b)
                        print(f"La resta de {a} y {b} es {xp}. rep👀🔥\n")
                        print("Ejecutando todas las opciones en bucle infinito (Presiona Ctrl+C para salir):\n")
                
                case _:
                    print("Opción no válida, intenta de nuevo.")
        
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    ejecutar()
