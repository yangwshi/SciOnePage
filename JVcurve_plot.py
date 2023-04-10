# -*- coding: utf-8 -*-
"""
@author: Yangwei Shi/GingerLab
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

def JV_curves(filePath ='', fileNames = [], labels = [], traceColors = ['C0','C1','C2','C3']):
    """
    ----For plotting JV curves----
    filePath: string
    fileNames: list of strings, without extension
    labels:
    traceColors: ['C0','C1','C2','C3'] is the defalt color
    """
    font={
          'weight' : 'bold',
          'size' : 22}
    mpl.rc('font',**font)
    
    curves_reverse = [] # for appending the reverse and forward curves
    curves_forward = []
    for i in range(len(fileNames)):
        df = pd.read_csv(filePath+fileNames[i]+'.liv1',delimiter = '\t',header = None)
        df[0] = df[0][:-11].astype(float)
        df[1] = df[1][:-11]
        curves_reverse.append(df)
    
        df_forward = pd.read_csv(filePath+fileNames[i]++'.liv2',delimiter = '\t',header = None)
        df_forward[0] = df_forward[0][:-11].astype(float)
        df_forward[1] = df_forward[1][:-11]
        curves_forward.append(df_forward)
        
    fig,axs = plt.subplots(figsize=(8.8,6.6))
    axs.set_xlabel('Voltage (V)',fontweight='bold',fontsize=22)
    axs.set_ylabel('Current density (mA/cm$^2$)',fontweight='bold',fontsize=22)
    axs.tick_params(direction='in',width=3,length=6) # show top and right ticks,put top=True, right=True
    axs.set_xlim(0,1.24)
    axs.set_ylim(0,25)
    plt.legend(frameon=False)
    # set axes linewidth
    for axis in ['top','bottom','left','right']:
        axs.spines[axis].set_linewidth(3)
# # Reverse
    for i in range(len(curves_reverse)):
        axs.plot(curves_reverse[1][0],curves_reverse[i][1],'-', lw=3, color= traceColors[i],label =labels[i])# label color lists
        axs.scatter(curves_reverse[1][0],curves_reverse[i][1],s=55, color= traceColors[i])
    # forward scan
        axs.plot(curves_forward[i][0],curves_forward[i][1],'--', lw=3, color= traceColors[i])
        axs.scatter(curves_forward[i][0],curves_forward[i][1],s=55, color= traceColors[i])
    plt.legend()
    plt.tight_layout() 
