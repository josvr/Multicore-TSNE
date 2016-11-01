#!/bin/bash

python testJosPlot.py
epstopdf *.eps
cp *.pdf /data/code/svn/masterRepo/Thesis/vectorGraphics
