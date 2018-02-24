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
    ys2 =[]


    for line in lines:
        if len(line) > 0:
            x, y0, y1 = line.split(',')

        xs.append(x)
        ys.append((float(y0), float(y1)))
        #ys2.append((float(y0)*.1))

    print("max", max(y0), max(y1), max (x))

    #print (ys2)
    ticks = numpy.arange(0, 1200.0, 100)
    print (ticks)

    plt.plot(ys)
    ymin, ymax = plt.ylim()

    print("ylim", ymin, ymax)
    plt.yscale('linear')
    plt.ylabel('Volts(V)')
    plt.xlabel('Sample Num')
    plt.title("Bench Tool 0.001")
    plt.autoscale(tight=True)
    plt.grid()
    plt.tight_layout()

    ticklabel=[]

    for tick in ticks:
        ticklabel.append(tick/1000 * 3.3)

    print (ticklabel)

    #Temp  plt.yticks(ticks, ticklabel)
    #plt.yticks(ticks)
    #plt.ylim(0 , 4.0)
    #plt.minorticks_off()
    #l, = plt.plot(')

    #plt.xticks(xs[0:30], xs[0:30])

    #l, = plt.plot(xs, ys, lw=2, color='red')

    #plt.axis([0, 1, -10, 10])
    plt.show()

