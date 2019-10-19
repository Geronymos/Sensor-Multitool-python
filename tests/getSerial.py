import serial.tools.list_ports
import serial
import re

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
            print( [float(value) for value in values] )

            print(s.decode())

