import matplotlib

matplotlib.use('Qt5Agg')
#matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy

#style.use('fivethirtyeight')


def start_graph():

    graph_data = open('/home/pi/oscope/oscope.csv', 'r').read()

    if graph_data is None:
        print("Nothing found")

    # print (graph_data)

    lines = graph_data.split('\n')
    xs = []
    ys = []
    dig =[]


    for line in lines:
        if len(line) > 0:
            x, y0, y1, dig0, dig1 = line.split(',')

        xs.append(x)
        ys.append((float(y0), float(y1), float(dig0),float (dig1) ))

    plt.figure("Pi Bench Tool")
    plt.subplot(111)
    plt.plot(ys)

    plt.ylabel('Volts(V)')
    plt.xlabel('Sample Num')
    plt.title("Bench Tool 00.00.01")
    #plt.autoscale(tight=True)
    plt.grid()
    plt.tight_layout()

    plt.show()


'''  
    plt.plot(ys)
    yminvar, ymaxvar = plt.ylim()


    print("ylim", yminvar, ymaxvar)
    plt.yscale('linear')
    plt.ylim(ymin=-1.5)

    #ticklabel=[]

    #for tick in ticks:
    #   ticklabel.append(tick/1000 * 3.3)

    #print (ticklabel)

    #Temp  plt.yticks(ticks, ticklabel)
    #plt.yticks(ticks)
    #plt.ylim(0 , 4.0)
    #plt.minorticks_off()
    #l, = plt.plot(')

    #plt.xticks(xs[0:30], xs[0:30])

    #l, = plt.plot(xs, ys, lw=2, color='red')

    #plt.axis([0, 1, -10, 10])
    plt.show()
'''
