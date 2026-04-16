# Simple ANOVA (2 groups only)

g1 = list(map(float, input("Enter group 1 values (space separated): ").split()))
g2 = list(map(float, input("Enter group 2 values (space separated): ").split()))

# Means
m1 = sum(g1) / len(g1)
m2 = sum(g2) / len(g2)
print("Mean of group 1:", m1, "Mean of group 2:", m2)

# Grand mean
grand_mean = (sum(g1) + sum(g2)) / (len(g1) + len(g2))
print("Grand mean:", grand_mean)

# SSC (between groups)
ssc = len(g1)*(m1 - grand_mean)**2 + len(g2)*(m2 - grand_mean)**2
print("SSC (between groups):", ssc)

# SSE (within groups)
sse = sum((x - m1)**2 for x in g1) + sum((x - m2)**2 for x in g2)
print("SSE (within groups):", sse)

# MSC and MSE
msc = ssc / (2 - 1)
mse = sse / (len(g1) + len(g2) - 2)
print("MSC (between groups):", msc)
print("MSE (within groups):", mse)

# F value
f = msc / mse

print("F-value:", f)