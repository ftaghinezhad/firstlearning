import numpy as np

traindata = []

f = open('SimLex999.txt','r')
    
i=1
    
for line in f:
    
    if i==1:
        i=i+1
        continue
    
    #print('i = ',i,' , line = ',line,' , len(line) = ', len(line))
    if len(line)!=1:
        s = line.split('	')
        traindata.append([s[0].strip(),s[1].strip(),s[3].strip()])  
        i = i+1 
              
f.close()


#----------------- Count the words and labels --------------------------------
data_x=[]
data_y=[]

i=0
for w in traindata:    
    data_x.append([traindata[i][0],traindata[i][1]])
    data_y.append(traindata[i][2])    
    i=i+1

values_x, counts_x = np.unique(data_x, return_counts=True)
values_y, counts_y = np.unique(data_y, return_counts=True)

#------------------------------------------------------------------------------
