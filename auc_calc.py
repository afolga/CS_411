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
#opening files
probability_array=[]
with open('file1.txt') as file_obj:
    for line in file_obj:
        inner_list = [elt.strip() for elt in line.split(',')]
        probability_array.append(inner_list)

positive_negative=[]
with open('file2.txt') as file_obj2:
    for line in file_obj2:
        inner_list = [elt.strip() for elt in line.split(',')]
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
    else: #this is tn
        tn+=1
#now we begin calculations of TPR, FPR
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


#calculating AUC here
delta_x = fpr[0]
delta_y = tpr[0]
area=0
num_rectangles=0
for i in range(len(tpr)):
    if delta_x!=fpr[i] and delta_y!=tpr[i]:
        #print("AREA : " + str(fpr[i]) + "--" + str(delta_x) + "*" + str(delta_y))
        area += (fpr[i] - delta_x) * tpr[i]-delta_y
        delta_x = fpr[i]
        #print("delta_x: "+str(delta_x)+"delta_y:"+str(delta_y))
        num_rectangles+=1
area=area*-1




f=open("auc.txt","w")
f.write(str(area))
f.close()