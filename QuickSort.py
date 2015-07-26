class QuickSort:
    def partition(self, a, pivotI):
        size = len(a)-1
        if(pivotI >= size+1):
            return a
        
        pivot = a[pivotI]
        #Moving pivot in the end
        a[size],a[pivotI]=a[pivotI],a[size]
        i=0
        for j in range(size):
            if(a[j]<=pivot):
                a[i],a[j] = a[j],a[i]
                i+=1
        #Moving pivot back
        a[i],a[size] = a[size],a[i]
        print a
        return a
