import matplotlib.pyplot as plt

import serial.tools.list_ports
import serial
import re

data = []

plt.show()
 
axes = plt.gca()
line, = axes.plot(data, 'r-')

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

            if( len(floatVals) > 0 ):
                while( len(data) < len(floatVals) ):
                    data.append([])
                for i in range(len(floatVals)):
                    data[i]
                    data[i].append( floatVals[i] )
                    # axes.plot(data[i], 'r-')
                    axes.plot(data[i])
                plt.draw()
                plt.pause(0.1)

            print(s.decode())
 
 

 
# for i in range(100):
#     xdata.append(i)
#     axes.plot(xdata, 'r-')
#     plt.draw()
#     # plt.pause(1e-17)
#     plt.pause(0.1)
#     # time.sleep(0.1)
 
# add this if you don't want the window to disappear at the end
plt.show()