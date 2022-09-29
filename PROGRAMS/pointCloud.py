import numpy as np
from requests import head
import scipy.linalg as scialg
import pandas as pd
import csv as csv


class PointCloud:

    def __init__(self,data=None):
        data = data

def extractFromFile(fpath):
    # Get Header
    header = pd.read_csv(fpath,header=None,nrows =1)
    # Get File Name    
    name = header.values[0][-1].split("-")[-1].split(".")[0]
    frameInfo = header.values[0,0:-1]
    # Dictionary of Frames
    nframes = {'calbody':1,'calReadings':frameInfo[-1],'empivot':frameInfo[-1],'optpivot':frameInfo[-1],'output':frameInfo[-1]}
    # Acquire Data
    frameData = pd.read_csv(fpath,header=None,names=["x","y","z"],skiprows=1)
    
    # Index Ranges
    startPoints = getIncrementIndex(frameInfo)
    
    #Parsing Data
    frame_clouds = []
    startingPoint = 0
    for itteration in nframes[name]:
        
    
    
def getIncrementIndex(frameInfo):
    startPoints = []
    start = 0
    startPoints.append(0)
    for index in frameInfo:
        start = start + index
        startPoints.append(start)
    return startPoints