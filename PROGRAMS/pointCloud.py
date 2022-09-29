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
    # Dictionary of Frames
    nframes = {'calbody':1,}
    
    