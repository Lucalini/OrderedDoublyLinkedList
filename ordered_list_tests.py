import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_is_empty(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list.add(5)
        self.assertFalse(t_list.is_empty())
    def test_add_then_listmethods(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(2)
        t_list.add(3)
        t_list.add(4)
        self.assertEqual(t_list.python_list(), [1,2,3,4])
        self.assertEqual(t_list.python_list_reversed(), [4,3,2,1])
    def test_search(self):
        t_list = OrderedList()
        t_list.add(50)
        t_list.add(8)
        t_list.add(4)
        t_list.add(42)
        self.assertTrue(t_list.search(8))
        self.assertFalse(t_list.search(59))
    def test_remove(self):
        t_list = OrderedList()
        t_list.add(50)
        t_list.add(8)
        t_list.add(4)
        t_list.add(42)
        self.assertTrue(t_list.remove(8))
        self.assertFalse(t_list.remove(8))
        t_list.add(42)
        self.assertTrue(t_list.remove(42))
        self.assertFalse(t_list.remove(42))

    def test_index(self):
        t_list = OrderedList()
        self.assertEqual(t_list.index(5), None)
        t_list.add(50)
        t_list.add(8)
        t_list.add(4)
        t_list.add(42)
        self.assertEqual(t_list.index(42), 2)
        self.assertEqual(t_list.index(4), 0)

    def test_size(self):
        t_list = OrderedList()
        self.assertEqual(t_list.size(), 0)
        t_list.add(50)
        t_list.pop(0)
        self.assertEqual(t_list.size(), 0)
        t_list.add(50)
        t_list.add(8)
        t_list.add(4)
        t_list.add(42)
        self.assertEqual(t_list.size(), 4)
        t_list.remove(42)
        self.assertEqual(t_list.size(), 3)

    def test_pop(self):
        t_list = OrderedList()
        t_list.add(50)
        t_list.add(8)
        t_list.add(4)
        t_list.add(42)
        self.assertEqual(t_list.pop(2), 42)
        self.assertEqual(t_list.size(), 3)
        with self.assertRaises(IndexError):
            t_list.pop(58)


if __name__ == '__main__': 
    unittest.main()
