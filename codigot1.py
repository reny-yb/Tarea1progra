import numpy as np
import time
import matplotlib.pyplot as plt
from time import perf_counter # Mide el tiempo de ejecución de código de manera precisa

#Creamos el decorador que se aplica sobre la función ejecución que calcula el tiempo de ejecución
def tiempo_ejecucion(func):
    def wrapper(self, metodo, *args, **kwargs):
        inicio = time.time()  # tiempo de inicio
        func(self, metodo, *args, **kwargs)  # ejecuta el método (no necesita retornar valor)
        fin = time.time()  # tiempo de fin
        tiempo_total = fin - inicio
        print(f"Tiempo para {func.__name__} ({metodo}): {tiempo_total:.6f} segundos")
        return tiempo_total
    return wrapper

    # Definimos la clase PCB con los tamaños de la grilla de tamaño NxM

class PCB:
    def __init__(self, N, M):
        self.LadoN = N 
        self.LadoM = M 

    # Nos damos cuenta que el problema se puede resolver con permutaciones de elementos donde
    # se tienen dos tipos de movimientos: hacia abajo y hacia la derecha. Esto es una combinatoria,
    # se implementa el factorial dentro del primer método porque pense que así podríamos obtener
    # de mejor manera el tiempo de ejecución pero en verdad da lo mismo, es de tipo 0(1) 
    # pues es constante para cualquier tamaño de grilla o PCB. Este es nuestro primer método

    def met_1(self):
        def factorial(n):
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

        num_caminos = (factorial(self.LadoN + self.LadoM - 2) //
                      (factorial(self.LadoN - 1) * factorial(self.LadoM - 1)))
        print("Método 1 (combinatoria):", num_caminos)
        return num_caminos
    #El problema también se puede resolver de forma recursiva, para esto cree
    #el met_2 que se llama () porque sino debiamos llamarlo como pcb.met_2(N-1,M-1)
    #pero ya teníamos estos datos al crear la instancia de clase

    def met_2(self):
        # Llama al método recursivo con los valores iniciales (0, 0)
        resultado = self._met_2_recursivo(0, 0)
        print("Método 2 (recursividad):", resultado)
        return resultado

    def _met_2_recursivo(self, n, m):
        # Caso base: si estamos en la esquina inferior derecha
        if n == self.LadoN - 1 and m == self.LadoM - 1:
            return 1
        # Caso base: si estamos fuera de los límites
        if n >= self.LadoN or m >= self.LadoM:
            return 0
        # Se suma el resto
        resultado = self._met_2_recursivo(n + 1, m) + self._met_2_recursivo(n, m + 1)
        return resultado

    @tiempo_ejecucion #Aplicamos decorador sobre la función que permite escoger entre uno de los dos métodos
    def ejecutar(self, metodo):
        if metodo == 'combinatoria':
            self.met_1()
        elif metodo == 'recursivo':
            self.met_2()
        else:
            raise ValueError("Método no válido. Usa 'combinatoria' o 'recursivo'.") 

#a continuación el código para graficar, se prueban 6 inputs distintos
pcb_lista = [PCB(2, 3), PCB(10, 11), PCB(11, 12),PCB(13,13)]

# Listas para almacenar los tiempos
tiempos_combinatoria = []
tiempos_recursivo = []

# Ejecutar los métodos y recolectar tiempos
for pcb in pcb_lista:
    tiempos_combinatoria.append(pcb.ejecutar('combinatoria'))
    tiempos_recursivo.append(pcb.ejecutar('recursivo'))

# Graficar los tiempos de ejecución
labels = ['(2,3)',  '(10,11)','(11,12)','(13,13)']
x = np.arange(len(labels))

plt.figure(figsize=(10, 6))

# Graficar las líneas
plt.plot(x, tiempos_combinatoria, label='Combinatoria', marker='o', color='b', linestyle='-')
plt.plot(x, tiempos_recursivo, label='Recursivo', marker='o', color='r', linestyle='-')

# Configurar el gráfico
plt.xlabel('Dimensiones (N, M)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de tiempos de ejecución (Combinatoria vs Recursivo)')
plt.xticks(x, labels)
plt.legend()

# Mostrar la gráfica
plt.show()