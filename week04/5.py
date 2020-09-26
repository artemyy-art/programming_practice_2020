import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
p, v = np.polyfit(x, y, deg=2, cov=True)
d, f = np.polyfit(x, y, deg=1, cov=True)
a= np.arange(1, 5.01, 0.01)
sp = plt.subplot(121)
plt.errorbar(x, y, xerr=max(abs(v[0, 0]), abs(v[1, 0]), abs(v[2, 0])), yerr=max(abs(v[0, 1]), abs(v[1, 1]), abs(v[2, 1])))
m=np.poly1d(p)
plt.plot(a, m(a))
sp = plt.subplot(122)
plt.errorbar(x, y, xerr=max(abs(f[0,0]), abs(f[1, 0])), yerr=max(abs(f[1,1]), abs(f[0,1])))
r=np.poly1d(d)
plt.plot(a, r(a))
plt.show()
