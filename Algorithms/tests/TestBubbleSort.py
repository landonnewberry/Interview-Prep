import unittest
import random
import datetime
from Algorithms.sorting.bubblesort import bubblesort
from Algorithms.sorting.mergesort import mergesort

class TestBubbleSort(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(bubblesort([5,3,4,1]), [1,3,4,5])

    def test_reversed_list(self):
        self.assertEqual(bubblesort([5,4,3,2,1]), [1,2,3,4,5])

    def test_negative_elements(self):
        self.assertEqual(bubblesort([-5,4,2,-1]), [-5,-1,2,4])

    def test_large_list(self):
        l = [ random.randint(-1000, 1001) for i in range(10000) ]
        self.assertEqual(bubblesort(l), sorted(l))
    
    def test_empty_list(self):
        self.assertEqual(bubblesort([]), [])

    def test_single_element_list(self):
        self.assertEqual(bubblesort([1]), [1])

    def test_slower_than_mergesort(self):
        l = [ random.randint(-1000, 1001) for i in range(10000) ]
        t1 = datetime.datetime.now()
        bubblesort(l)
        t2 = datetime.datetime.now()
        mergesort(l)
        t3 = datetime.datetime.now()
        self.assertLess(t3 - t2, t2 - t1)

if __name__ == '__main__':
    unittest.main()