import numpy as np
import math
import random

def sigmoid(x):
    return (1 / (1 + math.exp(-x)))
def sigmoid_derivative(x):
    return x * (1 - x)
#i can make the weights and biases random??
count=0
network_ls=[]
with open('texting.txt') as file_obj:
    for line in file_obj:
        inner_list = [elt.strip() for elt in line.split(',')]
        network_ls.append(inner_list)
    count+=len(inner_list)
layers=[]
with open('layers.txt') as file_obj:
    for line in file_obj:
        inner_list = [elt.strip() for elt in line.split(',')]
        layers.append(inner_list)
num_layers=int(layers[0][0])
bias=[0]*num_layers #only for hidden layers
for i in range(num_layers):
    bias[i]=random.random()

class_list=network_ls[0]
network_ls.pop(0)
weights=[[0 for i in range(len(network_ls[0])-1)] for j in range(num_layers)]
for j in range(num_layers):
    for i in range(len(network_ls[0])-1): #15
        weights[j][i]=random.random()

new_weights=[0]*num_layers
for j in range(num_layers): #2
    new_weights[j]=random.random()

#new bias
new_bias=random.random()
#for the end
final_classification=[0]*len(network_ls)
# START LOOP HERE, DEFINE ALL WEIGHTS AND BIASES BEFORE HERE
count=0

while (count<10):

    # Input to hidden layer
    sum_array=[[0 for i in range(len(network_ls))] for j in range(num_layers)]
    for n in range(num_layers):
        for j in range(len(network_ls)):
            for x in range(len(network_ls[0])-1):
                if (network_ls[j][x] !='yes' and network_ls[j][x]!='no'):
                    sum_array[n][j]+=weights[n][x]*float(network_ls[j][x])+bias[n]
    #HIDDEN LAYERS SIGMOID TIME
    for n in range(num_layers):
        for j in range(len(network_ls)):
            sum_array[n][j]=sigmoid(sum_array[n][j])
    #HIDDEN LAYERS COMPLETED


    #STARTING HIDDEN TO OUTPUT LAYER
    new_sum_hidden = [0] * len(network_ls)
    for i in range(len(network_ls)): #7
        for j in range(num_layers): #2
            new_sum_hidden[i]+=new_weights[j]*sum_array[j][i] + new_bias
    for i in range(len(new_sum_hidden)):
        new_sum_hidden[i]=sigmoid(new_sum_hidden[i])

    #need to do backpropagation
    #provides an efficient way to train neural networks
    #workhorse of all deep learning models
    #do for each layer
    class_label=[0]*len(network_ls)
    for j in range(len(network_ls)):
        class_label[j]=network_ls[j][-1]
        if class_label[j]=='no':
            class_label[j]=0
        else:
            class_label[j]=1
    new_weight_update=[0]*num_layers
    for i in range(num_layers):
        for j in range(len(network_ls)):
            new_weight_update[i]+=(new_sum_hidden[j]-class_label[j])*sum_array[i][j]

    new_bias_update=0
    for i in range(num_layers):
        for j in range(len(network_ls)):
            new_bias_update+=(new_sum_hidden[j]-class_label[j])


    weight_update=[[0 for i in range(len(network_ls[0])-1)] for j in range(num_layers)]
    for j in range(num_layers):
        for i in range(len(network_ls[0])-1): #15
            weight_update[j][i]=0
    var=0
    #LOSS / ENTROPY
    for  c in range(num_layers):
        for p in range(len(network_ls)):
            var+=((float(new_sum_hidden[p])-float(class_label[p]))*float(sum_array[c][p]))*(1-float(sum_array[c][p]))*float(new_weights[c])
            for a in range(len(network_ls[0])-1):
                if (network_ls[c][a] != 'yes' and network_ls[c][a] != 'no'):
                    weight_update[c][a]+=var*float(network_ls[c][a])
        var=0
    bias_update=[1]*num_layers
    a=0
    for c in range(num_layers):
        for p in range(len(network_ls)):
            a+=((float(new_sum_hidden[p])-float(class_label[p]))*float(sum_array[c][p]))*(1-float(sum_array[c][p]))*float(new_weights[c])
            #print(a)

        bias_update[c]=a

    ## bias_update, weight_update, new_bias_update, new_weight_update
    ##minibatch - linear logistic regression, random m on n mini batch
    ## LR=5e-3
    learning_rate=5e-3
    ## bias=bias-bias_update*LR. weight=weight-weight_update*LR

    for i in range(len(bias)):
        bias[i]=(bias[i]-bias_update[i])*learning_rate
    new_bias=(new_bias-new_bias_update)*learning_rate
    print(new_bias)
    for j in range(num_layers):
        for i in range(len(network_ls[0]) - 1):  # 15
            weights[j][i] =(weights[j][i] -weight_update[j][i])*learning_rate
    print(new_weights)
    for i in range(len(new_weights)):
        new_weights[i]=(new_weights[i]-new_weight_update[i])*learning_rate
            #new_weights[j][i] = (new_weights[j][i] -  new_weight_update[j][i]) * learning_rate
    #print(bias)
    #print(weights)
    print(new_sum_hidden)

    for i in range(len(new_sum_hidden)):
        if new_sum_hidden[i]>0.5:
            final_classification[i]='yes'
        else:
            final_classification[i]='no'
    # For each value new_sum_hidden (1x7), if >0.5, assign to 1/yes. Count number of misclassified, store in num_misclassified. If # misclassified==num_misclassified,
    # break, else num_misclassified=# misclassified (until the 2 match) ??

    count=count+1


#MAKING OUTPUT FILE
f=open("final_class.txt",'w')
for i in range(len(final_classification)):
    f.write(final_classification[i])
    f.write('\n')