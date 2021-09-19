# -*- coding: utf-8 -*-
"""
Spyder Editor


"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

plt.style.use('ggplot')


def Colors():
    return ['r','b', 'g', 'c', 'm', 'y','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
def lines():
    return  ['-', '--', '-.', ':']
def markers():
    return ['.','^','o','s','+','x','D']

def line_plot(x,y_list,names,xlim,ylim,xlabel,ylabel,figname,save_path,markers=False,linestyle=False):
    #set path and init figure
    path=save_path+'\\'+figname+'.png'
    fig,ax=plt.subplots(figsize=(10,10))
    
    #loop to plot all series
    i=0
    for y in y_list:
        #set colors,lines, and marker
        colors=Colors()
        if markers:
            marker_list=markers()
            marker=marker_list[i]
        else:
            marker=None
        if linestyle:
            linestyle_list=lines()
            linestyle=linestyle_list[i]
        else:
            linestyle=None
        ax.plot(x,y,color=colors[i],marker=marker,linestyle=linestyle,label=names[i])
        i+=1
        
    #ticks
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(axis='both', which='minor',length=3)
    ax.tick_params(axis='both', which='major',length=4)
    #axes labels
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    #lines at 0
    ax.axhline(color='k')
    ax.axvline(color='k')
    #legend
    ax.legend(loc='upper right')
    #limits
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    #title and save
    ax.set_title(figname)
    fig.savefig(path)
    
    # plt.show()
    return None

if __name__=='__main__':


    #Test cases, simple curve plots
    x=np.arange(-100,100,.1)
    y1=x
    y2=x**2
    y3=np.sin(5*x)
    y4=np.cos(x)*np.sin(x)**2
    xlim=[-5,5]
    ylim=[-5,5]
    ylabel='y'
    xlabel='x'
    figname='Test'
    save_path=r'C:\Users\hafee\Desktop'
    y_list=[y1,y2,y3,y4]
    names=['Line','Quadratic','Sin(5x)','Sin(x)*Cos(x)']
    line_plot(x,y_list,names,xlim,ylim,xlabel,ylabel,figname,save_path)
    
    # #cardioid curve
    # t=np.arange(-100,100,.1)
    # x=16*np.sin(t)**3
    # y_card=13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)

    # xlim=[-20,20]
    # ylim=[-20,20]
    # ylabel='y'
    # xlabel='x'
    # figname='Cardioid Curve'
    # save_path=r'C:\Users\hafee\Desktop'
    # y_list=[y_card]
    # names=[figname]
    # line_plot(x,y_list,names,xlim,ylim,xlabel,ylabel,figname,save_path)
    