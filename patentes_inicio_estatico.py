import time

def main():
    print("=" * 50)
    print("GENERADOR DE PATENTES".center(50))
    print("=" * 50)
    print("Este programa calcula la N-ésima patente a partir de AAA000.")
    print("La primera patente (AAA000) corresponde al número 0.\n")

    # Pedimos el número al usuario
    numero = int(input("Ingrese el número de patente a calcular: "))

    # Inicializamos variables
    patente = ""
    contador = 0   # AAA000 será el número 1
    inicio = time.time()  # Tiempo inicial

    TOTAL_PATENTES = 26**3 * 10**3
    if numero >= TOTAL_PATENTES:
        print(f"El número es demasiado grande. El máximo posible es {TOTAL_PATENTES - 1}.")
        return


    # Búsqueda de la patente con bucles anidados
    for i in range(26):
        for j in range(26):
            for k in range(26):
                for l in range(10):
                    for m in range(10):
                        for n in range(10):
                            contador += 1
                            patente = chr(65 + i) + chr(65 + j) + chr(65 + k) + str(l) + str(m) + str(n)
                            if contador == numero + 1:
                                print("\nRESULTADO".center(50, "-"))
                                print(f"Número solicitado: {numero}")
                                print(f"Patente encontrada: {patente}")
                                print(f"Valores finales de los índices:")
                                print(f"  i = {i}  -> {chr(65+i)} (1ª letra)")
                                print(f"  j = {j}  -> {chr(65+j)} (2ª letra)")
                                print(f"  k = {k}  -> {chr(65+k)} (3ª letra)")
                                print(f"  l = {l} (1er número)")
                                print(f"  m = {m} (2º número)")
                                print(f"  n = {n} (3er número)")
                                fin = time.time()
                                print(f"\nTiempo de ejecución: {fin - inicio:.4f} segundos")
                                return  # Finalizamos el programa

if __name__ == "__main__":
    main()
