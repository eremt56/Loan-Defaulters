import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

data = pd.read_csv("SBAcase.11.13.17.csv")

zipCodes = data["Zip"]



print(zipCodes)

plt.plot(zipCodes)

plt.savefig("Zip Code Plot")