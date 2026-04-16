# SIGN test

from statistics import median

data = list(map(float, input("Enter group 1 values (space separated): ").split()))
median = median(data)
print("Median:", median)

print("H0: The median is", median)

data_n = [i - median for i in data]

print("After Subtracting the median from each value:", data_n)

# Remove Zeros Step
signs = [i > 0 for i in data_n if i != 0]

pos_signs = sum(signs)
neg_signs = len(signs) - pos_signs
print("Number of positive signs:", pos_signs)
print("Number of negative signs:", neg_signs)

Tmin = min(pos_signs, neg_signs)
print("Tmin:", Tmin)

