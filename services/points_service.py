import math

POINT_ZERO = (0,0)
INFINITY = 99999999999999999

def calculateDistance(point: tuple, pointsList: list):
    distance = 0
    for actual in pointsList:
        if point[0] < INFINITY and point[1] < INFINITY:
            vector = math.pow((point[0] - actual[0]), 2) + math.pow((point[1] - actual[1]), 2)
            distance += math.sqrt(vector)
    return int(distance)

def calculateDistanceByPoint(points: list, pointsList: list):
    distance = 0
    result: tuple = (POINT_ZERO, INFINITY)
    for actual in points:
       distance = calculateDistance(actual, pointsList)
       if distance < result[1]:
           result = (actual, distance)
    return result

def newPoint(pointsList: list, limitX: tuple, limitY: tuple):
    xLess = INFINITY
    xHigher = INFINITY
    yLess = INFINITY
    yHigher = INFINITY
    for point in pointsList:
        if point[0] > limitX[0] and point[0] < limitX[1] and point[1] >= limitY[0] and point[1] >= limitY[1]:
            xLess = (xLess, point[0])[point[0] < xLess] 
            xHigher = (xHigher, point[0])[point[0] < xHigher] 
            yLess = (yLess, point[1])[point[1] < yLess] 
            yHigher = (yHigher, point[1])[point[1] < yHigher] 
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
    