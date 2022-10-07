
import pointCloud as PointCloud
import pivotCalibration as pivCal

def getPosition(empivot, optpivot):

    pivotCalibrationData = PointCloud.extractFromFile(empivot)
    pivCal.getPosition(pivotCalibrationData)

