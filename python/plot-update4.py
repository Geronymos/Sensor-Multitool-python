import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 6*np.pi, 100)
# y = np.sin(x)
y = [1]

# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
# line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma
line1, = ax.plot(y, 'r-') # Returns a tuple of line objects, thus the comma

# for phase in np.linspace(0, 10*np.pi, 500):
for phase in range(100):
    # line1.set_ydata(np.sin(x + phase))
    y.append(phase)
    line1.set_ydata(y)
    fig.canvas.draw()
    fig.canvas.flush_events()