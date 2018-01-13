# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time

import spidev
import time
import os
import csv


# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1250000


# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data


# Software SPI configuration:
#CLK  = 18
#MISO = 23
#MOSI = 24
#CS   = 25

#mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
#SPI_PORT   = 0
#SPI_DEVICE = 0
#mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
print('-' * 57)

sample_count = 0
samples = []
# Main program loop.
try:

    while True:

        # Read all the ADC channel values in a list.
        values = [0]*8

        #for i in range(8):
        #    # The read_adc function will get the value of the specified channel (0-7).
        #    values[i] = float(mcp.read_adc(i)/1024 *3.3)

        values[0] = float(ReadChannel(0)/1024 *3.3)
        values[1] = float(ReadChannel(1)/1024 *3.3)
        #print (values[0], values[1])

        #print(values[0])

        samples.append((time.time(), values[0], values[1]))
        sample_count +=1


        # print ("{},{:.3f},{:.3f}" .format(time.time(), values[6], values[7]))
        # Print the ADC values.
        #print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
        # Pause for half a second.
        #time.sleep(0.5)

except KeyboardInterrupt:

    spi.close()
    print(sample_count)

    first = samples.pop(0)
    last = samples.pop()

    duration = last[0]-first[0]

    samples_per_sec = float(sample_count/duration)

    print ("First {}, Last {}". format(samples.pop(0), samples.pop()))
    print ("Samples per sec {}" .format(samples_per_sec))


    with open('/home/pi/oscope/oscope.csv', 'w', newline='') as resultfile:

        sample_num = 0

        for sample in samples:
            str = "{}, {:.3f}, {:.3f}\n".format(sample_num, sample[1], sample[2])
            resultfile.write(str)
            sample_num +=1


    #for sample in samples:
    #   print (sample)
