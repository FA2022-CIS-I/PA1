import numpy as np
import scipy.linalg as linAlg
import pandas as pd
import frame as Frame

class PointCloud:
    """ 
        Class to contain the pointCloud, a set of points
    """

    def __init__(self, points=None):
        """
            Initialization of a point cloud
            :param points: the set of points describing a point cloud
            :type points: np.array[][]

            :return: none
        """
        self.points = points

    def registration(self,b):
        """
            Preforms a rigid-body registration relative to another point cloud and returns the transformation 
            :param b: the point cloud attempting to register to 
            :type b: PointCloud

            :return: The transformatio n as a Frame, from current Frame to the specified frame b 
            :rtype: Frame
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
            Preform a transformation applied from another PointCloud
            :param F: The point cloud to transform with 
            :type F: Frame 

            :return: the transformed Point Cloud
            :rtype: PointCloud 
        """
        return PointCloud(F.R.dot(self.points) + F.p)


def extractFromFile(fpath):
    """
       Extract point clouds from a file 
       :param fpath: The file containing point clouds
       :type fpath: str

       :return: a list of point clouds 
       :rtype: [PointCloud]
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
      Helper function to obtain the indexes to increment by per frame 
        :param frameInfo: information particular to a frame, including the specifications of what is contained in a frame 
        :type frameInfo: [int]

        :return: a list of numerical indexes to which to itterate over
        :rtype: [int]
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
