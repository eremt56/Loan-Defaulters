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

        self.data = self.frequencyEncode(self.data, 'City', 'CityEncoded')
        self.data = self.frequencyEncode(self.data, 'State', 'StateEncoded')
        self.data = self.frequencyEncode(self.data, 'Zip', 'ZipEncoded')
        self.data = self.frequencyEncode(self.data, 'Bank', 'BankEncoded')
        self.data = self.frequencyEncode(self.data, 'BankState', 'BankStateEncoded')
        self.data = self.frequencyEncode(self.data, 'NAICS', 'NAICSEncoded')
        self.data = self.frequencyEncode(self.data, 'ApprovalDate', 'ApprovalDateEncoded')        
        self.data = self.frequencyEncode(self.data, 'ApprovalIFY', 'ApprovalIFYEncoded')
        self.data = self.frequencyEncode(self.data, '', 'BankStateEncoded')
        self.data = self.frequencyEncode(self.data, 'BankState', 'BankStateEncoded')
        self.data = self.frequencyEncode(self.data, 'BankState', 'BankStateEncoded')
        self.data = self.frequencyEncode(self.data, 'BankState', 'BankStateEncoded')
        self.data = self.frequencyEncode(self.data, 'BankState', 'BankStateEncoded')
        self.data = self.frequencyEncode(self.data, 'BankState', 'BankStateEncoded')
        self.data = self.frequencyEncode(self.data, 'BankState', 'BankStateEncoded')

        self.data['UrbanRural'] = pd.get_dummies(self.data['UrbanRural'])
        #will this actaully work ^^^^?
        
        self.data = pd.get_dummies(self.data)



    def normalize(self, dataArray):
       
        for i in range(dataArray[0].size):

            maximum= np.amax(dataArray[i])
            minimum = np.amin(dataArray[i])

            for j in range(dataArray.size):
                dataArray[i][j] = ((dataArray[i][j] - minimum)/(maximum - minimum))


    def frequencyEncode(self, data, name, newName):
         encode = (data.groupby(name).size()) / len(data)
         data.loc[:, "{}_freq_encode".format(name)] = data[name].map(encode)
         data = data.drop([name], axis=1)
         return data

    def applyVals(dataArray):
        hash = dict()
        for i in dataArray:
            if hash[i] == None:
                hash[i] = 0
            else: hash[i]+=1



    

        
        


        