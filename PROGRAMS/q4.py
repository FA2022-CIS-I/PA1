import pointCloud as PointCloud

def transformation(calbodyFile,calreadingsFile):

    PointCloud
    objectFrames = PointCloud.extractFromFile(calbodyFile)
    trackerFrames = PointCloud.extractFromFile(calreadingsFile)
    #print(type(body_frames[0]))
    transformations = []
    for frame in trackerFrames:
        F_D = objectFrames[0][0].registration(frame[0].points)
        F_A = objectFrames[0][1].registration(frame[1].points)
        c_i = objectFrames[0][2].transform(F_D.inv().composition(F_A))  
        transformations.append(c_i)
    return transformations