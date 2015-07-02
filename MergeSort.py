'''
Created on 2 Jul 2015

@author: biedakl
'''


class MergeSorter:
    
    def merge(self, a,b):
        i=0
        j=0
        c = []
        for k in range(len(a)+len(b)):
            if(a[i]<b[j]):
                c.append(a[i])
                print("i: " + str(i))
                i+=1
                if(i == len(a)):
                    c.extend(b[j:])
                    break
                
            else:
                c.append(b[j])
                print("j: " + str(j))
                j+=1
                if(j == len(b)):
                    c.extend(a[i:])
                    break
                
                 
        return c



a = [21, 54, 67, 77]
b = [1, 44, 45, 54, 66]

merger = MergeSorter()
x = merger.merge(a, b)
print (x)
