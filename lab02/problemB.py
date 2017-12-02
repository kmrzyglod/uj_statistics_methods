import numpy as np


def printMatrix(result):
    for r in result:
        print(r)

def iterate(probabilityMatrix, startPoint, length):
    nextNode = startPoint
    nodeCounter = [0, 0, 0]
    for i in range(0, length):
        nextNode = np.random.choice(np.arange(0, 3), p=probabilityMatrix[nextNode])
        if(i > 1000):
            nodeCounter[nextNode] = nodeCounter[nextNode] + 1
    nodeCounter[0] = float(nodeCounter[0])/(length - 1000)
    nodeCounter[1] = float(nodeCounter[1])/(length - 1000)
    nodeCounter[2] = float(nodeCounter[2])/(length - 1000)
    return nodeCounter


matrix = [
        [0.64, 0.32, 0.04],
        [0.4, 0.5, 0.1],
        [0.25, 0.5, 0.25]
]

printMatrix(iterate(matrix, 0, 10**4))