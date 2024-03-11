import pandas as pd
import numpy as np

def region(df, vmax, vmin):
    return df[vmax]-df[vmin]
def mean(df, vmax, vmin):
    return (df[vmax]+df[vmin])/2
def total(df, a, b):
    return df[a]+df[b]

def transformacion(df):
    df['X_Region']=region(df, 'X_Maximum', 'X_Minimum')
    df['X_Mean']=mean(df, 'X_Maximum', 'X_Minimum')
    df['Y_Region']=region(df, 'Y_Maximum', 'Y_Minimum')
    df['Y_Mean']=mean(df, 'Y_Maximum', 'Y_Minimum')
    df['Total_Perimeter']= total(df, 'Y_Perimeter', 'X_Perimeter')
    df['Reg_Luminosity']=region(df, 'Maximum_of_Luminosity', 'Minimum_of_Luminosity')
    df['Mean_Luminosity']=mean(df, 'Maximum_of_Luminosity', 'Minimum_of_Luminosity')
    df['Total_Edges']=total(df, 'Edges_X_Index', 'Edges_Y_Index')
    df['Total_Log']=total(df, 'Log_X_Index', 'Log_Y_Index')
    