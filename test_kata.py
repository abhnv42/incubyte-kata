import unittest
from kata import add

class TestKataMethods(unittest.TestCase):
    def test_empty_string(self):
        # Assuming some_method should return True for input 1
        self.assertEqual(add(""), 0)

if __name__ == '__main__':
    unittest.main()