from scipy import stats

group1 = [65,87,73,79,81,69]
group2 = [75,69,83,81,72,79,90]
group3 = [59,78,67,62,83,76]
group4 = [94,89,80,88,96]

#perform Kruskal-Wallis Test 
value,p = stats.kruskal(group1, group2, group3, group4)

print(value)
print(p)

alpha = 0.05
if p > alpha:
	print('Accept H0)')
else:
	print('Reject H0')
