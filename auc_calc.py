#takes in 2 files (file1 , file2)
'''
file1: probability for the positive class
1, 0.56
2, 0.70
3, 0.33
file2:
1, P
2, N
3, P
'''
import pandas as pd
import numpy as np

import plotly.express as px
#use probabilites to sort
#AUC is ranking
probability_array=[]
with open('file1.txt') as file_obj:
    for line in file_obj:
        inner_list = [elt.strip() for elt in line.split(',')]
            # in alternative, if you need to use the file content as numbers
            # inner_list = [int(elt.strip()) for elt in line.split(',')]
        probability_array.append(inner_list)
file2= open('file2.txt')
positive_negative=[]
with open('file2.txt') as file_obj2:
    for line in file_obj2:
        inner_list = [elt.strip() for elt in line.split(',')]
        # in alternative, if you need to use the file content as numbers
        # inner_list = [int(elt.strip()) for elt in line.split(',')]
        positive_negative.append(inner_list)
my_dict={}
for i in range(len(probability_array)):
    if len(probability_array)==len(positive_negative):
        my_dict[probability_array[i][1]]=positive_negative[i][1]
res = {key: val for key, val in sorted(my_dict.items(), key = lambda ele: ele[0], reverse = True)} #this sorts the values by ascending order

tn=0# of -- in the dataset originally
fn=0#of ++ in the dataset originally
for x,y in res.items(): #y is the key
    if y=="P": #this is fn
        fn+=1
    else:
        tn+=1
#now we begin calculations
tp= 0
fp=0
count=0
tpr=[0]*len(res)
fpr=[0]*len(res)
for x,y in res.items():
    if y=="P":
        tp+=1
        fn-=1

    else:
        fp+=1
        tn-=1
    tpr[count] = tp / (tp + fn)
    fpr[count] = fp / (tn + fp)
    count+=1


auc_add=[0]*len(tpr)
auc=0

for i in range(0,len(tpr)):
    if tpr[i] ==0 or fpr[i]==0:
        auc_add[i]=0
    else:
        auc_add[i] = tpr[i] / fpr[i]
    auc+=auc_add[i]
    #print("THIS IS AUC:"+str(auc))

auc=1*np.trapz(tpr,fpr) #integrating
print(auc)
"""
THIS IS MY OWN CODE TO CHECK TO SEE IF IT MATCHES THE EXAMPLE!!!!!!!
fig=px.line(x=tpr,y=fpr)
fig.show()
"""
