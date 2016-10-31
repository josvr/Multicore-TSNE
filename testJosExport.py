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

matplotlib.use('Agg')
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
    fig = plt.figure()
    colormap = plt.cm.spectral
    plt.gca().set_prop_cycle(
        cycler('color', [colormap(i) for i in np.linspace(0, 0.9, 10)]))
    ax = fig.add_subplot(111)
    labels = []
    for d in digits:
        idx = classes == d
        ax.plot(Y[idx, 0], Y[idx, 1], 'o')
        labels.append(d)
    ax.legend(labels, numpoints=1, fancybox=True)
    fig.savefig(name)

def export(Y, classes, name):
   with open(name, 'w') as f:
     f.write("x y label\n")
     for y_i in range(0,Y.shape[0]):
        dim1 = Y[y_i][0]
        dim2 = Y[y_i][1]
        label = classes[y_i]
        f.write(str(dim1)+" "+str(dim2)+" "+str(label)+"\n")

################################################################

perp = [400]
files = ['/tmp/export/originalData.txt','/tmp/export/Layer0.txt','/tmp/export/Layer1.txt','/tmp/export/Layer2.txt']
for file in files:
 for p in reversed(perp):
  if file == '/tmp/export/Layer1.txt' and p == 500: 
    continue
  log("Going to process "+str(file)+" and perplexity = "+str(p))
  data, classes = get_data(file)
  #data = data[1:3000]
  #classes = classes[1:3000]
  classes = classes.flatten()
  dims = data.shape[1]
  points = data.shape[0]
  log("File "+str(file)+" has points ="+str(points)+" dims = "+str(dims))
  log("start TSNE")
  tsne = TSNE(n_jobs=4,perplexity=p,n_iter=5000)
  data_tsne = tsne.fit_transform(data)
  log("end TSNE")
  export(data_tsne, classes, 'tsne_'+str(dims)+'D-'+str(p)+'p.dat')
  plot(data_tsne,classes, 'tsne_'+str(dims)+'D-'+str(p)+'p.png')
  data = None
  data_tsne = None
  classes = None
  tsne = None
  log ('Ready '+str(file)+' and perplexity = '+str(p));
