import matplotlib

matplotlib.use('Qt5Agg')
#matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt


def two_scales(ax1, time, data1, data2, c1, c2):
    """

    Parameters
    ----------
    ax : axis
        Axis to put two scales on

    time : array-like
        x-axis values for both datasets

    data1: array-like
        Data for left hand scale

    data2 : array-like
        Data for right hand scale

    c1 : color
        Color for line 1

    c2 : color
        Color for line 2

    Returns
    -------
    ax : axis
        Original axis
    ax2 : axis
        New twin axis
    """
    ax2 = ax1.twinx()

    data_list1, data_list2 = zip(*data1)
    ax1.plot(time, data_list1, 'm')
    ax1.plot(time, data_list2, 'r')

    ax1.set_xlabel('Sample')
    ax1.set_ylabel('Analogue')

    data_list1, data_list2 = zip(*data2)
    ax2.plot(time, data_list1, 'b')
    ax2.plot(time, data_list2, 'c')

#    ax2.plot(time, data2)

    ax2.set_ylabel('Digital')
    return ax1, ax2

#start of old code.
'''
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
    dig = []

    for line in lines:
        if len(line) > 0:
            x, y0, y1, dig0, dig1 = line.split(',')

        xs.append(x)
        ys.append((float(y0), float(y1), float(dig0), float(dig1)))

    fig = plt.figure("Pi Bench Tool", figsize=(8, 3.6))
    plt.subplot(111)
    plt.plot(ys)

    plt.ylabel('Volts(V)')
    plt.xlabel('Sample Num')
    plt.title("Bench Tool 00.00.01")
    # plt.autoscale(tight=True)
    plt.grid()
    plt.tight_layout()

    
    axcolor = 'lightgoldenrodyellow'
    axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
    axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
    f0 = 15
    a0 = 7.5
    sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0)
    samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)
    sfreq.on_changed(update)
    samp.on_changed(update)
    

    plt.show()
# End of old code. 
'''

# Get the data
graph_data = open('/home/pi/oscope/oscope.csv', 'r').read()

if graph_data is None:
    print("Nothing found")

# print (graph_data)

lines = graph_data.split('\n')
xs = []
ys = []
dig = []

for line in lines:
    if len(line) > 0:
        x, y0, y1, dig0, dig1 = line.split(',')

    xs.append(int(x))
    ys.append((float(y0), float(y1)))
    dig.append((float(dig0), float(dig1)))

#fig = plt.figure("Pi Bench Tool", figsize=(8, 3.6))
#plt.subplot(111)
#plt.plot(ys)

#plt.ylabel('Volts(V)')
#plt.xlabel('Sample Num')
#plt.title("Bench Tool 00.00.01")
# plt.autoscale(tight=True)
#plt.grid()
#plt.tight_layout()


# Create axes
fig, ax = plt.subplots(num="Pi Bench Tool", figsize=(8,3.6))
ax1, ax2 = two_scales(ax, xs, ys, dig, 'r', 'b')

# Change color of each axis
def color_y_axis(ax, color):
    """Color your axes."""
    for t in ax.get_yticklabels():
        t.set_color(color)

    return None

color_y_axis(ax1, 'r')
color_y_axis(ax2, 'b')
plt.tight_layout()
plt.show()