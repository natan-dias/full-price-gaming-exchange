import unittest

class MyTestCase(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()