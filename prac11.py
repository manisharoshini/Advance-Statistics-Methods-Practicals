# Time series analysis and forecasting

import pandas as pd
import matplotlib.pyplot as plt

listt = [15,21,30,36,42,46,50,56,63,70,74,82,90,102]

df = pd.DataFrame(listt)

temp = df.rolling(window = 3).sum()
temp2 = df.rolling(window = 5).sum()

print(temp)

plt.plot(listt)
plt.plot(temp)
plt.plot(temp2)
plt.show()
##least square method
import matplotlib.pyplot as plt

X_pseudo = [2005,2006,2007,2008,2009,2010,2011] #YEARS

Y = [80,90,92,83,94,99,92] #PRODUCTION

A = 2008 #ASSUMED MEAN

print("Given Years:",X_pseudo)
print("Production:",Y,"TOTAL:",sum(Y))
Y_total = sum(Y)
print("Assumed Mean:",A)

X = [num - A for num in X_pseudo]
print("X:",X,"TOTAL:",sum(X))
##X = sum(X)

XY = [X[i] * Y[i] for i in range(len(X))]
print("XY:",XY,"TOTAL:",sum(XY))
XY = sum(XY)

X2 = [X[i] * X[i] for i in range(len(X))]
print("X2:",X2,"TOTAL:",sum(X2))
X2 = sum(X2)

#CALCULATE A AND B
print("--------------------")
print("FORMULA: a = <Y/N and b = <XY/<X2")

a = Y_total//len(X)
print("a:",a)
b = XY//X2
print("b:",b)
print("Calculating Yc = a + b(x)")

Yc = [a + b * x for x in X]
print(Yc)
plt.plot(X_pseudo,Y)
plt.plot(X_pseudo,Yc)
plt.show()

future = int(input("Enter the Year:"))
x_pred = future - A
print("In ",future,", the production will be", a + b * x_pred)
