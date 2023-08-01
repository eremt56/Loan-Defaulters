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

        self.data = self.data.drop(["Selected", "LoanNr_ChkDgt", "Name",
        "State", "FranchiseCode", "ChgOffDate", "BalanceGross", "DisbursementDate", "BalanceGross"], axis = 1)

        self.data = self.frequencyEncode(self.data, 'City', 'CityEncoded')
        self.data = self.frequencyEncode(self.data, 'Zip', 'ZipEncoded')
        self.data = self.frequencyEncode(self.data, 'Bank', 'BankEncoded')
        self.data = self.frequencyEncode(self.data, 'BankState', 'BankStateEncoded')
        self.data = self.frequencyEncode(self.data, 'NAICS', 'NAICSEncoded')
        self.data = self.frequencyEncode(self.data, 'ApprovalDate', 'ApprovalDateEncoded')        
        self.data = self.frequencyEncode(self.data, 'ApprovalFY', 'ApprovalFYEncoded')
        self.data = self.frequencyEncode(self.data, 'LowDoc', 'LowDocEncoded')        
        self.data = self.frequencyEncode(self.data, 'MIS_Status', 'MIS_StatusEncoded')
        
        self.data = pd.get_dummies(self.data, columns=['UrbanRural'], prefix='UrbanRural')
        self.data = pd.get_dummies(self.data, columns=['RevLineCr'], prefix='RevLineCr')

        self.data = self.normalize(self.data)

        self.data = self.data.dropna()

        self.data = self.data.T

        self.data = self.swap_rows(self.data, 'Default', 'RevLineCr_Y')

        valData = self.data.iloc[:31, 0:100]
 
        valDataAnswer = self.data.iloc[31, 0:100]

        answer = self.data.iloc[31, 100:]

        self.data = self.data.iloc[0:31, 100:]

        # Did I maybe swap the answer column incorrectly????

        return self.data, answer, valData, valDataAnswer


    def normalize(self, dataArray):
        
        dataArray = dataArray.replace({True:1, False:0})

        for i in dataArray.columns:
            maximum= np.amax(dataArray.loc[:, i])
            minimum = np.amin(dataArray.loc[:, i])

            for j in range(dataArray.loc[:, i].size):
                dataArray.loc[j, i] = ((dataArray.loc[j, i]) - minimum)/(maximum - minimum)

        return dataArray


    def frequencyEncode(self, data, name, newName):
         encode = (data.groupby(name).size()) / len(data)
         data.loc[:, "{}_freq_encode".format(name)] = data[name].map(encode)
         data = data.drop([name], axis=1)
         return data


    def swap_rows(self, df, row1, row2):
        df.loc[row1], df.loc[row2] =  df.loc[row2].copy(), df.loc[row1].copy()
        return df



    

        
        


        