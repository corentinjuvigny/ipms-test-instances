#!/usr/bin/python3

import sys
import pathlib
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def getLinesMax(mat):
    ret = 0
    for line in mat:
        if ret < len(line):
            ret = len(line)
    return ret

def correctingLines(mat):
    maxLine = getLinesMax(mat)
    for line in mat:
        length = len(line)
        lastValue = line[-1]
        for i in range(len(line),maxLine):
            line.append(lastValue)
    return mat,maxLine

def retrieve_values(instance_directory):
    for directory in pathlib.Path(instance_directory).iterdir():
        if directory.name == "fitness" and directory.is_dir():
            mat = []
            for fitnessFile in directory.iterdir():
                if "fitness" in fitnessFile.name:
                    with open(fitnessFile.absolute(),"r") as f:
                        l = []
                        for line in f.readlines():
                            l.append(float(line))
                        mat.append(l)
            return correctingLines(mat)

def get_best_and_mean_values(data):
    l = []
    for e in data:
        l.append(e[-1])
    best = min(l)
    mean = stats.mean(l)
    sd = stats.stdev(l)
    return best, mean , sd

            
@ticker.FuncFormatter
def major_formatter(x, pos):
    if x % 10 == 0:
        return "%d" % x
    return ""

if __name__ == '__main__':
    instance_directory = sys.argv[1]
    span = 1
    unit = 'm'
    if len(sys.argv) >= 4:
        unit = sys.argv[2]
        span = int(sys.argv[3])

    data, nbrLines = retrieve_values(instance_directory)
    #t = np.linspace(0,20*(nbrLines+1),nbrLines+1)
    t = []
    for i in range(0,nbrLines+1):
        t.append(span*i)
    fig, ax = plt.subplots()
    t = np.arange(0,span*(nbrLines+1),span)
    ax.set_xlabel('time (' + unit + ')')
    ax.set_ylabel('fitness')
    ax.set_title(sys.argv[4] if len(sys.argv) > 4 else sys.argv[1])
    l = []
    for j in range(nbrLines):
        moy = 0.0
        for i in range(len(data)):
            moy += data[i][j]
        l.append(moy / len(data))
    ax.stairs(l,edges=t,baseline=None,color='lightgreen',linestyle='-',linewidth=3,label='Mean graph')
    #ax.plot(tbis,l,linestyle='-')

    #for curve in data:
        #ax.plot(t,curve,linestyle='--')
        #ax.stairs(curve,edges=t,baseline=None,linestyle='--')

    mat = np.matrix(data)

    ax.boxplot(mat,positions=t[:-1],widths=0.5)

    ax.xaxis.set_major_formatter(major_formatter)
    ax.legend()

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    best, mean, sd = get_best_and_mean_values(data)
    greedy = data[0][0]
    best_gain = ((best - greedy) / greedy) * 100
    mean_gain = ((mean - greedy) / greedy) * 100
    print("greedy : {:.2E}, best : {:.2E}, best_gain : {:.4}, mean : {:.2E}, mean_gain : {:.4}, standard deviation : {:.4}, time : {}".format(greedy,best,best_gain,mean,mean_gain,sd,len(data[0])))
    plt.show()