import numpy as np
import pointCloud as PointCloud
import pivotCalibration as pivCal


def getCalibrationReadings(calBody,optPivot):
    """
        Acquires predicted EM marker positions on object given measured positions
        :param calBody: data points of the data describing calibrataion object
        :param optpivot: data points of calibration from optical
       
        :type calBody: str
        :type optpivot: str

        :return: coordinate describing the position
        :rtype: np.array[]
    """
    
    #Acquire information from files
    bodyData = PointCloud.extractFromFile(calBody)
    optData = PointCloud.extractFromFile(optPivot)

    # Acquire registration from optical tracker to em tracker
    F_D = optData[0][0].registration(bodyData[0][0].points)

    #conduct this for each optical data reading
    for i in range(len(optData)):
        optData[i][1] = optData[i][1].transform(F_D)

    # acquire calibration coordinate for optical data
    pivCalAns, pivPivAns = pivCal.getCalibration(optData,1)

    return pivPivAns
