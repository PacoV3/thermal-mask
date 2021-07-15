import numpy as np
import matplotlib.pyplot as plt

def two_scales(ax1, time, data1, data2, c1, c2):
    ax2 = ax1.twinx()
    ax1.plot(time, data1, color=c1)
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('exp')
    ax2.plot(time, data2, color=c2)
    ax2.set_ylabel('sin')
    return ax1, ax2

# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
s1 = np.exp(t)
s2 = np.sin(2 * np.pi * t)

# Create axes
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,4))

loss, = ax1.plot([1, 2, 3], [10,15,20])
loss.set_label('loss')
loss_t, = ax1.plot([1, 2, 3], [-10,135,-20])
loss_t.set_label('val_loss')
ax1.legend()
ax1.set_title("Training Loss")
ax1.set_xlabel("Epoch #")
ax1.set_ylabel("Loss")

plt.savefig('a')