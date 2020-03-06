#read data from .asc file 
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
import numpy as np

def ReadData(file_path):
    data_frame = pd.read_csv(file_path,skiprows=6,encoding="gbk",engine='python',sep=' ',delimiter=None, index_col=False,header=None,skipinitialspace=True)
    #data_frame = pd.read_csv(file_path)
    row,col = data_frame.shape
    value = data_frame.values
    res = value.reshape(262150,1)[0:262144].reshape(512,512).T
    res[res<0]=0
    #print(data_frame.ix[1,2])
    # print(value[23:30])
    # print(row,col,row*col)
    return res
