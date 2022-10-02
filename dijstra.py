from cmath import inf
from re import S
import pygame
import dijkstra
import numpy as np

#DEFINICION DE VARIABLES A USAR
AZUL = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN= (0, 255, 0)
tamtab=10 #MODIFICAR DEPENDIENDO EL NUMERO DE CELDAS QUE SE QUIERAN EN EL CUADRO
tamCuadro = 20
inicio=-1
fin=-1
xinicio=-1
yinicio=-1
xfin=-1
yfin=-1
obsop='s'

#AUXILIARES PARA GRAFICAR GRID
x=[]
for i in range((tamtab**2)):
    if i == 0:
        x=np.append(x,1)
    
    elif i % tamtab == 0:
        x=np.append(x,1)

    elif i > 0:
        aux=x[i-1]
        x=np.append(x,aux+tamCuadro+1)

y=[]
for i in range((tamtab**2)):
    if i == 0:
        y=np.append(y,1)

    elif i % tamtab == 0:
        aux=y[i-1]
        y=np.append(y,aux+tamCuadro+1)

    elif i > 0:
        aux=y[i-1]
        y=np.append(y,aux)

#CREACION DE GRID 
pygame.init()
size = (tamtab+(tamtab*tamCuadro),tamtab+(tamtab*tamCuadro))
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Grid on PYGAME")
clock = pygame.time.Clock()
gameOver = False

#INICIO DE GRID
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    screen.fill(BLACK)
    for i in range(1, size[0], tamCuadro + 1):
        for j in range(1, size[1], tamCuadro + 1):
            pygame.draw.rect(screen, AZUL, [i, j, tamCuadro, tamCuadro], 0)
    pygame.display.flip()
    
    #INGRESO DE COORDENAS DE PUNTO DE INICIO POR EL USUARIO
    while inicio < 0  or inicio >= tamtab**2:

        while xinicio <= 0 or xinicio > tamtab: 
            xinicio=int(input('Ingrese la coordenada X de inicio:'))
            if xinicio <= 0 or xinicio > tamtab:
                print('La coordenada de inicio en X esta fuera del rango.') 
        
        while yinicio <= 0 or yinicio >tamtab:
            yinicio=int(input('Ingrese la coordenada Y de inicio:'))
            if yinicio <= 0 or yinicio > tamtab:
                print('La coordenada de inicio en Y esta fuera del rango.')

        inicio=(tamtab*(yinicio-1))+xinicio-1
        print('inicio:')
        print(inicio)

        if inicio < 0 or inicio >= tamtab**2:
            print('El inicio esta fuera del rango.')

    #GRAFICADO DE PUNTO DE INICIO
    pygame.draw.rect(screen, RED, [x[inicio], y[inicio], tamCuadro, tamCuadro], 0)
    pygame.display.flip()

    #INGRESO DE COORDENADAS DE PUNTO DE FIN POR EL USUARIO
    while fin < 0 or fin >= tamtab**2 or inicio == fin:

        while xfin <= 0 or xfin > tamtab:
            xfin=int(input('Ingrese la coordenada x de fin:'))
            if xfin <= 0 or xfin > tamtab:
                print('La coordenada de fin en X esta fuera del rango.') 

        while yfin <= 0 or yfin >tamtab:
            yfin=int(input('Ingrese la coordenada y de fin:'))
            if yfin <= 0 or yfin > tamtab:
                print('La coordenada de fin en Y esta fuera del rango.')
        
        fin=(tamtab*(yfin-1))+xfin-1
        print('fin:')
        print(fin)

        if fin < 0 or fin >= tamtab**2:
            print('El fin esta fuera del rango.')

        if inicio == fin:
            print('El inicio y el fin son iguales:')
            xfin=-1
            yfin=-1

    #GRAFICADO DE PUNTO DE FIN
    pygame.draw.rect(screen, RED, [x[fin], y[fin], tamCuadro, tamCuadro], 0)
    pygame.display.flip()

    #CREACION DE MATRIZ DE MOVIMIENTOS
    matrix=np.zeros(((tamtab**2),(tamtab**2)+tamtab))
    for i in range(tamtab**2):
        #Para los de la orilla izquierda de la cuadricula
        if i % tamtab == 0 or i ==0:
            matrix[i][i]=0
            matrix[i][i+1]=1
            matrix[i][i+tamtab]=1
            matrix[i][i-tamtab]=1
        
        #para los de la orilla derecha de la cuadricula
        elif (i+1) % tamtab == 0:
            matrix[i][i]=0
            matrix[i][i-1]=1
            matrix[i][i+tamtab]=1
            matrix[i][i-tamtab]=1
        
        #para todos los cuadros restantes
        else:
            #Todos los valores en la diagonal principal son 0
            matrix[i][i]=0
            matrix[i][i+1]=1
            matrix[i][i-1]=1
            matrix[i][i+tamtab]=1
            matrix[i][i-tamtab]=1

    matriz2=np.delete(matrix,((tamtab**2)+2,(tamtab**2)+1,(tamtab**2)),axis=1)
    
    #AGREGADO DE OBSTACULOS
    while obsop == 's':
        obsop=str(input('Desea agregar un obstaculo(s/n):'))

        while obsop == 's':
            
            #INGRESO DE COORDENADA X DEL OBSTACULO
            xobs=int(input('Ingrese la coordenada X del obstaculo:')) 
            if xobs <= 0 or xobs > tamtab:
                print('La coordenada del obstaculo en X esta fuera del rango.')
            else:
                obsop='n'
                obsaux='s'
        
        while obsaux == 's':

            #INGRESO DE COORDENADA Y DEL OBSTACULO
            yobs=int(input('Ingrese la coordenada Y del obstaculo:')) 
            if yobs <= 0 or yobs > tamtab:
                print('La coordenada del obstaculo en Y esta fuera del rango.')
            else:
                obsaux='n'
                obsop='s'

        obs=(tamtab*(yobs-1))+xobs-1

        if obs == inicio:
            print('El obstaculo es:')
            print(obs)
            print('El obstaculo y el inicio son iguales:')
            obsop='s'

        elif obs == fin:
            print('El obstaculo es:')
            print(obs)
            print('El obstaculo y el fin son iguales:')
            obsop='s'

        elif obs != inicio and obs != fin and obsop == 's':
            print('El obstaculo es:')
            print(obs)
            for i in range(tamtab**2):
                matriz2[i][obs]=0
                matriz2[obs][i]=0
            
            pygame.draw.rect(screen, BLACK, [x[obs], y[obs], tamCuadro, tamCuadro], 0)
            pygame.display.flip()

    #CALCULO DE CAMINO MAS CORTO Y DISTANCIA CON ALGORITMO DE DIJKSTRA
    camino=(dijkstra.find_shortest_path(matriz2,inicio,fin))
    print('El camino es:')
    print(camino)
    distancia=(dijkstra.find_shortest_distance(matriz2,inicio,fin))
    print('La distancia es:')
    print(distancia)
    if distancia == inf:
        print('No se puede llegar a ese punto.')
    
    for i in camino:
        pygame.draw.rect(screen, GREEN, [x[i], y[i], tamCuadro, tamCuadro], 0)
        pygame.display.flip()
        pygame.time.delay(200)
    gameOver = True
pygame.quit()