#!/bin/bash

./tsneJosPlot.py ~/masterRepo/masterRepo/Thesis/data/tsne_4158D-400p.dat /home/josr/masterRepo/masterRepo/Thesis/vectorGraphics/tsne_4158D-400p.pdf
./tsneJosPlot.py ~/masterRepo/masterRepo/Thesis/data/tsne_5000D-400p.dat /home/josr/masterRepo/masterRepo/Thesis/vectorGraphics/tsne_5000D-400p.pdf
./tsneJosPlot.py ~/masterRepo/masterRepo/Thesis/data/tsne_3000D-400p.dat /home/josr/masterRepo/masterRepo/Thesis/vectorGraphics/tsne_3000D-400p.pdf
./tsneJosPlot.py ~/masterRepo/masterRepo/Thesis/data/tsne_1500D-400p.dat /home/josr/masterRepo/masterRepo/Thesis/vectorGraphics/tsne_1500D-400p.pdf
./tsneJosPlot.py ~/masterRepo/masterRepo/Thesis/data/output_2D.dat /home/josr/masterRepo/masterRepo/Thesis/vectorGraphics/tsne_output_2D.pdf

gnome-open /home/josr/masterRepo/masterRepo/Thesis/vectorGraphics/tsne_output_2D.pdf
