import unittest

from assignment import upper, lower


class TestAssignment(unittest.TestCase):
    def test_upper(self):
        result = upper("the new line")
        print('result u:', result)
        self.assertEqual(result, 'THE NEW LINE')

    def test_lower(self):
        result = lower("HELLO WORLD")
        print('result l:', result)
        self.assertEqual(result, 'hello world')


if __name__ == '__main__':
    unittest.main()
