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
print(tpr)
print(fpr)


#auc=0
    #print("THIS IS AUC:"+str(auc))
#when the height or width is changing, can calculate
#auc=1*np.trapz(tpr,fpr) #integrating, probs should ask
#have to do it by sqaures
#print(auc)



#consider sliding window technique
delta_x = fpr[0]
delta_y = tpr[0]
area=0
num_rectangles=0
for i in range(len(tpr)):
    print("AREA : " + str(fpr[i]) + "--" + str(delta_x) + "*" + str(delta_y))
    #first case, no idea how to fix because both need to be different
    if delta_x!=fpr[i] and delta_y!=tpr[i]:
        #delta_x=fpr[i]
        #delta_y=tpr[i]
        print("AREA : " + str(fpr[i]) + "--" + str(delta_x) + "*" + str(delta_y))
        area += (fpr[i] - delta_x) * tpr[i]-delta_y
        delta_x = fpr[i]

        #delta_y=tpr[i]
        print("delta_x: "+str(delta_x)+"delta_y:"+str(delta_y))
        num_rectangles+=1
area=area*-1
print(area)

    #have to check for changes in x over y



#THIS IS MY OWN CODE TO CHECK TO SEE IF IT MATCHES THE EXAMPLE!!!!!!!
#fig=px.line(x=fpr,y=tpr)
#fig.show()



f=open("auc.txt","w")
f.write(str(area))
f.close()