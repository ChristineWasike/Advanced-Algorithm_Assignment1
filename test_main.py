import unittest

from main import sock_merchant


class test_main(unittest.TestCase):
    def test_case1(self):
        test_nums = 10
        test_list = [1, 2, 1, 3, 4, 2, 5, 4, 1, 3]
        self.assertEqual(4, sock_merchant(test_nums, test_list))

    def test_case2(self):
        test_nums = 7
        test_list = [1, 2, 1, 2, 1, 3, 2]
        self.assertEqual(2, sock_merchant(test_nums, test_list))

    def test_case3(self):
        test_nums = 9
        test_list = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        self.assertEqual(3, sock_merchant(test_nums, test_list))

    def test_case4(self):
        test_nums = 10
        test_list = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
        self.assertEqual(4, sock_merchant(test_nums, test_list))

    # Based on rubric
    def test_case5(self):
        test_nums = 30
        test_list = [5, 8, 5, 5, 1, 7, 6, 2, 1, 3, 6, 3, 4, 1, 8, 4, 8, 3, 6, 7, 0, 3, 3, 9, 4, 4, 8, 4, 7, 8]
        self.assertEqual(10, sock_merchant(test_nums, test_list))

    # Based on rubric
    def test_case6(self):
        test_nums = 80
        test_list = [4, 19, 9, 16, 19, 4, 18, 5, 15, 4, 19, 6, 7, 2, 3, 1, 3, 7, 0, 19, 12, 6, 18, 6, 8, 0, 6, 11, 8, 2,
                     13, 2, 3, 18, 11, 17, 5, 7, 13, 12, 13, 6, 18, 8, 12, 2, 5, 10, 0, 16, 2, 7, 5, 8, 19, 11, 11, 15,
                     1, 3, 5, 13, 11, 4, 7, 17, 5, 12, 13, 17, 19, 17, 2, 15, 14, 6, 14, 0, 0, 5]
        self.assertEqual(36, sock_merchant(test_nums, test_list))
