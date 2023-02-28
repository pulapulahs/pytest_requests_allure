import unittest
# 需要使用没有pytest的解释器，否则会自动按pytest来运行
from nametest import get_formatted_name


class NamesTestCases(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('the', 'eight')
        self.assertEqual(formatted_name, 'The Eight')

    def test_first_last_middle_name(self):
        formatted_name =get_formatted_name('the', 'eight', 'honey')
        self.assertEqual(formatted_name, 'The Honey Eight')


# main后需要去掉括号，否则无法运行
if __name__=="__main__":
    unittest.main

