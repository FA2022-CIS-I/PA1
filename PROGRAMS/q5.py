
import pointCloud as PointCloud
import pivotCalibration as pivCal

def getCalibrationReadings(empivot):
    """
        Get positional information from empivot
        @param empivot - see driver.py
        returns the positoinal location relative to tracker
    """

    pivotCalibrationData = PointCloud.extractFromFile(empivot)
    pivCalAns, pivPivAns = pivCal.getCalibration(pivotCalibrationData)
    return pivPivAns
