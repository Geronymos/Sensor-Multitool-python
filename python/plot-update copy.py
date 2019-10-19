import matplotlib.pyplot as plt
import time
import random
 
ysample = random.sample(range(-50, 50), 100)
 
xdata = []
ydata = []
 
plt.show()
 
axes = plt.gca()
line, = axes.plot(xdata, ydata, 'r-')
 
for i in range(100):
    xdata.append(i)
    ydata.append(i*2)
    axes.plot(xdata, ydata, 'r-')
    plt.draw()
    # plt.pause(1e-17)
    plt.pause(0.1)
    # time.sleep(0.1)
 
# add this if you don't want the window to disappear at the end
plt.show()