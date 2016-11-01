import gzip
import pickle
import numpy as np
import matplotlib
from cycler import cycler
import urllib
import os
import sys
from MulticoreTSNE import MulticoreTSNE as TSNE
from datetime import datetime

matplotlib.use('ps')
import matplotlib.pyplot as plt

def log(string):
    sys.stderr.write('[' + str(datetime.now()) + '] ' + str(string) + '\n')
    sys.stderr.flush()

def iter_loadtxt(filename, delimiter=',', skiprows=0, dtype=float):
    def iter_func():
        with open(filename, 'r') as infile:
            for _ in range(skiprows):
                next(infile)
            for line in infile:
                line = line.rstrip().split(delimiter)
                for item in line:
                    yield dtype(item)
        iter_loadtxt.rowlength = len(line)
 
    data = np.fromiter(iter_func(), dtype=dtype)
    data = data.reshape((-1, iter_loadtxt.rowlength))
    return data

def get_data(file_name): 
    a = iter_loadtxt(file_name,delimiter=' ',skiprows=1,dtype=np.float64)
    b = iter_loadtxt("/tmp/subset.blp.txt.labels",delimiter=' ',skiprows=0,dtype=np.int64)
    if a.shape[0] != b.shape[0]: 
      raise ValueError("Shape x does not match shape y "+str(a.shape)+" vs "+str(b.shape))
    return a,b


def plot(Y, classes, name):
    digits = set(classes)
    fig,ax = plt.subplots()
    almost_black = '#262626'
    for x,y,l in Y:
       color = '#4daf4a'
       if int(l) == 1: 
         color = '#e41a1c'
       ax.scatter(x, y, label=str(1), alpha=0.5, edgecolor=almost_black, facecolor=color, linewidth=0.15)

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    spines_to_remove = ['top', 'right','bottom','left']
    for spine in spines_to_remove:
      ax.spines[spine].set_visible(False)
    fig.savefig(name,bbox_inches='tight',pad_inches=0,dpi=600)

import glob

files = glob.glob('*.dat')
for file in files:
  target_name = file[:-3]+'eps'
  data, classes = get_data(file)
  classes = classes.flatten()
  dims = data.shape[1]
  points = data.shape[0]
  log("File "+str(file)+" has points ="+str(points)+" dims = "+str(dims))
  plot(data,classes, target_name)
