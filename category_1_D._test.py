import unittest

from category_1_D import remove_numeric_value


class TestNumericRemove(unittest.TestCase):
	def test_numeric(self):
		result =remove_numeric_value('ABCd1234efg567')
		self.assertEqual(result, 'abcdefg')

if __name__ == '__main__':
    unittest.main()