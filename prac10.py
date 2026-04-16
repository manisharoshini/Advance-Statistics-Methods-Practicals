# Wilcoxon signed rank test

import scipy.stats as rank

data = [6,5,1,5,2,2,7,5,3,7,7,4]
median = 3

print("Question:",data)
print("H0: median ==",median)

data_n = [ i - 3 for i in data]

print("After subtracting by",median,"we get:",data_n)

#REMOVE ZERO
signs_temp = [i  for i in data_n if i != 0]
print("Remove Zeros:",signs_temp)
signs = [abs(i)  for i in signs_temp]
print(signs)
rankk = rank.rankdata(signs)
print("Ranking:",rankk)

p_signs = sum([ rankk[i] for i in range(len(signs_temp)) if signs_temp[i] > 0])
n_signs = sum([ rankk[i] for i in range(len(signs_temp)) if signs_temp[i] < 0])

print("T+ Positive:",p_signs)
print("T- Negative:",n_signs)

T = min(p_signs,n_signs)
print("Mininum T:",T)
