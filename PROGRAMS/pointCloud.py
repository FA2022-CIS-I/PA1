import numpy as np
from requests import head
import scipy.linalg as scialg
import pandas as pd
import csv as csv


class PointCloud:

    def __init__(self, data=None):
        self.data = data

    def registration(self,b):
        """
            Self in analgous to a
        """
        print(type(self.data))
        print(type(b))

        aMean = np.mean(self.data, axis =1)
        bMean = np.mean(b, axis =1)
        print(aMean)
        print(bMean)

def extractFromFile(fpath):
    # Get Header
    header = pd.read_csv(fpath, header=None, nrows=1)
    # Get File Name
    name = header.values[0][-1].split("-")[-1].split(".")[0]
    #print(header.values)
    frameInfo = header.values[0, 0:3]
    #print(frameInfo)
    # Dictionary of Frames
    nframes = {'calbody': 1, 'calreadings': frameInfo[-2],
               'empivot': frameInfo[-1], 'optpivot': frameInfo[-1], 'output': frameInfo[-1]}
    # Acquire Data
    frameData = pd.read_csv(fpath, header=None, names=[
                            "x", "y", "z"], skiprows=1)
    #print(frameData)
    #print(frameInfo)
    # Index Ranges
    indexes = getIncrementIndex(frameInfo)
    print(indexes)
    # Parsing Data
    frameClouds = []
    #print(indexes)
    print(frameData.values)
    for frame in range(nframes[name]):
        singularFrame = []
        #print(frame)
        for index in range(len(indexes)-1):
            print(frameData.values[(frame*indexes[-1]+indexes[index]):(frame*indexes[-1])+indexes[index+1],:].T)
            singularFrame.append(PointCloud(
                frameData.values[(frame*indexes[-1]+indexes[index]):(frame*indexes[-1])+indexes[index+1],:].T))
        frameClouds.append(singularFrame)
    #print(len(frame_clouds))
    return frameClouds

def getIncrementIndex(frameInfo):
    startPoints = []
    start = 0
    startPoints.append(0)
    for index in frameInfo:
        start = start + index
        startPoints.append(start)
    return startPoints
