import numpy as np
import sys
import random

def sigmoid(x):
    return (1 / (1 + np.exp(-x)))
#i can make the weights and biases random??
count=0
network_ls=[]
with open('texting.txt') as file_obj:
    for line in file_obj:
        inner_list = [elt.strip() for elt in line.split(',')]
        network_ls.append(inner_list)
    count+=len(inner_list)

#print(count)
#print(network_ls)
#need to ignore first list
class_list=network_ls[0]
network_ls.pop(0)
#print(class_list)
#print(network_ls)
# number of neurons

weights=[]
count_weight=0
count_sum=0
rows,cols=(len(network_ls[0])-1),len(network_ls)
#print(len(network_ls[0])-1) #16
#print(len(network_ls)) #7
sums=[[0]*cols]*rows
#print(sums)
count_up=0
for x in range(len(network_ls)):
    #print("THIS IS X"+str(x))
    count_up+=1
    #print('this is len(x)' +str(x))
    weights.append(random.random())
    for y in network_ls:
        #count_up=0
        #print('this is len(y):'+str(y))
        if y[x]!='yes' and y[x]!='no':
            print(y[x])
            #print("+++++++")
            #print('this is sums[count_sum][count_weight]')
            #sums[count_up][count_sum] += np.dot(float(y[x]), weights[count_up]) #weights[len 7]
        #print("count_sum:",str(count_sum))
        count_sum+=1
        #count_up+=1
        #print("THIS IS THE NEW COUNTER:"+str(count_up))
#print(weights)

for i in network_ls:
    #print(len(i))
    weights.append(random.random())
    print("THIS IS i:"+str(len(i)))
    #is i the number of layers???
    #weights.append(random.random())
    #print(weights)
    for x in i:
        print(x)
        #count_sum+=1
        #print(count_sum)
        if x!='yes' and x!='no':
            #this means its a number
            #here i want a random weight , then run sigmoid
            print(str(sums[count_weight]))
           #sums[count_sum][count_weight]+=np.dot(float(x),weights[count_weight])
    count_sum+=1
    #print(count_sum)
    count_weight+=1
#rint(network_ls)
rows,cols=(len(network_ls[0])-1),len(network_ls)
sums=[[0]*cols]*rows
#print(len(network_ls[0])-1) #16
print(len(network_ls)) #7
weights_new=[[0]*16]*7
for i in range(0,len(network_ls[0])-1):  #16
    for j in range(0,len(network_ls)): #7
        weights_new[j][i]=random.random()

print(weights_new)

for i in range(0,len(network_ls[0])-1):  #16
    for j in range(0,len(network_ls)): #7
        if network_ls[j][i]!='yes' and network_ls[j][i]!='no':
            #print(network_ls[j][i])
            #print(weights_new[j][i])
            sums[i][j]+=(float(network_ls[j][i])*(weights_new[j][i]))

print(sums)

#print(count_weight)
    #then need to call sigmoid on each of the sums
#print(len(weights))
#print(len(sums[0]))
#print(len(sums[1]))
#print("sums="+str(sums))
sigmoid_sum=[0]*(len(network_ls[0])-1)
sigs=0
count_sig=0
for i in sums:
    for x in i:
        sigs+=x
        sigmoid_sum[count_sig]=sigmoid(sigs)
    count_sig+=1
    #print(sigs)
    sigs=0
#print(sigmoid_sum) #hypothetically first layer
network=[]
with open('input.txt') as file_obj:
    for line in file_obj:
        inner_list = [elt.strip() for elt in line.split(',')]
        network.append(inner_list)
#ignore first array
#print(network)
def sigmoid(x):
    return (1 / (1 + np.exp(-x)))

def sigmoid_derivative(x):
    return x * (1 - x)
