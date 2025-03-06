import unittest
from kata import add

class TestKataMethods(unittest.TestCase):

    def test_wrong_arg_type(self):
        self.assertEqual(add(1), "Invalid input")

    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_one_number(self):
        self.assertEqual(add("1"), 1)
    
    def test_multiple_numbers(self):
        self.assertEqual(add("1,5"), 6)

    def test_new_lines(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_many_numbers_with_new_lines(self):
        self.assertEqual(add("1\n2,3\n4,5"), 15)

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            add("-1,2")
        err = context.exception
        self.assertEqual(str(err), "negative numbers not allowed : [-1]")

if __name__ == '__main__':
    unittest.main()