'''
Created on 2 Jul 2015

@author: biedakl
'''
from random import randint

class MergeSorter:

    def __init__(self):
        self.counter = 0
    
    def sort(self, x):
        size = len(x)
        if(size>1):
            a = x[0:size/2]
            b = x[size/2:]
            a = self.sort(a)
            b = self.sort(b)
            x = self.merge(a,b)
            return x
        return x
    
    def merge(self, a,b):
        i=0
        j=0
        c = []
        for k in range(len(a)+len(b)):
            if(a[i]<=b[j]):
                c.append(a[i])
                i+=1
                if(i == len(a)):
                    c.extend(b[j:])
                    self.counter+=len(b[i:])
                    break
                
            else:
                self.counter+=len(a)-i
                c.append(b[j])
                j+=1
                if(j == len(b)):
                    c.extend(a[i:])
                    self.counter+=len(a[i:])
                    break
                
                 
        return c
    
def brute(a):
    c = 0
    for i in range(len(a)):
        for j in range(len(a)-i):
            if(a[i]>a[i+j]):
                c+=1
        if(i%100==0):
            print((i+0.0)/len(a))
    return c

def fillRandom(n):
    a = []
    for i in range(n):
        a.append(randint(0, n))

def readArrayFromFile():
    a = []
    f = open("/home/biedakl/pythonApps/AlgorithmsCoursera/IntegerArray.txt", 'r')
    for line in f:
        a.append(int(line))
    return a



#a = fillRandom(1000)
a = [76, 80, 451, 546, 555, 3,  684, 732, 743, 4, 5]
b = readArrayFromFile()
merger = MergeSorter()
x = merger.sort(b)
#print (brute(b))
print (x)
print (merger.counter)
