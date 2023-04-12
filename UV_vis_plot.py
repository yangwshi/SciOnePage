# -*- coding: utf-8 -*-
"""
@author: Yangwei Shi/GingerLab
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

"""
write a function for plotting UV-vis

"""

def UV_vis_plot(filePath = '',fileNames = [], labels = [], traceColors = ['C0','C1','C2','C3'], FigName='UV_vis.png', xaixsRange = [500,800]):
    """
    ---This function is used to plot the XRD spectra of mutiple samples---
    --KeyWords include the following items--
    1. filePath:--copy the full file path here. 
    2. fileNames: Can specify what you would like to call it
    3. labels: labels for all the xrd files, the sequence should be correct
    4. traceColors: defalt value is ['C0','C1','C2','C3']
    5. xaixsRange: the range of x axis, default value is [500,800]
    """
    folder = filePath
    fileNames = fileNames
    labels = labels
    traceColors = traceColors
    FigName = FigName
    xaixsRange = xaixsRange
    
    font={'weight' : 'bold',
      'size' : 22,
     'family': 'Tahoma'}
# can also add font family into the dic: 'family': 'Tahoma' 
    mpl.rc('font',**font)
    
    data = []
    for i in range(len(fileNames)):
        df = pd.read_csv(folder+fileNames[i]+'.csv')
        data.append(df)
            
    fig,axs = plt.subplots(figsize=(8.8,6.6))
    axs.set_xlim(xaixsRange)
    plt.yticks([]) # hide y axis values
    axs.set_xlabel('2\u03B8 (\u00B0)',fontweight='bold',fontsize=22) # 2 theta, degree
    axs.set_ylabel('Intensity (a.u.)',fontweight='bold',fontsize=22)
    axs.tick_params(direction='in',width=3,length=6)
    for axis in ['top','bottom','left','right']:
        axs.spines[axis].set_linewidth(3)
    for j in range(len(fileNames)):
        axs.plot(data[j]['Wavelength (nm)'], data[j]['Absorbance (AU)'],lw=3,label=labels[j],color = traceColors[j])
    plt.legend(frameon=False,loc='upper right')
    plt.savefig(folder+FigName,bbox_inches='tight', dpi=300)