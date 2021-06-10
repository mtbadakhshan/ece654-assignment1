import unittest
from src.authenticate import authenticate

class TestSum(unittest.TestCase):


	def test_true_negative(self):
		# True negative
		result = authenticate('Alice', 'pass123')
		self.assertEqual(result, 'Pass')
		result = authenticate('Bob', 'uwaterloo')
		self.assertEqual(result, 'Pass')
		result = authenticate('Peggy', 'canada')
		self.assertEqual(result, 'Pass')
		result = authenticate('Victor', 'ece657')
		self.assertEqual(result, 'Pass')

	def test_true_positive(self):
		# true positive
		result = authenticate('Eve', 'hacker')
		self.assertEqual(result, 'Fail')
		result = authenticate('Alice', 'malicious')
		self.assertEqual(result, 'Fail')
		result = authenticate('Eve', 'pass123')
		self.assertEqual(result, 'Fail')

	def test_false_negative(self):
		# false negative
		result = authenticate('Alice', '0000002efr')
		self.assertEqual(result, 'Pass')
		result = authenticate('Bob', '0000000140')
		self.assertEqual(result, 'Pass')
		result = authenticate('Peggy', '0000007mgv')
		self.assertEqual(result, 'Pass')
		result = authenticate('Victor', '00000000kh')
		self.assertEqual(result, 'Pass')



if __name__ == '__main__':
    unittest.main()