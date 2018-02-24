import matplotlib

#matplotlib.use('Qt5Agg')
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()

def reset(event):
    sfreq.reset()
    samp.reset()

def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()


def start_graph():

    fig, ax = plt.subplots(figsize=(8,3.5))
    plt.subplots_adjust(left=0.25, bottom=0.25)


    graph_data = open('/home/pi/oscope/oscope.csv', 'r').read()

    if graph_data == None:
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
        #print(x)
        ys.append((y1))
        ys2.append((float(y0)*.1))

        #ys.append(y1)
        #print(y0, y1)
    #print(xs)
    print (ys2)

    test = [.1,.2,.3,.4,.5,.6]

    #print(xs[0:100], ys[0:100])

    #plt.xticks(xs[0:30])
    #plt.ylim(0,4)
    plt.plot(ys)

    #l, = plt.plot(')

    #plt.xticks(xs[0:30], xs[0:30])

    #l, = plt.plot(xs, ys, lw=2, color='red')

    #plt.axis([0, 1, -10, 10])
    plt.show()
'''
    axcolor = 'lightgoldenrodyellow'
    axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
    axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

    a0 = 5
    f0 = 3

    sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0)
    samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)

    sfreq.on_changed(update)
    samp.on_changed(update)

    resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

    button.on_clicked(reset)

    rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
    radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)

    radio.on_clicked(colorfunc)
'''
    #plt.show()













'''
import matplotlib

matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')
#plt.ion()

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def animate(i):
    graph_data = open('/home/pi/oscope/oscope.csv','r').read()

    if graph_data == None:
        print("Nothing found")

    #print (graph_data)

    lines = graph_data.split('\n')
    xs = []
    ys = []


#    min = input("First sample to display")
#    max = input("Last sample to display")

#   if min == '':
#      print("Set first sample to 0")
#        min = 0
#    if max == '':
#        max = len(lines)
#        print("Set Last Sample to last sample in file ", max)

#    print (min, max)
    #sample = 0

    #for j in range(int(min), int(max)):
    #    #print (i)
    #   x, y0, y1 = lines[j].split(',')
    #    xs.append(x)
    #    ys.append((y0, y1))


    for line in lines:
        try:
            x, y0, y1 = line.split(',')
        except:
            print("fart ", line)

        xs.append(x)
        print(x)
        ys.append((y0, y1))
        print(y0, y1)

    ax1.clear()
    ax1.plot(xs, ys)

def start_graph():
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

'''
