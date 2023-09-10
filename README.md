Instituto de Investigaciones en Inteligencia Artificial - Universidad Veracruzana

**Análisis de algoritmos Tarea 5**

Adaptar un algoritmo de Dijkstra para que trabaje en una rejilla de 40x40 donde se defina el punto inicial (ri, ci) y el punto final (rf, cf) y encuentre la ruta optima con las siguientes variantes:

1) Usar 4 vecinos con distancias unitarias.
1) Usar 8 vecinos.
1) Incluir posibilidades de definir obstáculos.

El lenguaje utilizado para el desarrollo del algoritmo es Python, utilizando el modulo Dijkstra del usuario crixodia en github, https://github.com/crixodia/python-dijkstra/blob/master/dijkstra.py, al cual solamente se le tiene que pasar la matriz de adyacencia, ademas se hace uno de la librería pygame para la creación del grid.

Para la creación de la matriz de adyacencia se tomo como referencia la matriz de un grid de 3x3 como se muestra a continuación:



|0|1|2|
| - | - | - |
|3|4|5|
|6|7|8|

`  `0, 1, 2, 3, 4, 5, 6, 7, 8 

0 [0. 1. 0. 1. 0. 0. 0. 0. 0.] 

1 [1. 0. 1. 0. 1. 0. 0. 0. 0.] 

2 [0. 1. 0. 0. 0. 1. 0. 0. 0.] 

3 [1. 0. 0. 0. 1. 0. 1. 0. 0.] 

4 [0. 1. 0. 1. 0. 1. 0. 1. 0.] 

5 [0. 0. 1. 0. 1. 0. 0. 0. 1.] 

6 [0. 0. 0. 1. 0. 0. 0. 1. 0.] 

7 [0. 0. 0. 0. 1. 0. 1. 0. 1.] 

8 [0. 0. 0. 0. 0. 1. 0. 1. 0.]

Se utiliza un ciclo for para crear los movimientos de cada celda, donde se crean 3 casos específicos:

1. Para las celdas del centro, estas se pueden mover hacia la izquierda, derecha.
1. Para las celdas del lado izquierdo, haciendo que solamente se puedan mover hacia la derecha.
1. Para las celdas del lado derecho haciendo que solo se puedan mover hacia la izquierda.

Para los movimientos de arriba y abajo se hace uso de una variable llamada tamtab, la cual tiene como valor el numero de celdas en el grid para cada lado, gracias a esto es posible cambiar el tamaño del grid sin modificar lo demás del código, ademas de permitir que dentro el for se agreguen estos movimientos a cada celda. Y ademas gracias a esta misma variable se agregan los movimientos para los diagonales en el caso de los 8 vecinos. En el caso de que el usuario meta algún obstáculos, los movimientos de estas celdas son eliminadas de la matriz, para que de esta manera sea imposible llegar a ellos.

El código tiene limitaciones para que el inicio y el fin sean coordenadas dentro del tamaño del grid, ademas que los obstáculos que el usuario meta no puedan ser ni el inicio ni el fin, sin tener limitaciones en el numero de obstáculos que meta.



Al correr el código primero obtenemos un grid con todas las celdas en color azul:

![](Aspose.Words.5e9c9324-b742-493d-85a2-765f2212f73f.001.png)

Después el usuario agrega el inicio, poniéndose la celda en color rojo:

![](Aspose.Words.5e9c9324-b742-493d-85a2-765f2212f73f.002.png)

A continuación, el usuario agrega el final marcándose en color rojo:

![](Aspose.Words.5e9c9324-b742-493d-85a2-765f2212f73f.003.png)

A continuación cada celda que el usuario ingrese como obstáculo se pondrá de color negro:

![](Aspose.Words.5e9c9324-b742-493d-85a2-765f2212f73f.004.png) ![](Aspose.Words.5e9c9324-b742-493d-85a2-765f2212f73f.005.png)

Finalmente, cuando el usuario decida no meter mas obstáculos, el recorrido empezara a verse, cambiando las celdas por las que pasa a color verde:

![](Aspose.Words.5e9c9324-b742-493d-85a2-765f2212f73f.006.png)

Mientras que en la Terminal se imprime cual es el camino elegido y la distancia del recorrido:

![](Aspose.Words.5e9c9324-b742-493d-85a2-765f2212f73f.007.png)

**Conclusión:**

Como se puede observar se llega al resultado esperado, obteniendo el camino mas corto para llegar al final, esto logrado gracias al algoritmo de Dijsktra, que a partir de la matriz de adyacencia calcula ese camino y la distancia, ademas gracias a la librería pygame es posible simular el recorrido para así ver de manera grafica como es que si obtiene ese camino y como se recorre.
Análisis de algoritmos
