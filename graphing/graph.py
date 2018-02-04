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

    ax1.clear()
    ax1.plot(xs, ys)

def start_graph():
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

