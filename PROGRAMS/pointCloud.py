import numpy as np
from requests import head
import scipy.linalg as scialg
import pandas as pd
import csv as csv


class PointCloud:

    def __init__(self, data=None):
        self.data = data


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
    #print(indexes)
    # Parsing Data
    frame_clouds = []
    #print(indexes)
    for frame in range(nframes[name]):
        for index in range(len(indexes)-1):
            # print(indexes[index])
            frame_clouds.append(PointCloud(
                frameData.values[indexes[-1]*frame + indexes[index] + frameInfo[-1]*frame:indexes[index+1], :].T))
       # print(len(frame_clouds))

    #print(len(frame_clouds))
    return frame_clouds

def getIncrementIndex(frameInfo):
    startPoints = []
    start = 0
    startPoints.append(0)
    for index in frameInfo:
        start = start + index
        startPoints.append(start)
    return startPoints
