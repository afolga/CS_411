'''
NBC.py
Naive-Bayesian Classifier
- includes variable to switch on/off smoothing
        - print in both options
- input: any num of attr, where last attr = class attr (attr vals = discrete)
        - first row = attr names
        - rest = data instances

A1, A2, A3, A4, C
b, b, b, t, 1
a, a, b, t, 1
a, y, t, d, 1

x, y, f, d, 0
x, s, f, r, 0

'''
#from anytree import Node, RenderTree // wanted to use this library for its tree implementation



class dataNode: # e.g. node for storing data to get likelihoods
        def __init__(self, data, count):
                self.data = data
                self.count = count
        
        def newInstanceFound(self):
                self.count = self.count + 1
                

# Function: split_class
# Splits the data by class
# Input: List
# Output: Dictionary
def split_by_class(data): # data being list of list
        split_set = dict()
        for i in range(len(data)):
                set = data[i]
                class_val = set[-1] # get last attribute == class value
                if (class_val not in split_set): # kind of obvious, but new key(class)
                        split_set[class_val] = list()
                split_set[class_val].append(set)
        #for class_key in split_set:
                #for row in split_set[class_key]:
                        #row.pop() # get rid of class val at end of each list (row in file)
        return split_set

# Function: get_likelihood
# Gets likelihoods from data dictionary
# Input: Dictionary, List
# Output: Dictionary
def get_likelihood(data, nameList, smoothing): # data being the split dictionary
        like_set = dict()
        for key in data:
                like_set[key] = list() # key is className
                for i in range(len(nameList) - 1): # initialize attribute instance lists
                        valList = list()
                        like_set[key].append(valList)
                for instance in data[key]: # each data instance (row in file)
                        #print(instance)
                        valCounter = 0
                        for i in range(len(instance) - 1):
                                # populating the inside-most list w/ count
                                # uncomment print statements in conditionals for error checking (3 total) + 1 at bottom for full set (line 79)
                                if (len(like_set[key][i]) == 0): # first instance of charAttr group
                                        if smoothing == False:
                                                like_set[key][i].append([instance[valCounter], 1])
                                        else:
                                                like_set[key][i].append([instance[valCounter], 2])
                                else:
                                        dupBoolean = False
                                        for j in range(len(like_set[key][i])):
                                                if instance[valCounter] == like_set[key][i][j][0]:
                                                        #print("instrance[valCounter] is " + instance[valCounter] + " and " + str(like_set[key][i][j][0]))
                                                        dupBoolean = True
                                                        break
                                        if dupBoolean == True: # duplicate found
                                                like_set[key][i][j][1] = like_set[key][i][j][1] + 1
                                        else: # no duplicate
                                                if smoothing == False:
                                                        like_set[key][i].append([instance[valCounter], 1])
                                                else:
                                                        like_set[key][i].append([instance[valCounter], 2])
                                valCounter = valCounter + 1
        #print(like_set)
        return like_set

# Rest of Program
#print('Python refresh sanity check')
smoothingBool = True # pretty sure smoothing works

trainingFileString = 'file3.txt'
testingFileString = 'file4.txt'

parsedData = [] # list of list (parsed strings)
attrNameArray = [] # list of attr names + class name at index[-1]
numPerAttrPerClassArray = [] # total num insatnces per atttribute per class
totalInstances = 0

# // getting data from training file as list of list
with open(trainingFileString) as trainingFile:
        fileInput = trainingFile.readlines() # grabbed file data as list of strings
        # // split fileInput LoS into List of List
        i = 1
        for line in fileInput:
                line = line.strip()
                if line:
                        if i==1: # don't add attr names to list of list i.e. data instances
                                i = i+1
                                attrNameArray = [attribute.strip() for attribute in line.split(',')] # make list from string
                        else:
                                parsedLine = []
                                #data = line.split(',')
                                data = [attribute.strip() for attribute in line.split(',')] # make list from string
                                parsedData.append(data)  # populate list of list
                                totalInstances = totalInstances + 1

split_input = split_by_class(parsedData) # btw dictionary

# training output files
outputTrainFile = 'privateTrainOutput.txt'
demoTrainingFileOne = 'NB_probabilities_no_smoothing.txt'
demoTrainingFileTwo = 'NB_ probabilities_smoothing.txt'
f=open(outputTrainFile,"w")

# getting all likelihoods
# class likelihoods
classProbs = []
for key in split_input:
        newNode = dataNode(key, len(split_input[key])) # no attrName needs bc class
        classProbs.append(newNode)
