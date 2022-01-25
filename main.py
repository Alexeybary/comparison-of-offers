
import re

import scipy
from scipy import spatial
import numpy as np

with open("sentences.txt") as file:
    lines=[]
    for line in file:
        lines.append(line.lower().strip())
d={}
count=0

for line in lines:
    for i in re.split('[^a-z]',line):
        if i not in d.keys() and i!='':
            d[i]=count
            count+=1
matrix = np.zeros((len(lines),len(d)))
for i in range(len(lines)):
    for keys,values in d.items():
        temp=lines[i].count(keys,0,len(lines[i]))
        matrix[i][values]=temp
for i in range(len(lines)):
    val=scipy.spatial.distance.cosine(matrix[0],matrix[i])
    print(val)