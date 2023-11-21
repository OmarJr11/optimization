import math

POINT_ZERO = (0,0) #Punto original
INFINITY = 99999999999999999 #Infinito

""" 
    Funcion que calcula la distancia desde un punto de origen hasta multiples puntos de llegada
    point: un punto (X,Y)
    pointsList: una lista de puntos (X,Y)
"""
def calculateDistance(point: tuple, pointsList: list):
    distance = 0
    #Se calcula la distancia del punto de origen hasta los multiples puntos de llegada
    for actual in pointsList:
       vector = math.pow((point[0] - actual[0]), 2) + math.pow((point[1] - actual[1]), 2)
       distance += math.sqrt(vector)
    return int(distance)

""" 
    Funcion que calcula la distancia desde los puntos de origen propuesto hasta multiples puntos de llegada
    retorna el punto con menor distancia
    points: Lista de puntos (X,Y) propuestp para la optimizacion
    pointsList: una lista de puntos (X,Y) ingresada por el usuario
"""
def calculateDistanceByPoint(points: list, pointsList: list):
    distance = 0
    result: tuple = (POINT_ZERO, INFINITY)
    i = 1
    #Se recorren los puntos propuesto para la optimizacion
    for actual in points:
        #Se consiguen los puntos conectados al hub y los puntos conectados al central principal
        newLists = generateNewPointList(pointsList, i)
        listPointNew = newLists[1]
        #Se calcula la distancia
        if len(listPointNew) > 0:
            listPointNew.insert(0, POINT_ZERO)
            distance = (calculateDistance(actual, listPointNew), calculateDistance(actual, listPointNew) + calculateDistance(POINT_ZERO, newLists[0]))[len(newLists[0]) > 0]
        else:
            distance = calculateDistance(POINT_ZERO, pointsList)
        #Se guarda la menor
        if distance < result[1]:
           result = (actual, distance)
        i+=1
    return result


""" 
    Funcion que calcula las conexiones para el punto propuesto y para el punto inicial
    pointsList: una lista de puntos (X,Y) ingresada por el usuario
    type: tipo del cuadrante
"""
def generateNewPointList(pointsList: list, type: int):
    rangeX: tuple
    rangeY: tuple
    if type == 1:
        rangeX = (0, INFINITY) 
        rangeY = (0, INFINITY)
    elif type == 2:
        rangeX = (0, INFINITY) 
        rangeY = (-1*INFINITY, -1)
    elif type == 3:
        rangeX = (-1*INFINITY, -1) 
        rangeY = (-1*INFINITY, -1)
    elif type == 4:
        rangeX = (-1*INFINITY, -1) 
        rangeY = (0, INFINITY)
    elif type == 5:
        rangeX = (-1*INFINITY, INFINITY) 
        rangeY = (0, INFINITY)
    elif type == 6:
        rangeX = (-1*INFINITY, INFINITY) 
        rangeY = (-1*INFINITY, -1)
    elif type == 7:
        rangeX = (0, INFINITY)
        rangeY = (-1*INFINITY, INFINITY) 
    elif type == 8:
        rangeX = (-1*INFINITY, -1) 
        rangeY = (-1*INFINITY, INFINITY)
    
    listPoint0 = []
    listPointNew = []
    for point in pointsList:
        if point[0] >= rangeX[0] and point[0] <= rangeX[1] and point[1] >= rangeY[0] and point[1] <= rangeY[1]:
            listPointNew.insert(0, point)
        else:
            listPoint0.insert(0, point)
    return (listPoint0, listPointNew)     
""" 
    Se calcula un punto propuesto para la optimizacion dependiendo de los puntos ingresado y su rango
    pointsList: una lista de puntos (X,Y) ingresada por el usuario
    limitX: Rango en X
    limitY: Rango en Y
"""
def newPoint(pointsList: list, limitX: tuple, limitY: tuple):
    xLess = INFINITY
    xHigher = -INFINITY
    yLess = INFINITY
    yHigher = -INFINITY
    for point in pointsList:
        if point[0] >= limitX[0] and point[0] <= limitX[1] and point[1] >= limitY[0] and point[1] <= limitY[1]:
            xLess = (xLess, point[0])[point[0] < xLess] 
            xHigher = (xHigher, point[0])[point[0] > xHigher]
            yLess = (yLess, point[1])[point[1] < yLess] 
            yHigher = (yHigher, point[1])[point[1] > yHigher]
    return ((xLess + xHigher)//2, (yLess + yHigher)//2)

def searchNewPoint(pointsList: list):
    quadrantXPositiveYPositive = newPoint(pointsList, (0, INFINITY), (0, INFINITY))
    quadrantXPositiveYNegative = newPoint(pointsList, (0, INFINITY), (-1 * INFINITY, -1))
    quadrantXNegativeYNegative = newPoint(pointsList, (-1 * INFINITY, -1), (-1 * INFINITY, -1))
    quadrantXNegativeYPositive = newPoint(pointsList, (-1 * INFINITY, -1), (0, INFINITY))
    quadrantXYPositive  = newPoint(pointsList, (-1 * INFINITY, INFINITY), (0, INFINITY))
    quadrantXYNegative = newPoint(pointsList, (-1 * INFINITY, INFINITY), (-1 * INFINITY, -1))
    quadrantYXNegative = newPoint(pointsList, (-1 * INFINITY, -1), (-1 * INFINITY, INFINITY))
    quadrantYXPositive  = newPoint(pointsList, (0,INFINITY), (-1 * INFINITY, INFINITY))
    return [quadrantXPositiveYPositive, quadrantXPositiveYNegative, quadrantXNegativeYNegative, quadrantXNegativeYPositive, quadrantXYPositive, quadrantXYNegative, quadrantYXNegative, quadrantYXPositive]

def optimizeDistance(pointsList: list):
    distanceOriginal = calculateDistance(POINT_ZERO, pointsList)
    points = searchNewPoint(pointsList)
    result = calculateDistanceByPoint(points, pointsList)
    return (result, distanceOriginal)
    