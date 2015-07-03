'''
Created on 2 Jul 2015

@author: biedakl
'''
from random import randint

class MergeSorter:
    
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
            if(a[i]<b[j]):
                c.append(a[i])
                i+=1
                if(i == len(a)):
                    c.extend(b[j:])
                    break
                
            else:
                c.append(b[j])
                j+=1
                if(j == len(b)):
                    c.extend(a[i:])
                    break
                
        print(c)         
        return c



a = []
for i in range(1000):
    a.append(randint(0, 1000))

merger = MergeSorter()
x = merger.sort(a)
print (x)
