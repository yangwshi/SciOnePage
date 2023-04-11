# -*- coding: utf-8 -*-
"""
@author: Yangwei Shi/GingerLab
""" 
from igor import binarywave as bw
import matplotlib.pyplot as plt
import matplotlib as mpl

def SKPM_plot(filePath = '', fileName='', scale = 4, cmap='magma', figName='SKPM.png'):
    """
    ---This is for plotting the SKPM image, potential part---
    filePath: complete file path
    fileName: filename without extension as extension .ibw has been attached inside of the code
    cmap = cmap
    scale: image size, i.g. 4um x 4um just type 4, by the way, the defalt pixel in x axis is 256
    figName = figName
    """
    
    font={'weight' : 'bold',
      'size' : 22,
     'family': 'Tahoma'}
    mpl.rc('font',**font)
    
    folder = filePath
    df = bw.load(folder + fileName +'.ibw')
    df_skpm = df['wave']['wData']
    df_potential = df_skpm[:,:,3]
   
    
    fig,axs = plt.subplots(figsize=(8,6))
    plt.imshow(df_potential,cmap=cmap)
    # costimize colobar
    cbar=plt.colorbar()
    cbar.set_label('Potential (V)', rotation=270, fontsize=20, fontweight='bold',labelpad=18) #labelpad=20
    cbar.outline.set_linewidth(3)
    cbar.ax.tick_params(width=3,labelsize=20)
    #plt.clim(0.6,1.1)  # Range
    plt.tight_layout()
    plt.xticks([])
    plt.yticks([])
    
    # draw a scale
    scale = scale # um
    x = [245-256/(scale), 245] # 1 um
    y = [245, 245]
    plt.plot(x, y, color="white", linewidth=6.5)
    
    # change the outline thickness
    for axis in ['top','bottom','left','right']:
        axs.spines[axis].set_linewidth(3)
        axs.tick_params(direction='in',width=3,length=6)
    plt.tight_layout()
    # save figure
    plt.savefig(folder + figName, bbox_inches='tight', dpi=300)
    
    
    
    
    
    
    
    
    
    