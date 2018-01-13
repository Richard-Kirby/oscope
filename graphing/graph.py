import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def animate(i):
    graph_data = open('oscope.csv','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []

    min = input("First sample to display")
    max = input("Last sample to display")

    if min == '':
        print("Set first sample to 0")
        min = 0
    if max == '':
        max = 0
        print("Set Last Sample to last sample in file")

    sample = 0
    for line in lines:
        if sample > int(min) and (sample < int(max) or int(max) == 0):
            if len(line) > 1:
                x, y0, y1 = line.split(',')
                xs.append(x)
                ys.append((y0, y1))
        elif sample > int(max):
            break
        sample +=1
    ax1.clear()
    ax1.plot(xs, ys)

def start_graph():
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

