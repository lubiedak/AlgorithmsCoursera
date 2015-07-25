class QuickSort:
    def partition(self, a, pivotI):
        size = len(a)
        if(pivotI >= size):
            return a
        
        pivot = a[pivotI]
        i=0
        for j in range(size):
            if(a[j]<=pivot and j!=pivotI):
                a[i],a[j] = a[j],a[i]
                
        a[i],a[pivotI] = a[pivotI],a[i]
        
        return a