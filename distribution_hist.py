import random
from  matplotlib import pyplot as plt
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
import numpy as np
plotly.tools.set_credentials_file(username='tagineer', api_key='tq8PSmjOREsCupCDC09S')

def para_hist(distrib, label, name):
    """
    Usage:
    distrib_histogram(distrib, label, name)
    Argument:
        Distrib: a list of feature.
        Label: a list of labels.
        Name: a string as title of this plot.
    Return:
        A URL on `https://plot.ly`.
    """
    plt.style.use('seaborn-deep')
    bins = np.linspace(-1, 1, 20)
    data = np.vstack(distrib).T
    plt.hist(data, bins, label=label)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    fig = plt.gcf()
    fig.savefig(name + ".pdf")
    plot_url = py.plot_mpl(fig, filename = name)
    return plot_url


def overlap_hist(distrib, label, name):
    """
    Usage:
    overlap_hist(distrib, label, name)
    Argument:
        Distrib: a list of features.
        Label: a list of labels.
        Name: a string as title of the plot.
    Return:
        A pdf was saved.
        A URL on `https://plot.ly`.
    """
    plt.style.use('seaborn-deep')
    bins = np.linspace(-1, 1, 100)
    for idx, i in enumerate(distrib):
        plt.hist(i, bins, alpha=0.5, label=label[idx])
    plt.legend(loc = "upper right")
    plt.title(name)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    fig = plt.gcf()
    fig.savefig(name + ".pdf")
    plot_url = py.plot_mpl(fig, filename = name)
    return plot_url

if __name__ == "__main__":
    x = [random.gauss(0,1) for _ in range(2550)]
    y = [random.gauss(0,1) for _ in range(2550)]
    z = [random.gauss(0,1) for _ in range(2550)]
    print para_hist([x, y, z], ['x', 'y', 'z'], "Test")
    print overlap_hist([x, y, z], ['Domain1', 'Adapted1->2', 'Domain2'], "Feature Distribution")
