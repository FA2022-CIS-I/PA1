import numpy as np
import scipy.linalg as linAlg
import pandas as pd
import csv as csv
import frame as Frame

class PointCloud:

    def __init__(self, data=None):
        self.points = data

    def registration(self,b):
  
        aMean = np.mean(self.points, axis =1,keepdims=True)
        bMean = np.mean(b, axis =1,keepdims=True)
        aTilde = self.points - aMean
        bTilde = b - bMean

        H = aTilde.dot(bTilde.T)
        U,S,V = linAlg.svd(H)
        U = U.T
        V_t = V.T
        
        R = V_t.dot(U)
        p = bMean - R.dot(aMean)
        return Frame.Frame(R,p)
    
    def transform(self,F):
        return PointCloud(F.R.dot(self.points) + F.p)


def extractFromFile(fpath):
    # Get Header
    header = pd.read_csv(fpath, header=None, nrows=1)
    # Get File Name
    name = header.values[0][-1].split("-")[-1].split(".")[0]
    frameInfo = header.values[0]
    #print(name)
    #print(frameInfo)
    # Dictionary of Frames
    fileFrames = {'calbody': 1, 'calreadings': frameInfo[-2],
               'empivot': frameInfo[-2], 'optpivot': frameInfo[-2], 'output': frameInfo[-2]}
    frameReadings = {'calbody': frameInfo[0:3], 'calreadings': frameInfo[0:3],
               'empivot': frameInfo[0], 'optpivot': frameInfo[0:2], 'output': frameInfo[0]}
    # Acquire Data
    frameData = pd.read_csv(fpath, header=None, names=[
                            "x", "y", "z"], skiprows=1)
    #print(frameData)
    # Index Ranges
    indexes = getIncrementIndex(frameReadings[name])
    #print(indexes)
    # Parsing Data
    frameClouds = []
    #print(fileFrames)
    for frame in range(fileFrames[name]):
        singularFrame = []
        #print(frame)
        #print("indexes " + str(indexes))

        for index in range(len(indexes)-1):
           # print(frameData.values[(frame*indexes[-1]+indexes[index]):(frame*indexes[-1])+indexes[index+1],:].T)
            singularFrame.append(PointCloud(
                frameData.values[(frame*indexes[-1]+indexes[index]):(frame*indexes[-1])+indexes[index+1],:].T))
        frameClouds.append(singularFrame)
    #print(len(frameClouds))
    return frameClouds

def getIncrementIndex(frameInfo):
    #print("Frame Info " + str(type(frameInfo)))
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
