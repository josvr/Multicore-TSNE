#!/usr/bin/python3
import matplotlib
matplotlib.use('Agg')
import pandas as pd

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import matplotlib.font_manager as fm
from matplotlib import rc

plot1_color='#e41a1c'
plot2_color='#377eb8'
axis_color='#435470'
hist_grid_color='#f0f0f0'

legend_location = 4
if sys.argv[1].find('4158D') != -1:
  legend_location = 3
 
inp = pd.read_csv(sys.argv[1],sep=' ',skiprows=1,header=None,names=['x','y','z'])
nonBotnet = inp.query('z==0')
botnet = inp.query('z==1')
sns.set_style("whitegrid", {'axes.grid' : False,'axes.edgecolor':axis_color})

# START FONT SETTINGS
rc('font', family='sans serif')
rc('text', usetex=True)
rc('text.latex',preamble=r'\usepackage[variant=b]{fedraserif}')
# END FONT SETTINGS

p = sns.jointplot(x = nonBotnet['x'],y = nonBotnet['y'],label="Non botnet",marginal_kws=dict(bins=22, rug=False),linewidth=1,edgecolor='black',color=plot1_color,alpha=0.3,stat_func=None)
p.set_axis_labels("", "")
p.x = botnet['x']
p.y = botnet['y']
p = p.plot_joint(
plt.scatter,label="Botnet",edgecolor='black',linewidth=1,color=plot2_color,alpha=0.3
)
p.ax_marg_x.hist(
botnet['x'],
22,
color=plot2_color,
alpha = 0.3
)
p.ax_marg_y.hist(
botnet['y'],
22,
color=plot2_color,
orientation = 'horizontal',
alpha = 0.3
)
plt.setp(p.ax_marg_x.yaxis.get_majorticklines(), visible=True)
plt.setp(p.ax_marg_x.yaxis.get_minorticklines(), visible=False)
plt.setp(p.ax_marg_y.xaxis.get_majorticklines(), visible=True)
plt.setp(p.ax_marg_y.xaxis.get_minorticklines(), visible=False)
plt.setp(p.ax_marg_x.get_yticklabels(),fontsize=7)
plt.setp(p.ax_marg_y.get_xticklabels(),fontsize=7)
p.ax_marg_x.yaxis.grid(True,color=hist_grid_color)
p.ax_marg_y.xaxis.grid(True,color=hist_grid_color)

plt.setp(p.ax_joint.get_xticklabels(), visible=False)
plt.setp(p.ax_joint.get_yticklabels(), visible=False)
plt.setp(p.ax_marg_x.get_yticklabels(), visible=True)
plt.setp(p.ax_marg_y.get_xticklabels(), visible=True)
plt.setp(p.ax_marg_y.get_xticklabels(), rotation=270)
legend = plt.legend(loc=legend_location,frameon=True)
legend.get_frame().set_edgecolor(axis_color)
plt.savefig(sys.argv[2],format='pdf',bbox_inches='tight',transparant=True)
