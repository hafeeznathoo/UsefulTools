'''
Plotting script

will take in the icu DF's columns, and generate plots as needed


initial - demographic group bar charts
number of passes and fails for the screens

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import plotnine as p9

def BarPlot(df, out_filepath, title):
    labels = df.age_group.unique()
    males = list(df[df['Gender']=='Male'].percent)
    females = list(df[df['Gender']=='Female'].percent)
    # unspecified = list(df[df['Gender']=='Unspecified'].percent)
    
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, males, width, label='Males')
    rects2 = ax.bar(x + width/2, females, width, label='Females')
    # rects3 = ax.bar(x + width/2, unspecified, width, label='Unspecified')
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Proportion')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    
    fig.tight_layout()
    
    plt.show()
    fig.savefig(out_filepath+'\\'+title+'.png')
    
    return None
