#!/bin/bash

#python testJosPlot.py
for f in *.eps
do
  epstopdf $f
done
cp *.pdf /data/code/svn/masterRepo/Thesis/vectorGraphics
