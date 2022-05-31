import unittest

from assignment import upper, lower, given_string_valid


class TestAssignment(unittest.TestCase):
    def test_upper(self):
        result = upper("the new line")
        print('result u:', result)
        self.assertEqual(result, 'THE NEW LINE')

    def test_lower(self):
        result = lower("HELLO WORLD")
        print('result l:', result)
        self.assertEqual(result, 'hello world')

    def test_valid_string(self):
        result_1 = given_string_valid('sss')
        print('result_1:', result_1)
        self.assertTrue(result_1)


if __name__ == '__main__':
    unittest.main()
