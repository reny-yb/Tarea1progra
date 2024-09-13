import numpy as np
import time
import matplotlib.pyplot as plt
from time import perf_counter # Mide el tiempo de ejecución de código de manera precisa

#Creamos el decorador que se aplica sobre la función ejecución que calcula el tiempo de ejecución
def tiempo_ejecucion(func):
    def wrapper(self, metodo, *args, **kwargs):
        inicio = time.time()  # tiempo de inicio
        resultado = func(self, metodo, *args, **kwargs)
        fin = time.time()  # tiempo de fin
        print(f"Tiempo de ejecución para {func.__name__} ({metodo}): {fin - inicio:.6f} segundos") #cantidad de decimales
        return resultado
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
            
#código para grafico
t_combinatoria = []
t_recursivo = []
n_values = range(4, 15)  # Prueba tamaños pequeños para evitar tiempos excesivos en recursión

# Ejecutar cada método para varios valores de N y M
for i in n_values:
    pcb = PCB(i, i)  # Grillas de NxN

    # Tiempo para combinatoria
    tiempo_inicio = perf_counter()
    pcb.ejecutar('combinatoria')
    tiempo_total = perf_counter() - tiempo_inicio
    t_combinatoria.append(tiempo_total)

    # Tiempo para recursivo
    tiempo_inicio = perf_counter()
    pcb.ejecutar('recursivo')
    tiempo_total = perf_counter() - tiempo_inicio
    t_recursivo.append(tiempo_total)

# Gráfico de los tiempos de ejecución
plt.plot(n_values, t_combinatoria, label='Combinatoria')
plt.plot(n_values, t_recursivo, label='Recursivo')

plt.xlabel('Tamaño de la grilla (N = M)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Comparación de tiempos de ejecución')
plt.legend()
plt.grid(True)
plt.savefig('tiempos_ejecucion.svg') 
plt.show()     
