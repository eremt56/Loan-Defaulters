import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

class Classifaction:

    # Class Objects:
    weight = np.zeros((31, 1))
    weightNought = np.zeros((1, 1))

    tempWeight = np.zeros((31, 1))
    tempWeightNought = np.zeros((1, 1))

    regStep = 0.002

    batchSize = 225

    learningRate = 0.001


    # Initialization:
    def __init__(self):
        self.weight = np.random.rand(31, 1)
        self.weightNought = np.random.rand(1, 1)

        self.tempWeight = np.copy(self.weight)
        self.tempWeightNought = np.copy(self.weightNought)


    # Operational Functions:
    def sigmoid(self, val):
        return 1/(1 + np.power(np.e, -val))
    

    # Log Loss: 
    def lossFunc(self, guess, answer):
        return -(answer*np.log(guess) + (1-answer)*np.log(1-guess))
    
    def guess(self, input):
        first = input.to_numpy().reshape(31, 1)
        second = np.dot(self.weight.T, first)
        third = second + self.weightNought
        return self.sigmoid(third)
    
    def derivWeight(self, input, answer):
        return np.dot(input.to_numpy().reshape(31, 1), (self.sigmoid(np.dot(self.tempWeight.T, input) - answer)).reshape(1, 1)) + np.dot(self.regStep, self.tempWeight)        
    
    def derivWeightNought(self, guess, answer):
        return guess - answer


    # The Loss Function Including its Regularization:
    def lossAndReg(self, loss):
        return loss + (self.regStep/2) * (np.linalg.norm(self.weight))**2


    # Training Function:
    def training(self, data, answer, valData, valAnswer):
         
        count = 0
        epoch = 0
        realLoss = 0
        graphData = np.ndarray(8)

        for i in range(data.columns.size):

            guess = self.guess(data.iloc[:, i])
           
            self.tempWeight = self.tempWeight - self.learningRate * self.derivWeight(data.iloc[:, i],  answer.iloc[i])

            self.tempWeightNought = self.tempWeightNought - self.learningRate * self.derivWeightNought(guess, answer.iloc[i])
            
            count+=1


            # Testing of trained weights on a validation data set
            if count >= self.batchSize:
                self.weight = self.tempWeight
                self.weightNought = self.tempWeightNought

                for i in range(valData.iloc[0, :].size):
                    guess = self.guess(valData.iloc[:, i])
                    loss = self.lossFunc(guess, valAnswer.iloc[i])
                    loss = self.lossAndReg(loss)
                    realLoss += loss
                    
                graphData[epoch] = realLoss/self.batchSize

                print('Loss at epoch ', epoch, ' is ', realLoss/self.batchSize)

                count = 0
                loss = 0
                realLoss = 0
                epoch+=1

        plt.plot(graphData)
        plt.title("Loss Trend Per Epoch")
        plt.xlabel("Epoch")
        plt.ylabel("Log Loss")
        plt.savefig("LossData.png")


                 