import pandas as pd
import numpy as np

class Classifaction:

    # Class Objects:
    weight = np.zeros(32, 1)
    weightNought = np.zeros(1, 1)

    tempWeight = np.zeros(32, 1)
    tempWeightNought = np.zeros(1, 1)

    regStep = 0.01

    batchSize = 100

    learningRate = 0.001


    # Initialization:
    def __init__(self):
            self.weight = np.random.rand()
            self.weightNought = np.random.rand()

            self.tempWeight = np.copy(self.weight)
            self.tempWeightNought = np.copy(self.weightNought)


    # Operational Functions:
    def sigmoid(self, val):
        return 1/(1 + np.power(np.e, -val))

    # Squared Loss:
    def lossFunc(self, guess, answer):
        return (guess - answer)**2
    
    def guess(self, input):
        return self.sigmoid(np.dot(self.weight.T, input).resize(1,1) + self.weightNought)
    
    def derivWeight(self, input, guess, answer):
         return (guess - answer) * input + self.regStep * self.weight

    def derivWeightNought(self, guess, answer):
        return guess - answer

    def lossAndReg(self, loss):
        return loss + (self.regStep/2) * np.linalg.norm(self.weight)**2

    def training(self, data, answer):
         
        count = 0



        for i in range(data.columns.size):
            
            guess = self.guess(data.loc[:, i])
            
            self.tempWeight = self.tempWeight - self.learningRate * self.derivWeight(data.loc[:, i], guess, answer.loc[:, i])
            # how to properly init weights in logistic regression
            
            count+=1

            if count >= 263:
                self.weight = self.tempWeight
                self.weightNought = self.tempWeightNought




                 