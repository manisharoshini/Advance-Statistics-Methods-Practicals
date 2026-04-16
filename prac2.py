# Problems based on normal distribution

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,50,200)

def normal_dist(x, mean, sd):
    prob_density = (np.pi*sd) * np.exp(-0.5 * ((x - mean) / sd) ** 2)
    return prob_density

def SND(x,u,sd):
    return (x-u)/sd

mean = np.mean(x)
sd = np.std(x)
print("Mean:", mean)
print("Standard Deviation:", sd)

pdf = normal_dist(x, mean, sd)
print("Probability Density Function:", pdf)
print("z scores:", SND(26,30,5))