import numpy as np

def getCalibration(calibrationData, frame):
    """
        Acquires the Calibration Data regarding a set of coordinates 
        :param calibrationData: the set of data to conduct a calibration against 
        :param frame: The index of the frame that is held relative to other points
        :type calibrationData: list[][] comprising of pointClouds
        :type frame: int, of the corresponding frame

        :return: relative position of a specified point, relative to pivot and relative to marker
        :rtype: np.array[]
        
    """
    numberOfFrames = len(calibrationData)
    
    #Defining a local probe coordinate system to compute g_j
    G_first = calibrationData[0][frame].points

    g_0 = np.mean(G_first,axis = 1,keepdims=True)
    g_j = G_first - g_0

    #Variables and setup for least squares problems
    R_j = np.zeros([numberOfFrames*3,6])
    p_squares = np.zeros([numberOfFrames*3])

    for k in range(numberOfFrames):
        F = calibrationData[k][frame].registration(g_j)
        R = F.R
        p = F.p
        for i in range(0,3):
            R_j[k*3][i]= R[0][i]
            R_j[k*3+1][i]= R[1][i]
            R_j[k*3+2][i]= R[2][i]
            p_squares[k*3+i] = -1*p[i]
        
    for n in range(numberOfFrames):
        R_j[n*3][3]=-1
        R_j[n*3+1][4]=-1
        R_j[n*3+2][5]=-1
    
    #execute least squares problem
    result = np.linalg.lstsq(R_j,p_squares,rcond=None)

    #return information regarding the position relative to the EM tracker base
    pivCal = np.array(result[0][0:3])
    pivPiv = np.array(result[0][3:6])

    return pivPiv,pivCal



    
