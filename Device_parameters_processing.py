# -*- coding: utf-8 -*-
"""
@author: Yangwei Shi/GingerLab
"""

import pandas as pd
from scipy.optimize import fmin, fsolve
from scipy.interpolate import interp1d

def Device_parameters(filePath = '',cells = [], pixels = ['1_scan_0','2_scan_0','3_scan_0','4_scan_0','5_scan_0','6_scan_0','7_scan_0','8_scan_0']):
    """
    ----This function is to recalculate the device paramters (Voc, PCE, FF, Jsc) from JV scans----
    filePath: String
    cells: one substrate is called a cell
    pixels: default is 8
    """
    for i in range(len(cells)):
        Jsc = []
        Voc = []
        FF = []
        PCE = []
        Pixel = []
        # Reverse scan
        for j in range(len(pixels)):
            df = pd.read_csv(filePath+cells[i]+pixels[j]+'.liv1',delimiter = '\t',header = None)
            df[0] = df[0][:-11].astype(float) # df[1] = df[1][:-11].astype(float) 
            jv_interp = interp1d(df[0][:-11], -df[1][:-11], kind="cubic", fill_value="extrapolate") # jsc should be negative
            jsc = (-1)*jv_interp(0) # in mA/cm2
            voc = fsolve(jv_interp, x0=1.1) # x0 is intial guess
            v_mpp = fmin(lambda x: x * jv_interp(x), 0.8*voc, disp=False) # voltage at max power point
            j_mpp = jv_interp(v_mpp)
            ff = -(j_mpp*v_mpp)/(jsc*voc)*100
            pce = (voc * jsc * ff)/ 100
            Jsc.append(jsc)
            FF.append(ff[0])
            Voc.append(voc[0])
            PCE.append(pce[0])
            Pixel.append(Pixel[j][0])
        
        device_performance = pd.DataFrame()
        device_performance['PCE'] = PCE
        device_performance['Voc'] = Voc
        device_performance['FF'] = FF
        device_performance['Jsc'] = Jsc
        device_performance['Pixels']=Pixel
        # forward scan
        Jsc_f = []
        Voc_f = []
        FF_f = []
        PCE_f = []
        for j in range(len(pixels)):
            df = pd.read_csv(filePath+cells[i]+pixels[j]+'.liv2',delimiter = '\t',header = None)
            df[0] = df[0][:-11].astype(float) # df[1] = df[1][:-11].astype(float) 
            jv_interp = interp1d(df[0][:-11], -df[1][:-11], kind="cubic", fill_value="extrapolate") # jsc should be negative
            jsc = (-1)*jv_interp(0) # in mA/cm2
            voc = fsolve(jv_interp, x0=1.1) # x0 is intial guess
            v_mpp = fmin(lambda x: x * jv_interp(x), 0.8*voc, disp=False) # voltage at max power point
            j_mpp = jv_interp(v_mpp)
            ff = -(j_mpp*v_mpp)/(jsc*voc)*100
            pce = (voc * jsc * ff)/ 100
            Jsc_f.append(jsc)
            FF_f.append(ff[0])
            Voc_f.append(voc[0])
            PCE_f.append(pce[0])
            
        device_performance['PCE(F)'] = PCE_f
        device_performance['Voc(F)'] = Voc_f
        device_performance['FF(F)'] = FF_f
        device_performance['Jsc(F)'] = Jsc_f
        device_performance['Hysteresis'] = (device_performance['PCE']-device_performance['PCE(F)'])/device_performance['PCE']
        device_performance = device_performance.round(4) # only have three decimals in the dataframe
        # remember to change the sample name!!!
        device_performance['sample']='OTf_6mM' # this allows you to 
        # save file to csv file
        device_performance.to_csv(filePath+cells[i]+'.csv',index=False) 
