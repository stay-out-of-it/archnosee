import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from math import *


master = Tk()
for i in range(5):
    Label(master, text="x={}, y=".format(i)).grid(row=i)
    e = Entry(master)
    e.grid(row=i, column=1)


    print(e.get())

mainloop( )
print(e.get())
x = [1, 2, 3, 4, 5]
y = [1, 2, 2, 4, 3]
i = 1


def inputs(y, i):
    c = input("Write y{}(x={}):".format(i, i))
    if c.isdigit():
        y += [int(c)]
        i += 1
    else:
        print("Incorrect data")
        return inputs(i)

'''
for i in x:
    inputs(y, i)
'''

plt.scatter(x, y)

def mnk(d):
    plt.scatter(x, y)
    legend = []
    fx = sp.linspace(x[0], x[-1])

    fp, residuals, rank, sv, rcond = sp.polyfit(x, y, d, full=True)
    f = sp.poly1d(fp)
    plt.plot(fx, f(fx), linewidth=2)
    legend.append("Polinom %i" % f.order)

    plt.legend(legend, loc="upper left")
    plt.grid()

mnk(3)

x=np.array(x, dtype=float)
y=np.array(y, dtype=float)
def lagranz(x,y,t):
    z=0
    for j in range(len(y)):
        p1=1; p2=1
        for i in range(len(x)):
            if i==j:
                p1=p1*1; p2=p2*1
            else:
                p1=p1*(t-x[i])
                p2=p2*(x[j]-x[i])
        z=z+y[j]*p1/p2
    return z



xnew=np.linspace(np.min(x),np.max(x),100)
ynew=[lagranz(x,y,i) for i in xnew]
plt.plot(xnew,ynew)


plt.show()
