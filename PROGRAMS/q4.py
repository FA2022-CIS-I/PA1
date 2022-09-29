import pointCloud as PointCloud

def transformation(calbodyFile,calreadingsFile):

    PointCloud
    #body_frames = PointCloud.extractFromFile(calbodyFile)
    readings_frames = PointCloud.extractFromFile(calreadingsFile)
    #print(type(body_frames[0]))
    transformations = []
    for frame in readings_frames:
        a=10
        #print(type(frame))
        #print(frame[1].data)
        #body_frames[0][0].registration(frame[0].data)