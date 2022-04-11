# CS_411
# Project 2

# - Computing AUC 
Completed by Agnes Folga. Program takes in 2 files, reads the probabilities of the positive class, sorts by ascending order, and correlates it with its positive, or negative classification. TPR and FPR are calculated, then the AUC is calculated by the change in x and y of the graph (not using traditional calculus as by guidelines). AUC value is printed to a txt file
# - Implementing a Naive-Bayesian Classifier
Completed by Alex Tkaczyk. Program input being 2 files. 
First file being a training dataset, which is parsed (using split_by_class) and the data is stored in a complex dictionary(referred to as ParsedDict here). ParsedDict is then iterated through to compute the conditional probabilities(using get_likelihood). All conditional likelihoods are then written out to a file. Condiitonal likelihoods are also stored in a different dictionary (referred to as ProbDict here), as preperation for testing.
The second file being a test dataset, which is parsed through and iterates through ProbDict. Whilst iterating, the program checks whether the data instances were present in the training data. The probabilities are then summed up and stored in a list. Once all class probabilties are calculated, the program checks through the list and chooses whichever probabilty is higher -> choosing the predicted class. The predicted class is then written out to a file.
Smoothing in this program is done using a singular boolean, which can be altered by the programmer

split_by_class:
    creates a dictionary, then iterates through a list of list. It uses the class name as the keys and then appends the data instances as lists under the designated keys
get_likelihood:
    takes in a dictionary and list, creates a new dictionary (complexer than any other--full of lists of lists of etc...). Iterates through the input dictionary and counts up all instances of data and their counts.