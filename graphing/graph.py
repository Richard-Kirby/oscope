import matplotlib

matplotlib.use('Qt5Agg')
#matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy
from matplotlib.widgets import Slider, Button, RadioButtons

#style.use('fivethirtyeight')
def update(val):
    amp = samp.val
    freq = sfreq.val
    #l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()

def start_graph():

    global samp
    global sfreq
    global fig
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

    fig= plt.figure("Pi Bench Tool", figsize=(8,3.6))
    plt.subplot(111)
    plt.plot(ys)

    plt.ylabel('Volts(V)')
    plt.xlabel('Sample Num')
    plt.title("Bench Tool 00.00.01")
    #plt.autoscale(tight=True)
    plt.grid()
    plt.tight_layout()

    '''
    axcolor = 'lightgoldenrodyellow'
    axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
    axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
    f0 = 15
    a0 = 7.5
    sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0)
    samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)
    sfreq.on_changed(update)
    samp.on_changed(update)
    '''
    
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
