import unittest
from mergesort import mergesort
import random
import datetime

def timed(f):
    def wrapper():
        t1 = datetime.datetime.now()
        f()
        t2 = datetime.datetime.now()
        print("Function {} took {} to execute.".format(f.__name__, t2 - t1))
    return wrapper

class TestMergeSort(unittest.TestCase):

    def test_reversed_order_even_list(self):
        self.assertEqual(mergesort([4,3,2,1]), [1,2,3,4])
    
    def test_reversed_order_odd_list(self):
        self.assertEqual(mergesort([5,4,3,2,1]), [1,2,3,4,5])

    def test_empty_list(self):
        self.assertEqual(mergesort([]), [])

    def test_single_element_list(self):
        self.assertEqual(mergesort([1]), [1])

    def test_negative_elements(self):
        self.assertEqual(mergesort([4,-5,2,-3,-2]), [-5,-3,-2,2,4])

    def test_repeating_elements(self):
        self.assertEqual(mergesort([2,2,2,3,2]), [2,2,2,2,3])

    def test_large_list(self):
        l = [ random.randint(-1000,1001) for i in range(1000000) ]
        self.assertEqual(mergesort(l), sorted(l))

    def test_mergesort_slower_than_sorted(self):
        l = [ random.randint(-1000,1001) for i in range(1000000) ]
        t1 = datetime.datetime.now()
        mergesort(l)
        t2 = datetime.datetime.now()
        sorted(l)
        t3 = datetime.datetime.now()    
        self.assertGreater(t2 - t1, t3 - t2)


if __name__ == "__main__":
    unittest.main()
