import unittest
from data_structures.hashset import HashSet

class TestHashSet(unittest.TestCase):

    def test_contains(self):
        h = HashSet()
        h.add(1030)
        self.assertFalse(h.contains(1031))
        self.assertTrue(h.contains(1030))
    
    def test_remove(self):
        h = HashSet()
        h.add(1030)
        self.assertTrue(h.contains(1030))
        h.remove(1030)
        self.assertFalse(h.contains(1030))

    