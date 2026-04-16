# F test 

import math

sample1= int(input("Enter the number of data points: "))
sample1_points = []
for i in range(sample1):
    sample1_points.append(float(input("Enter data point: ")))
    
sample2 = int(input("Enter the number of data points: "))
sample2_points = []
for j in range(sample2):
    sample2_points.append(float(input("Enter data point: ")))

x1_bar = sum(sample1_points)/sample1
x2_bar = sum(sample2_points)/sample2

x1_min_x1_bar_sqr = [(k - x1_bar)**2 for k in sample1_points]
x2_min_x2_bar_sqr = [(l - x2_bar)**2 for l in sample2_points]

print(sum(x1_min_x1_bar_sqr))
print(sum(x2_min_x2_bar_sqr))

s1_sqr = sum(x1_min_x1_bar_sqr)/ (sample1 - 1)
s2_sqr = sum(x2_min_x2_bar_sqr)/ (sample2 - 1)

print("s1^2: ", s1_sqr)
print("s2^2: ", s2_sqr)

if (s1_sqr > s2_sqr):
    f = s1_sqr / s2_sqr
else:
    f = s2_sqr / s1_sqr
    
print("Calculated Value of F: ", f)

df1 = sample1 - 1
df2 = sample2 - 1
print("Degrees of freedom for sample 1: ", df1)
print("Degrees of freedom for sample 2: ", df2)