import numpy as np
import scipy.linalg as linAlg
import pandas as pd
import frame as Frame

class PointCloud:
    """ 
        Class to contain the pointCloud, a set of points
    """

    def __init__(self, data=None):
        """
            Initialization of the point cloud
            @param data is the data in which the point cloud contains
            @param self is the object in which to receive those data points
        """
        self.points = data

    def registration(self,b):
        """
            Registration - Compute the expected values 
            @param self - first point cloud as reference
            @param b - second point cloud as reference 
        """

        #per technique, we compute the mean first
        aMean = np.mean(self.points, axis =1,keepdims=True)
        bMean = np.mean(b, axis =1,keepdims=True)
        aTilde = self.points - aMean
        bTilde = b - bMean

        # use SVD to acquire V
        H = aTilde.dot(bTilde.T)
        U,S,V = linAlg.svd(H)
        U = U.T
        V_t = V.T
        
        # acquire R and p for this point cloud
        R = V_t.dot((U))
        p = bMean - R.dot(aMean)
        return Frame.Frame(R,p)
    
    def transform(self,F):
        """
            PointCloud multiplication 
            @param self, object itself, one of two partaking in multiplication 
            @param F, second object reqiured, two of two partaking in multiplication
        """
        return PointCloud(F.R.dot(self.points) + F.p)


def extractFromFile(fpath):
    """
        Extracts and creates a point cloud object from the file which contains data points. 
        @param fpath is the set of data points to read data from 
        returns a list containing all the frames and their respective point clouds
    """
    # Get Header
    header = pd.read_csv(fpath, header=None, nrows=1)
    # Get File Name
    name = header.values[0][-1].split("-")[-1].split(".")[0]
    frameInfo = header.values[0]
    # Dictionary of Frames
    fileFrames = {'calbody': 1, 'calreadings': frameInfo[-2],
               'empivot': frameInfo[-2], 'optpivot': frameInfo[-2], 'output': frameInfo[-2]}
    frameReadings = {'calbody': frameInfo[0:3], 'calreadings': frameInfo[0:3],
               'empivot': frameInfo[0], 'optpivot': frameInfo[0:2], 'output': frameInfo[0]}
    # Acquire Data
    frameData = pd.read_csv(fpath, header=None, names=[
                            "x", "y", "z"], skiprows=1)
    indexes = getIncrementIndex(frameReadings[name])
    frameClouds = []
    #Format the data so that each one is contained within a frame, essentially parsing the file
    for frame in range(fileFrames[name]):
        singularFrame = []
        for index in range(len(indexes)-1):
            singularFrame.append(PointCloud(
                frameData.values[(frame*indexes[-1]+indexes[index]):(frame*indexes[-1])+indexes[index+1],:].T))
        frameClouds.append(singularFrame)
    return frameClouds

def getIncrementIndex(frameInfo):
    """
        Helper function for extractFromFile, computes the set of indicies to increment by per data within frame
        @param frameInfo are the parameters regarding a frame
        return the set of indicies needed to traverse each frame
    """
    startPoints = []
    start = 0
    startPoints.append(0)
    if type(frameInfo) == int:
        startPoints.append(frameInfo)
    else:
        for index in frameInfo:
            start = start + index
            startPoints.append(start)
    return startPoints
