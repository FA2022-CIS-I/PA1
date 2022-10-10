import pointCloud as PointCloud

def transformation(calbodyFile,calreadingsFile):
    """
        Transformation, acquires the transofrmation necessary to link one point cloud to another 
        :param calbodyFile: file containing data for obtaining calibration object data 
        @param calreadingsFile
        (see driver.py for description)
        returns the matrix containing the transformation matrix

    """
    #Acquire information for frames
    objectFrames = PointCloud.extractFromFile(calbodyFile)
    trackerFrames = PointCloud.extractFromFile(calreadingsFile)
    transformations = []

    #Transformation for each respective references
    for frame in trackerFrames:
        F_D = objectFrames[0][0].registration(frame[0].points)
        F_A = objectFrames[0][1].registration(frame[1].points)
        c_i = objectFrames[0][2].transform(F_D.inv().composition(F_A))  
        transformations.append(c_i)
    return transformations