# Explicación detallada del Generador de Patentes

Este documento explica paso a paso cómo funciona el programa que genera la **N-ésima patente** en formato `AAA000` a partir de bucles anidados.

---

## 1. Importación de librerías
Se importa la librería estándar `time`:

```python
import time
```
Sirve para medir cuánto demora la ejecución del cálculo.  
La función `time.time()` devuelve el tiempo actual en segundos.

---

## 2. Presentación del programa
Se imprime un título y un texto introductorio:

```python
print("=" * 50)
print("GENERADOR DE PATENTES".center(50))
print("=" * 50)
print("Este programa calcula la N-ésima patente a partir de AAA000.")
print("La primera patente (AAA000) corresponde al número 0.\n")
```

El `.center(50)` centra el texto dentro de 50 caracteres.

---

## 3. Entrada de datos
Se pide al usuario un número entero que representa la patente a calcular:

```python
numero = int(input("Ingrese el número de patente a calcular: "))
```

Ejemplo: si ingresa `5`, se buscará la patente número 5 a partir de `AAA000`.

---

## 4. Inicialización de variables
```python
patente = ""
contador = 0   # AAA000 será el número 1
inicio = time.time()
```

- `patente` guardará la patente generada en cada vuelta.  
- `contador` cuenta cuántas patentes se han generado.  
- `inicio` guarda el tiempo exacto en que arrancó el cálculo.

---

## 5. Cálculo del máximo posible
El total de patentes posibles es:

\[ 26^3 \times 10^3 = 17.576.000 \]

```python
TOTAL_PATENTES = 26**3 * 10**3
if numero >= TOTAL_PATENTES:
    print(f"El número es demasiado grande. El máximo posible es {TOTAL_PATENTES - 1}.")
    return
```

Si el usuario pide un número mayor, se avisa y el programa termina.

---

## 6. Generación con bucles anidados
Aquí se generan todas las combinaciones posibles con **6 bucles for**:

```python
for i in range(26):
    for j in range(26):
        for k in range(26):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        contador += 1
                        patente = chr(65 + i) + chr(65 + j) + chr(65 + k) + str(l) + str(m) + str(n)
                        if contador == numero + 1:
                            print("Patente encontrada:", patente)
                            return
```

- `i, j, k` → recorren letras (A–Z).  
- `l, m, n` → recorren números (0–9).  
- `chr(65+i)` transforma un número en letra (ejemplo: `65 → A`, `66 → B`).  
- Se incrementa el `contador` en cada vuelta hasta alcanzar el número deseado.

---

## 7. Mostrar resultados
Cuando se encuentra la patente buscada, se imprime la información:

```python
print("Número solicitado:", numero)
print("Patente encontrada:", patente)
print("Valores finales de los índices:")
print(f"  i = {i} -> {chr(65+i)}")
print(f"  j = {j} -> {chr(65+j)}")
print(f"  k = {k} -> {chr(65+k)}")
print(f"  l = {l}, m = {m}, n = {n}")
fin = time.time()
print("Tiempo de ejecución:", fin - inicio, "segundos")
```

---

## 8. Estructura principal
```python
if __name__ == "__main__":
    main()
```

Esto asegura que `main()` solo se ejecute si el archivo se corre directamente, y no si se importa como módulo.

---

## 🔑 Resumen didáctico
- El programa funciona como un **odómetro**: cada posición (letra o número) avanza hasta completar el rango y luego pasa al siguiente.  
- Se usan **6 bucles anidados** para las 6 posiciones de la patente.  
- El `contador` permite saber en qué número de patente estamos.  
- Se controla el rango máximo (17.576.000 patentes posibles).  
- Se mide el tiempo de ejecución para mostrar la complejidad del algoritmo.

---

## 📌 Ejemplo de ejecución

Entrada:
```
Ingrese el número de patente a calcular: 15
```

Salida:
```
Número solicitado: 15
Patente encontrada: AAA015
Valores finales de los índices:
  i = 0 -> A
  j = 0 -> A
  k = 0 -> A
  l = 0, m = 1, n = 5

Tiempo de ejecución: 0.0001 segundos
```
