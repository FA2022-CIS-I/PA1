
import pointCloud as PointCloud
import pivotCalibration as pivCal

def getCalibrationReadings(empivot):

    pivotCalibrationData = PointCloud.extractFromFile(empivot)
    pivCalAns, pivPivAns = pivCal.getPosition(pivotCalibrationData)
    return pivPivAns
