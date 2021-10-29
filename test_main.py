import unittest

from main import sock_merchant


class test_main(unittest.TestCase):
    def test_case1(self):
        test_nums = 10
        test_list = [1, 2, 1, 3, 4, 2, 5, 4, 1, 3]
        self.assertEqual(sock_merchant(test_nums, test_list), 4)

    def test_case2(self):
        test_nums = 7
        test_list = [1, 2, 1, 2, 1, 3, 2]
        self.assertEqual(sock_merchant(test_nums, test_list), 2)

    def test_case3(self):
        test_nums = 9
        test_list = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        self.assertEqual(sock_merchant(test_nums, test_list), 3)

    def test_case4(self):
        test_nums = 10
        test_list = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
        self.assertEqual(sock_merchant(test_nums, test_list), 4)
