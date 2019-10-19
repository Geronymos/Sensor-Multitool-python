import numpy as np
import matplotlib.pyplot as plt
import serial
import serial.tools.list_ports
import re


# plt.show()
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)

plots = []
counter = 0

serialDevices = serial.tools.list_ports.comports()
print("Devices: ")

for device in serialDevices:
    print(device)
    # print(device.device)

    with serial.Serial(device.device, 9600, timeout=1) as ser:
        while True:
            # x = ser.read()          # read one byte
            s = ser.read(1000)        # read up to ten bytes (timeout)
            # line = ser.readlines()   # read a '\n' terminated line
            values = re.findall("\d+[.,]?\d+", s.decode())
            floatVals = [float(value) for value in values]
            print( floatVals )

            # IF THERE ARE NOT ENOUGH PLOTS FOR EVERY VALUE: MAKE MORE PLOTS!
            while( len(floatVals) > len( plots ) ):
                newPlot, = ax.plot([], [])
                plots.append( newPlot )

            if( len(floatVals) > 0 ):

                print( "plots", plots )
                counter += 1
                
                for i in range(len(floatVals)):
                    # newPlot.set_ydata( range( counter ) )
                    plots[i].set_ydata( np.append(plots[i].get_ydata(), floatVals[i]) )
                    plots[i].set_xdata( range( counter ) )
                
                ax.relim()
                ax.autoscale_view()
 
                fig.canvas.draw()
                fig.canvas.flush_events()
                # plt.draw()
                # plt.pause(0.1)

            print(s.decode())
 
# add this if you don't want the window to disappear at the end
# plt.show()