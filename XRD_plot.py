# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

"""
write a function for plotting UV-vis and XRD patterns

"""

def XRD_plot(filePath = '',fileNames = [], labels = [], traceColors = ['C0','C1','C2','C3'], Norm = 'norm', FigName='XRD', xaixsRange = [5,75]):
    """
    ---This function is used to plot the XRD spectra of mutiple samples---
    --KeyWords include the following items--
    1. filePath:--copy the full file path here. 
    2. fileNames: Can specify what you would like to call it
    3. labels: labels for all the xrd files, the sequence should be correct
    4. traceColors: defalt value is ['C0','C1','C2','C3']
    5. Norm = Norm, defalt value is 'norm'. if not specify, will consider as not normalized
    6. xaixsRange: the range of x axis, default value is [5,75]
    """
    folder = filePath
    fileNames = fileNames
    labels = labels
    traceColors = traceColors
    Norm = Norm
    FigName = FigName
    xaixsRange = xaixsRange
    
    font={'weight' : 'bold',
      'size' : 22,
     'family': 'Tahoma'}
# can also add font family into the dic: 'family': 'Tahoma' 
    mpl.rc('font',**font)
    
    data = []
    gaps = [0, 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1]
    if Norm =='norm':
        for i in range(len(fileNames)):
            df = pd.read_csv(folder+fileNames[i], sep='\s+',header=None,index_col=False)
            df = df.drop(0)
            df[0] = df[0].astype(float)
            df[1] = df[1]/df[1].max()
            data.append(df[[0,1]])
            
        fig,axs = plt.subplots(figsize=(8.8,6.6))
        axs.set_xlim(xaixsRange)
        plt.yticks([]) # hide y axis values
        axs.set_xlabel('2\u03B8 (\u00B0)',fontweight='bold',fontsize=22) # 2 theta, degree
        axs.set_ylabel('Intensity (a.u.)',fontweight='bold',fontsize=22)
        axs.tick_params(direction='in',width=3,length=6)
        for axis in ['top','bottom','left','right']:
                axs.spines[axis].set_linewidth(3)
        for j in range(len(fileNames)):
            axs.plot(data[j][0], data[j][1]+gaps[j],lw=3,label=labels[j],color = traceColors[j])
        plt.legend(frameon=False,loc='upper right')
        plt.savefig(folder+FigName,bbox_inches='tight', dpi=300)     
    else:
        for i in range(len(fileNames)):
            data_0 = pd.read_csv(folder+fileNames[i], sep='\s+',header=None,index_col=False)
            data_0 = data_0.drop(0)
            data_0[0] = data_0[0].astype(float)
            data.append(data_0[[0,1]]) 
