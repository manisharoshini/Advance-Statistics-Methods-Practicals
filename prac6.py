# T - Test 
import math 

data = int(input("Enter the number of data points: "))
data_point = []

for j in range(data):
    data_point.append(float(input("Enter data point: ")))

mu = 65
tabular_t = 2.626

print("Data Point: ", data_point)
X_bar = sum(data_point)/data
print("X-bar: ", X_bar)

X_min_X_bar_sqr = [(i - X_bar)**2 for i in data_point]
print("X-X-bar^2: ", X_min_X_bar_sqr)
print("Total X-X^2:", sum(X_min_X_bar_sqr))

sd = math.sqrt(sum(X_min_X_bar_sqr)/(data-1))

t = (X_bar - mu) / (math.sqrt(data) /sd)
print("t-Value: ", t)

if (t > tabular_t):
    print("Reject Null Hypothesis")
else: 
    print("Accept Null Hypothesis")