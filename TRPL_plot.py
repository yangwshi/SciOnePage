# -*- coding: utf-8 -*-
"""
@author: Yangwei Shi/GingerLab
stretch_exp_fit function is from Margherita/GingerLab
"""
# import package
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def TRPL(filePath = '',fileName = '', columns = [], color = [],FigName=[],xlim = [0,800],ylim =[0.01,1.1],offset=0):
    """
    Keywords input--
    filePath: paste the file path here, string format
    fileName: the file name including the extension.
    Columns: string, the sample names, will be used as the labels as well
    color: specify the colors for each trace
    FigNmae: Figure name
    xlim: x-axis range
    ylim: y-axis range
    offset: shift the PL spectra so that it starts from zero
    """
    df = pd.read_csv(filePath+fileName)
    df.columns = columns
    color = color
    FigName = FigName
    xlim = xlim
    ylim=ylim
    offset = offset
    # font parameters
    font={
          'weight' : 'bold',
          'size' : 22}
    mpl.rc('font',**font)
    # plot
    fig,axs = plt.subplots(figsize=(8.8,6.6))
    plt.yscale('log')
    plt.xlim(xlim)
    plt.ylim(ylim)
    axs.set_xlabel('Time (ns)',fontsize=22,fontweight='bold')
    axs.set_ylabel("Intensity (norm.)",fontsize=22,fontweight='bold')
    for axis in ['top','bottom','left','right']:
        axs.spines[axis].set_linewidth(3)
        axs.tick_params(direction='out',which='both',width=3,length=7)
    for i in range(len(columns)-1):
        plt.plot(df[columns[0]]-offset, df[columns[i+1]]/df[columns[i+1]].max(), lw=3,color = color[i],label=columns[i+1])
    plt.legend(frameon=False)
    plt.savefig(filePath+FigName, bbox_inches='tight', dpi=300)


# stretch_exp_fit function
from scipy.optimize import differential_evolution
from scipy.special import gamma

def stretch_exp_fit(TRPL, t, Tc = (0,1e4*1e-9), Beta = (0,1), A = (0,1.5)):

    def exp_stretch(t, tc, beta, a):
        return ((a * np.exp(-((1.0 / tc) * t) ** beta)))

    def avg_tau_from_exp_stretch(tc, beta):
        return (tc / beta) * gamma(1.0 / beta)

    def Diff_Ev_Fit_SE(TRPL):

        def residuals(params):#params are the parameters to be adjusted by differential evolution or leastsq, interp is the data to compare to the model.
            #Variable Rates
            tc = params[0]
            beta = params[1]
            a = params[2]


            PL_sim = exp_stretch(t,tc,beta,a)

            Resid= (np.sum(((PL_sim-TRPL)**2)/(np.sqrt(PL_sim)**2)))
            return Resid #returns the difference between the PL data and simulated data

        bounds = [Tc, Beta, A]

        result = differential_evolution(residuals, bounds)
        return result.x

    p = Diff_Ev_Fit_SE(TRPL)

    tc = p[0]
    beta = p[1]
    a = p[2]


    PL_fit = exp_stretch(t,tc,beta,a)

    avg_tau = avg_tau_from_exp_stretch(tc,beta)

    return tc, beta, a, avg_tau, PL_fit



def TRPL_fitting(filePath = '',fileName = '', columns = [], color = [],FigName=[],xlim = [0,800],ylim =[0.01,1.1],offset=0):
    """
    Keywords input--
    filePath: paste the file path here, string format
    fileName: the file name including the extension.
    Columns: string, the sample names, will be used as the labels as well
    color: specify the colors for each trace
    FigNmae: Figure name
    xlim: x-axis range
    ylim: y-axis range
    offset: shift the PL spectra so that it starts from zero
    """
    df = pd.read_csv(filePath+fileName)
    df.columns = columns
    color = color
    FigName = FigName
    xlim = xlim
    ylim = ylim
    offset = offset
    # font parameters
    font={
          'weight' : 'bold',
          'size' : 22}
    mpl.rc('font',**font)
    
    
    for i in range(len(columns)-1):
        stretched=stretch_exp_fit((df[columns[i+1]].values)/np.max(df[columns[i+1]].values), df[columns[0]].values*1e-9,\
                               Tc = (0,500*1e-9), Beta = (0.3,1), A = (0.99,1))
        print('This is sample--',columns[i+1])
        print("tau_c (ns) = "+str(stretched[0]*1e9))
        print("Beta = "+str(stretched[1]))
        print("avg. tau (ns) = "+str(stretched[3]*1e9))
        #plotting
        fig,axs = plt.subplots(figsize=(8,6))
        plt.plot(df[columns[0]]-38, (df[columns[i+1]])/df[columns[i+1]].max(), lw=1.5,color = color[i],label=columns[i+1])
        plt.plot(df[columns[0]], stretched[4], 'k--', lw = 2.5)
        plt.yscale('log')
        plt.xlim([0,500])
        axs.set_xlabel('Time (ns)',fontsize=22,fontweight='bold')
        axs.set_ylabel("Intensity (norm.)",fontsize=22,fontweight='bold')
        for axis in ['top','bottom','left','right']:
            axs.spines[axis].set_linewidth(3)
            axs.tick_params(direction='out',which='both',width=3,length=7)
            plt.legend(frameon=False)
            plt.show()  



     
