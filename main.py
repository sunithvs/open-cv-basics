from scipy.optimize import curve_fit
import math as m
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def fit(a, b, c, d):
    def objective(ss, c0, k):
        return c0 + ss * k

    xnew = np.array((a))
    ynew = np.array((b))
    wnew = np.array((c))
    vnew = np.array((d))
    popt, _ = curve_fit(objective, xnew, ynew)
    a1, b1 = popt
    popt, _ = curve_fit(objective, wnew, vnew)
    c1, d1 = popt
    print('log(ccn) = %.5f + log(ss)* %.5f' % (a1, b1))

    x_line = np.arange(min(xnew), max(xnew), 0.192)
    y_line = objective(x_line, a1, b1)
    wline = np.arange(min(wnew), max(wnew), 0.192)
    vline = objective(wline, c1, d1)

    plt.scatter((xnew), (ynew))
    plt.errorbar((x_line), (y_line), yerr=vline)


time18, height18, pcasp18, ss18, cnnuc18, ccncr18, factor18 = np.loadtxt("20090618_CCN_CORRECTED.txt", skiprows=62,
                                                                         unpack=True)
time19, height19, pcasp19, ss19, cnnuc19, ccncr19, factor19 = np.loadtxt("20090620_CCN_CORRECTED.txt", skiprows=62,
                                                                         unpack=True)
time20, height20, pcasp20, ss20, cnnuc20, ccncr20, factor20 = np.loadtxt("20090622_CCN_CORRECTED.txt", skiprows=62,
                                                                         unpack=True)

ccn18 = []
ssn18 = []
for i in range(len(height18)):
    if 2200 <= height18[i] <= 2400:
        ccn18.append(ccncr18[i])
        ssn18.append(ss18[i])

ccn18 = np.log(ccn18)
ssn18 = np.log(ssn18)
data1 = {'ssn18': ssn18, 'ccn18': ccn18}
df1 = pd.DataFrame(data1)
x1 = df1.groupby("ssn18")["ccn18"].mean().reset_index()
y1 = df1.groupby("ssn18")["ccn18"].std().reset_index()

fit(x1["ssn18"], x1["ccn18"], y1["ssn18"], y1["ccn18"])

ccn19 = []
ssn19 = []
for i in range(len(height19)):
    if 1800 <= height19[i] <= 2000:
        ccn19.append(ccncr19[i])
        ssn19.append(ss19[i])

ccn19 = np.log(ccn19)
ssn19 = np.log(ssn19)
data2 = {'ssn19': ssn19, 'ccn19': ccn19}
df2 = pd.DataFrame(data2)
x2 = df2.groupby("ssn19")["ccn19"].mean().reset_index()
y2 = df2.groupby("ssn19")["ccn19"].std().reset_index()

fit(x2["ssn19"], x2["ccn19"], y2["ssn19"], y2["ccn19"])

ccn20 = []
ssn20 = []
for i in range(len(height20)):
    if 1900 <= height20[i] <= 2100:
        ccn20.append(ccncr20[i])
        ssn20.append(ss20[i])

ccn20 = np.log(ccn20)
ssn20 = np.log(ssn20)
data3 = {'ssn20': ssn20, 'ccn20': ccn20}
df3 = pd.DataFrame(data3)
x3 = df3.groupby("ssn20")["ccn20"].mean().reset_index()
y3 = df3.groupby("ssn20")["ccn20"].std().reset_index()

fit(x3["ssn20"], x3["ccn20"], y3["ssn20"], y3["ccn20"])
plt.show()