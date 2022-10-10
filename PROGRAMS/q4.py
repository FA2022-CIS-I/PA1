import pointCloud as PointCloud

def getCExepcted(calbodyFile,calreadingsFile):
    """
        Acquires positions relative to EM tracker base coordinate system of markers
        :param calBodyFile: data regarding calibration body data 
        :param calreadingsFile: data regarding the readings of the body 

        :type calBodyFile: str
        :type calreadingsFile: str

        :return: list of positions 
        :rtype: [PointCloud]
    """
    #Acquire information for frames
    objectFrames = PointCloud.extractFromFile(calbodyFile)
    trackerFrames = PointCloud.extractFromFile(calreadingsFile)
    cExepcted = []

    #Transformation for each respective references
    for frame in trackerFrames:
        F_D = objectFrames[0][0].registration(frame[0].points)
        F_A = objectFrames[0][1].registration(frame[1].points)
        c_i = objectFrames[0][2].transform(F_D.inv().composition(F_A))  
        cExepcted.append(c_i)
    return cExepcted