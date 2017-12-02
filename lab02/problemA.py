import numpy as np


def printMatrix(result):
    for r in result:
        print(r)

def multiplyMatrix(X, Y):
    result = [x[:] for x in [[0] * len(X)] *len(Y)]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result


def checkConvergenceCondition(prevMatrix, matrix):
    result = np.subtract(matrix, prevMatrix)
    maxEl = np.amax(result)
    return maxEl >= 10**-5

def multiplyToStationaryState(matrix):
    result = matrix
    iterations = 1
    result = multiplyMatrix(result, matrix)
    prevMatrix = matrix
    while checkConvergenceCondition(prevMatrix, result):
        prevMatrix = result;
        result = multiplyMatrix(result, matrix)
        iterations = iterations + 1
    return result, iterations


matrix = [
    [0.64, 0.32, 0.04],
    [0.4, 0.5, 0.1],
    [0.25, 0.5, 0.25]
]

resultMatrix, iterations = multiplyToStationaryState(matrix)
print(iterations)
printMatrix(resultMatrix)
