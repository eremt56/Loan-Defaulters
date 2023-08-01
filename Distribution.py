import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

zero = 0
one = 0

data = pd.read_csv("SBAcase.11.13.17.csv")

default = data["Default"]

for i in default:
    if i == 0: zero+=1
    if i == 1: one+=1

print(zero, " Zeros and ", one, " ones")

print(default)

plt.plot(default)

plt.savefig("Default Distribution")