# -*- coding: utf-8 -*-
"""
General histogram creation file, matplotlib, numpy
"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')


def Colors():
    return ['r','b', 'g', 'c', 'm', 'y','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
def lines():
    return  ['-', '--', '-.', ':']
def markers():
    return ['.','^','o','s','+','x','D']

def histogram(x_list,names,xlabel,ylabel,figname,save_path,bins=None,density=False,alpha=0.5,linestyle='-'):
    '''
    x_list = list of n x 1 arrays to plot
    names = names in list order
    xlabel, ylabel = axis labels
    figname = figure labels
    save_path = dir to save plot, if None plot will display
    '''
    fig,ax=plt.subplots(figsize=(10,10))
    
    #loop to plot all series
    i=0
    for x in x_list:
        #set colors,lines, and marker
        colors=Colors()
        ax.hist(x,color=colors[i],bins=bins,label=names[i],alpha=alpha,ls=linestyle)
        ax.axvline(np.mean(x),color=colors[i],linestyle='--',lw=2)
        i+=1
        
    #ticks
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(axis='both', which='minor',length=3)
    ax.tick_params(axis='both', which='major',length=4)
    #axes labels
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    #legend
    ax.legend(loc='upper right')
    #title and save
    ax.set_title(figname)
    
    if save_path==None:
        plt.show()
    else:
        path=save_path+'\\'+figname+'.png'
        fig.savefig(path)
    
        plt.show()
    return None

if __name__=='__main__':
    '''
    Test Run on random data
    '''
    data=np.random.randint(0, 1000, 100)
    x_list=[data]
    xlabel='x'
    ylabel='counts'
    figname='Test Histogram'
    save_path=None
    names=['Data']
    histogram(x_list,names,xlabel,ylabel,figname,save_path,bins=None)

    
