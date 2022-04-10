'''
NBC.py
Naive-Bayesian Classifier
- includes variable to switch on/off smoothing
        - print in both options
- input: any num of attr, where last attr = class attr (attr vals = discrete)
        - first row = attr names
        - rest = data instances
file3(example file):
A1, A2, A3, C
a, b, t, 1
x, y, f, 0
'''

# Function: split_class
# Splits the data by class
# Input: List
# Output: Dictionary
def split_by_class(data):
        split_set = dict()
        for i in range(len(data)):
                set = data[i]
                class_val = set[-1] # get last attribute
                if (class_val not in split_set): # kind of obvious, but new key(class)
                        split_set[class_val] = list()
                split_set[class_val].append(set)
        return split_set

# Rest of Program
print('Python refresh sanity check')
smoothingBool = False
fileString = 'file3.txt'
#demoTrainingFileOne = 'NB_probabilities_no_smoothing.txt'
#demoTrainingFileTwo = 'NB_ probabilities_smoothing.txt'
parsedData = []
attrNameArray = []

# // getting data from file
with open(fileString) as file3:
        fileInput = file3.readlines() # grabbed file data as list of strings
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

split_input = split_by_class(parsedData)
for class_key in split_input:
        print(class_key)
        for row in split_input[class_key]:
                print(row)
print(attrNameArray)

# to deal with categorical data/all: use enum


# once all enumed -> continue with computation of Naive Bayesian


# for test data (not training data)
testFileString = 'testFilePain.txt'
#demoTestFile = 'NB_test_smoothing.txt'
outputTestClassFile = '' # create new file, which will be written to


# for smoothing: use function on slides (w/ Additoinal Issues--zero counts)
