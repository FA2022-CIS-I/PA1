
import pointCloud as PointCloud
import pivotCalibration as pivCal

def getRelativePosition(empivot):
    """
        Acquires positions relative to EM tracker base coordinate system of a given dimple 
        :param empivot: data points of probe in EM coordinates
        :type empivot: str

        :return: coordinate describing the position
        :rtype: np.array[]
    """
    # Acquisition of data
    pivotCalibrationData = PointCloud.extractFromFile(empivot)
    
    # Obtain data regarding pivot calibration
    pivCalAns, pivPivAns = pivCal.getCalibration(pivotCalibrationData,0)
    return pivPivAns
