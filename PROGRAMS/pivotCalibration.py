import numpy as np

def getPosition(calibrationData):
    numberOfFrames = len(calibrationData)
    
    G_first = calibrationData[0][0].points

    g_0 = np.mean(G_first,axis = 1,keepdims=True)
    g_j = G_first - g_0

    R_j = np.zeros([numberOfFrames*3,6])
    p_squares = np.zeros([numberOfFrames*3])

    for k in range(numberOfFrames):
        F = calibrationData[k][0].registration(g_j)
        R = F.R
        p = F.p
        for i in range(0,3):
            R_j[k*3][i]= R[0][i]
            R_j[k*3+1][i]= R[1][i]
            R_j[k*3+2][i]= R[2][i]
            p_squares = -1*p[i]
        
    for n in range(numberOfFrames):
        R_j[n*3][3]=-1
        R_j[n*3+1][4]=-1
        R_j[n*3+2][5]=-1
    print((R_j))
    print(p_squares)
    
    result = np.linalg.lstsq(R_j,p_squares)
    print(result)


    
