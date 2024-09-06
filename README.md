✨**Respuestas parte teórica tarea 1**✨

**¿Qué es un paradigma de programación?**
Un paradigma según la RAE es un "conjunto de teorías cuyo núcleo central se acepta sin cuestionar y que suministra la base 
y modelo para resolver problemas y avanzar en el conocimiento.", se entiende entonces como un paradigma de programación a la
forma de pensar y estructurar un código con el objetivo de solucionar un problema, lo que termina siendo el cómo nos enfrentamos a este,
la manera de separar los datos (estructurar) y definir las funciones adecuadas para resolver.

**¿En qué se basa la programación orientada a objetos?**
Con el paradigma de Programación Orientado a Objetos lo que buscamos es dejar de centrarnos en la lógica pura de los 
programas, para empezar a pensar en objetos, lo que constituye la base de este paradigma. Estos objetos representan componentes
del sistema que tienen datos (atributos) y comportamientos (métodos). Los programadores crean plantillas llamadas clases,
que sirven para definir las características y acciones de los objetos. Luego, se crean objetos individuales a partir de la plantilla de clase.

**¿Cuál es la diferencia entre recursividad e iteración, y cómo se relaciona esto con la notación
big 𝑂?explicar la diferencia de rendimiento entre 𝑂(1) y 𝑂(𝑛)**
La diferencia entre recursividad e iteración es cómo se busca finalizar la ejecución de un proceso. En una función recursiva, se define
un caso base, y la función se sigue ejecutando llamándose a sí misma hasta llegar a ese punto que detiene la recursión. En cambio, una
función iterativa repite un bloque de código utilizando un bucle, como for o while, y la ejecución se repetirá hasta que se cumpla 
o deje de cumplir una condición específica. Esto se relaciona con la notación Big O pues como son enfoques distintos la cantidad de tiempo 
y espacio que consumen son distintos, para las funciones recursivas cada llamada recursiva se apila en la memoria, lo que puede incrementar
el uso de espacio, en cambio la función iterativa no necesita utilizar la pila de llamadas. 

La diferencia entre el rendimiento O(1) y O(n) se refiere a el tiempo que se demora en ejecutar un codigo según la naturaleza de su entrada,
un rendimiento O(1) nos habla de una ejecución de tiempo constante sin importar el tamaño de su entrada mientras que 0(n) nos habla de que
linealmente aumenta el tiempo de ejecución según el tamaño de la entrada.

**¿Cómo se calcula el orden en un programa que funciona por etapas?**
El orden en un programa que funciona por etapas se calcula analizando el Big O de cada etapa individualmente. Luego, se toma en cuenta la
etapa con el mayor tiempo de ejecución (la más costosa) para determinar la complejidad total del programa. Por ejemplo, si una etapa tiene
una complejidad O(1) y otra es O(log n), la complejidad total del programa será O(log n), ya que se toma el mayor orden de entre las etapas.

**¿Cómo se puede determinar la complejidad temporal de un algoritmo recursivo?**
Para determinar la complejidad temporal de un algoritmo recursivo, se debe ver cómo el tiempo de ejecución varía con el tamaño de la entrada 
y las llamadas recursivas, esto se denomina relación de recurrencia luego con el uso del Teorema Maestro el cual proporcionan una forma sistemática
de analizar la complejidad pues considera tres componentes principales: el número de subproblemas generados, el tamaño al que se reduce cada subproblema
y el costo del trabajo realizado fuera de las llamadas recursivas. Dependiendo de la relación entre estos componentes, el
teorema ofrece una fórmula para determinar la complejidad temporal del algoritmo.

