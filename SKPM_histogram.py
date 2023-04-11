from igor import binarywave as bw
import matplotlib.pyplot as plt
import matplotlib as mpl

def SKPM_histogram(filePath='',fileNames=[],labels = [], traceColors=['C0','C1','C2'],binSize = 20,figName = 'SKPM_histogram.png'):
    """
    ---This is for plotting the SKPM image, potential part---
    filePath: complete file path
    fileNames: filename without extension, ['a','b','c']
    labels = []
    traceColors = traceColors
    figName = figName
    binSize = 20, default
    """
    font={'weight' : 'bold',
      'size' : 22,
     'family': 'Tahoma'}
    mpl.rc('font',**font)

    folder = filePath
    fileNames = fileNames
    labels = labels
    traceColors = traceColors
    binSize = binSize
    df = []
    for i in range(len(fileNames)):
        potential = bw.load(folder + fileNames[i] +'.ibw')
        df_skpm = potential['wave']['wData']
        df_potential = df_skpm[:,:,3]
        Potential = df_potential.flatten()
        df.append(Potential)
        
    
    
    fig,axs = plt.subplots(figsize=(8,6))
    axs.set_xlabel('Work function (eV)',fontsize=22,fontweight='bold')
    axs.set_ylabel("Pixel (a.u.)",fontsize=22,fontweight='bold')
    axs.set_xlim([4.0,5.2])
    plt.yticks([])
    # plt.axhline(y=0,linestyle='-',color='black',linewidth=2.5)
    plt.ticklabel_format(axis='y', style='sci', scilimits=(4,4))     
    for axis in ['top','bottom','left','right']:
        axs.spines[axis].set_linewidth(3)
        axs.tick_params(direction='in',width=2.5,length=7)
        
    for j in range(len(df)):
        axs.hist(df[j],bins=binSize,color=traceColors[j],label=labels[j],alpha=1) # purple #270b52
    plt.legend()
    plt.tight_layout()
    plt.savefig(folder + figName, bbox_inches='tight', dpi=300)