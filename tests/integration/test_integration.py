import unittest
from src import my_sum

class TestSum(unittest.TestCase):
	def test_first(self):
		"""
		First test
		"""
		data = [1, 2, 3]
		result = my_sum.sum_(data)
		self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()