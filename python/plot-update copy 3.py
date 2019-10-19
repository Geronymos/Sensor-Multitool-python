import matplotlib.pyplot as plt
import time
import random
 
xdata = []
 
plt.show()
 
axes = plt.gca()
line, = axes.plot(xdata, 'r-')
 
for i in range(100):
    xdata.append(i)
    axes.plot(xdata, 'r-')
    plt.draw()
    # plt.pause(1e-17)
    plt.pause(0.1)
    # time.sleep(0.1)
 
# add this if you don't want the window to disappear at the end
plt.show()