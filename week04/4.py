import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
with plt.xkcd():
    plt.plot(x, eval(input()))
    plt.show()