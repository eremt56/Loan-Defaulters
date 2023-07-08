import pandas as pd
import numpy as np


class Processing:
    
    # Class Objects:
    data = pd.DataFrame()


    # Data Parsing:
    def __init__(self):
        
        self.data = pd.read_csv("SBAcase.11.13.17.csv")

    # Cleaning the data:
    # I am looking for unimportant data
    # Discrete Data to be encoded
    # Continuous Data to be normalized
    def clean(self):

        self.data.drop(["Selected", "LoanNr_ChkDgt", "Name",
        "State", "FranchiseCode", "ChgOffDate", "BalanceGross"], axis = 1)
        
        self.data = pd.get_dummies(self.data)

        print(self.data)


    def normalize(self, dataArray):
       
        for i in range(dataArray[0].size):

            maximum= np.amax(dataArray[i])
            minimum = np.amin(dataArray[i])

            for j in range(dataArray.size):
                dataArray[i][j] = ((dataArray[i][j] - minimum)/(maximum - minimum))

        
        


        