# Property plotting of normal distribution 

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,50,100)

def normal_dist(x, mean, sd):
    prob_density = (np.pi * sd) * np.exp(-0.5 * ((x-mean)/sd)**2)
    return prob_density

mean = np.mean(x)
sd = np.std(x)

pdf = normal_dist(x, mean, sd)

plt.plot(x, pdf, color = "red")
plt.xlabel("Data Points")
plt.ylabel("Probability Density")
plt.show()

mean = 30
sd = 5
print("for Mean = ", mean, "For Standard Deviation = ", sd)
values = np.random.normal(mean,sd,1000)

plt.hist(values, 200,color = "red")

plt.show()