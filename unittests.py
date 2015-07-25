import unittest
from QuickSort import QuickSort
import random as r

class TestQuickSort(unittest.TestCase):

    def test_partitionWrongPivotIndex(self):
        size = r.randint(5,50)
        array = [r.randint(0,size) for i in xrange(size)]
        pivotIndex = size;
        
        qs = QuickSort()
        
        result = qs.partition(array, pivotIndex)
        self.assertEqual(array,result)
        
        
    def test_partitionExpectedTransformation(self):
        array = [4, 2, 1, 0, 8, 4, 3, 7, 6]
        pivotI = 5
        pivot = 4
        expected = [4, 2, 1, 0, 3, 4, 8, 7, 6]
        qs = QuickSort()
        
        result = qs.partition(array, pivotI)
        self.assertEqual(array,result)

    def test_partitionExpectedTransformation2(self):
        array = [4, 5, 1, 0, 8, 4, 3, 7, 6]
        pivotI = 5
        pivot = 4
        expected = [4, 1, 0, 3, 4, 5, 8, 7, 6]
        qs = QuickSort()
        
        result = qs.partition(array, pivotI)
        self.assertEqual(array,result)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQuickSort)
    unittest.TextTestRunner(verbosity=2).run(suite)