# instance conditional likelihoods
instanceLikelihood = get_likelihood(split_input, attrNameArray, smoothingBool)
for classKey in instanceLikelihood:
        for instance in instanceLikelihood[classKey]:
                perAttrCount = 0
                for data in instance:
                        perAttrCount = perAttrCount + data[1]
        numPerAttrPerClassArray.append([classKey, perAttrCount])

for key in classProbs:
        probability = float(key.count) / totalInstances
        f.write("P(" + attrNameArray[-1] + "=" + key.data + ") = " + str(probability) + "\n") # P(C=?) = ?
classIndex = 0

condProbDict = dict() # conditional probability dictionary
for classKey in instanceLikelihood:
        #print(classKey)
        index = 0
        for instance in instanceLikelihood[classKey]:
                #print("New instance")
                for data in instance:
                        #print(data)
                        prob = data[1] / float(numPerAttrPerClassArray[classIndex][1])
                        term = str(attrNameArray[index] + "=" + data[0] + " | " + attrNameArray[-1] + "=" + classKey)
                        condProbDict[term] = prob
                        f.write("P(" + term + ") = " + str(prob) + "\n") # P(AttrName=? | C=?) = ?
                index = index + 1
        classIndex = classIndex + 1

# create and populate data structure to hold probs for testing

f.close()

# for test data (not training data)
testAttrNameArray = [] # HOLD TEST ATTR NAMES
parsedData = [] # reusing old list from training

with open(testingFileString) as testFile:
        fileInput = testFile.readlines() # grabbed file data as string
        # // split fileInput LoS into List of List
        i = 1
        for line in fileInput:
                line = line.strip()
                if line: # not stripping attr names
                        parsedLine = []
                        #data = line.split(',')
                        data = [attribute.strip() for attribute in line.split(',')] # make list from string
                        parsedData.append(data)  # populate list of list

#print(parsedData)
testProbList = []
classIndex = 0
# use condProbDict for testing/getting class probabilities
#print(totalInstances)
for classKey in instanceLikelihood:
        classProbList = []
        for testListIndex in range(len(parsedData)-1):
                #print(parsedData[testListIndex+1]) # conditional prob equations
                attrCounter = 0
                totalProb = 1
                for dataTestInstance in parsedData[testListIndex+1]: #checking each instance
                        #print(dataTestInstance)
                        foundMatchingProb = False # boolean for match
                        foundProb = 0.0 # float for holding prob
                        for key in condProbDict: # checking probability dictionary
                                #print("Key: " + key + " has val of " + str(condProbDict[key]))
                                #print(key)
                                searchString = str(parsedData[0][attrCounter]) + "=" + str(dataTestInstance) + " | " + attrNameArray[-1] + "=" + str(classKey)
                                if searchString in key:
                                        #print("got data for " + searchString)
                                        foundMatchingProb = True
                                        foundProb = condProbDict[key]
                                        break
                        if foundMatchingProb == True:
                                #print("Multiplying totalProb (" + str(totalProb) + ") by " + str(foundProb))
                                totalProb = totalProb * foundProb
                        else: 
                                if smoothingBool == False:
                                        #print("Multiplying totalProb (" + str(totalProb) + ") by 0")
                                        totalProb = totalProb * 0
                                else:
                                        smoothedProb = 1.0 / totalInstances
                                        #print("Multiplying totalProb (" + str(totalProb) + ") by " + str(smoothedProb))
                                        totalProb = totalProb * smoothedProb
                        attrCounter = attrCounter + 1
                classProbList.append(totalProb)
        testProbList.append(classProbList)
#print(testProbList)

# testing output
demoTestFile = 'NB_test_smoothing.txt'
outputTestFile = 'privateTestsOutput.txt'
testFileOut=open(outputTestFile,"w")
for testedInstances in testProbList: # row in test file
        bestProb = testedInstances[0]
        savedBestIndex = 0
        index = 0
        for classProb in testedInstances:
                if classProb > bestProb:
                        bestProb = classProb
                        savedBestIndex = index
                index = index + 1
        bestClassName = ""
        classIndexGetter = 0
        for classKey in instanceLikelihood:
                if classIndexGetter == savedBestIndex:
                        bestClassName = classKey
                        break
                classIndexGetter = classIndexGetter + 1
        #print(bestClassName)
        testFileOut.write(bestClassName + "\n")
testFileOut.close()

# NOTES
# for smoothing: use function on slides (w/ Additoinal Issues--zero counts)
