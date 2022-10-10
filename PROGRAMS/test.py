from random import random
import numpy as np
import scipy.linalg as linalg
import pointCloud as PointCloud


def test_operation(tolerance):

    rotationMatrix = rotation()
    randomMatrixA = getRandomMatrix(3, 10)
    randomMatrixB = getRandomMatrix(3, 1)

    print("Random Matrix A: \n" + str(randomMatrixA))
    print("Random Matrix B: \n" + str(randomMatrixB))

    b = rotationMatrix.dot(randomMatrixA) + randomMatrixB
    F = PointCloud.PointCloud(randomMatrixA).registration(
        PointCloud.PointCloud(b).points)
    
    print("Matrix b:\n " + str(b))
    print("Matrix F.R \n" + str(F.R)+"\n Matrix F.p\n" + str(F.p))


    calculated = np.abs(rotationMatrix - F.R)
    toleranceResult = np.all(calculated - F.R) <= tolerance
    if(toleranceResult is False):
        
        print("Rotation matrix is not within tolerance: " + str((calculated - F.R)))
    else:
        print("Rotation matrix within tolerance of F.R: " + str(toleranceResult))

    determinantresult = np.abs(linalg.det(F.R) - linalg.det(rotationMatrix))
    toleranceResult = (determinantresult) <= tolerance
    if(toleranceResult is False):
        
        print("Rotation matrix determinant is not roughly one: " + str(determinantresult))
    else:
        print("Rotation matrix determinant is roughly one: " + str(toleranceResult))


    calculated = np.abs(rotationMatrix - F.p)
    toleranceResult = np.all(calculated - F.p) <= tolerance
    if(toleranceResult is False):
        print("Translational matrix is not within tolerance: " + str(calculated - F.p))
    else:
        print("Translational matrix is within tolerance: " + str(toleranceResult))


def rotation():
    omega = np.random.uniform(0, 2*np.pi)
    beta = np.random.uniform(0, 2*np.pi)
    gamma = np.random.uniform(0, 2*np.pi)
    from scipy.spatial.transform import Rotation as R
    rotationX = R.from_quat(
        [0, 0, np.sin(omega), np.cos(np.cos(omega))]).as_matrix()
    rotationY = R.from_quat(
        [0, 0, np.sin(beta), np.cos(np.cos(beta))]).as_matrix()
    rotationZ = R.from_quat(
        [0, 0, np.sin(gamma), np.cos(np.cos(gamma))]).as_matrix()
    return rotationX.dot(rotationY.dot(rotationZ))


def getRandomMatrix(row, col):
    return np.random.uniform(0, 10, (row, col))
