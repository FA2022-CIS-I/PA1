
import pointCloud as PointCloud
import pivotCalibration as pivCal

def getPosition(empivot, optpivot):

    pivotCalibrationData = PointCloud.extractFromFile(empivot)
    pivCalAns, pivPivAns = pivCal.getPosition(pivotCalibrationData)
    return pivPivAns
