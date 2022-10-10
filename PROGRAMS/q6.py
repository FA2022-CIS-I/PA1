import numpy as np
import pointCloud as PointCloud
import pivotCalibration as pivCal


def getCalibrationReadings(calBody,optPivot):
    bodyData = PointCloud.extractFromFile(calBody)
    optData = PointCloud.extractFromFile(optPivot)

    F_D = optData[0][0].registration(bodyData[0][0].points)


    for i in range(len(optData)):
        optData[i][1] = optData[i][1].transform(F_D)

    pivCalAns, pivPivAns = pivCal.getCalibration(optData,1)

    return pivPivAns
