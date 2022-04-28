'''
Alexander Tkaczyk
Linear Regression Model
    input: any num of attr, where last attr = output/predictive var (attr vals = discrete)
            first row = attr names
            rest = data instances
    using same loss function (from lecture)
    using batch gradient descent method for optimization

Sample Input:
    A1, A2, Y 
    1.5, 2.2, 4.3 
    20, 1.6, 3.5
A? = X COORDS
Y = Y COORD

Prelim:
    Code in training data

Problem 1:
    Get Test Instances w/o output variable
    Predict output variable
    Write predicted value to text file
    (any num of input vars)

Problem 2: 
    Using plot package (found by me), plot:
        training input data points
        output linear func
        predicted value for each test instance
    (one input var)

Resources:
        Linear and Logistic Slides (17-21)
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

trainingFileString = '1-linear-regression-training.txt' #--change during demo
testingFileString = '1-linear-regression-testData.txt' #--change during demo

# // getting data from training file as list of list
def parseData(fileName):
        cleanedData = list()
        with open(fileName) as file:
                fileInput = file.readlines() # grabbed file data as list of strings
                # // split fileInput LoS into List of List
                i = 1
                for line in fileInput:
                        line = line.strip()
                        if line:
                                if i==1: # don't add attr names to list of list i.e. data instances
                                        i = i+1
                                else:
                                        #data = line.split(',')
                                        data = [attribute.strip() for attribute in line.split(',')] # make list from string
                                        floatData = [eval(x) for x in data] # convert strings to floats
                                        cleanedData.append(floatData)  # populate list of list
        return cleanedData

parsedData = parseData(trainingFileString) # list of list (parsed strings)
#print(parsedData) # where in each array[0] = x, and array[1] = y

# linear regression model: y = theta0 + theta1*x 
theta0 = 1.0
theta1 = 1.0

# Learning Rate
alpha = 0.0001

# Total num of data instances
n = float(len(parsedData))

# linearRegFunc
# both params are type float
# ℎ_𝛉 = 𝜃_0 + 𝜃_1*x_i (essentially y = mx+b) ----- use for h_𝛉(x_1)
def linearRegFunc(x_val):
        yPredict = theta1 * x_val + theta0
        return yPredict

# summationForLR -- might have to script this...no func
# sum(i=1 -> n) ((h_𝜃(x_i)-y_i)^2 ---- use for summation
def summationForLR(data):
        sum = 0.0
        for i in range(int(n)):
                h_0 = linearRegFunc(data[i][0])
                y_i = data[i][1]
                sum = sum + (h_0 - y_i)
        return sum

# batchGradientDescent
# using all data instances(batch)
counter = 0
oldLoss = 0 # might not be right -- potentially change
while(True):
        # calculate loss here (using loss = lossFunciton)

        yPredict = linearRegFunc(parsedData[counter][0])
        #print("yPredict = " + str(yPredict))
        summationResult = summationForLR(parsedData)
        #print("SumResult = " + str(summationResult))
        newTheta0 = theta0 - alpha*(1.0/n)* summationResult
        #print("Theta0 = " + str(theta0))
        newTheta1 = theta1 - alpha*(1.0/n)*summationResult * parsedData[counter][0]
        #print("Theta1 = " + str(theta1) + "\n")
        theta0 = newTheta0
        theta1 = newTheta1

        #print("yPredict = " + str(yPredict) + " and yActual = " + str(parsedData[counter][1]) + "\n")
        newLoss = (1.0/(2.0*n)) * (summationForLR(parsedData) ** 2)
        #newLoss = abs(yPredict - parsedData[counter][1])
        #print("New Loss = " + str(newLoss) + "\n")
        if abs(newLoss - oldLoss) < 0.000001:
                #print("Breaking out, found convergence\n")
                break
        oldLoss = newLoss
#print("Theta0 = " + str(theta0) + "\n")
#print("Theta1 = " + str(theta1) + "\n")

# plotting training data
for dataPoint in parsedData:
        plt.scatter(dataPoint[0], dataPoint[1], color='blue')
# plotting linear function
x = np.linspace(0,3,100)
y = theta0 + theta1*x
plt.plot(x, y, '-r')

# Testing data
parsedTestData = parseData(testingFileString) # list of list (parsed strings)
#print(parsedTestData) # where in each array[0] = x, and array[1] = y

for i in range(len(parsedTestData)):
        yTestPred = linearRegFunc(parsedTestData[i][0])
        parsedTestData[i].append(yTestPred)
        #print(parsedTestData[i])

# plotting test data
for dataPoint in parsedTestData:
        plt.scatter(dataPoint[0], dataPoint[1], color='black')
# plt.xlim([0, 20])
# plt.ylim([0, 20])
trainingLegend = mpatches.Patch(color='blue', label='Training data')
testingLegend = mpatches.Patch(color='black', label='Testing data')
lineLegend = mpatches.Patch(color='red', label='Linear Function')
plt.legend(handles=[trainingLegend, testingLegend, lineLegend])
#plt.legend()
plt.show()