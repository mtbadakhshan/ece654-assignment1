import unittest
from src.authenticate import authenticate
from analysis.ast import ast_identifiers
from analysis.ast import ast_nestingLevel


class TestAuth(unittest.TestCase):


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

	def test_ast_identifiers_length(self):
		#Check that there are no identifiers with length equal 13
		result = ast_identifiers.is_any_identifier_with_length_n('src/authenticate.py', 13)
		self.assertTrue(result)

	def test_ast_nesting_level(self):
		#Maximum control structure nesting is 4
		result = ast_nestingLevel.ctrlstr_nstlvl('src/authenticate.py')
		self.assertTrue(result <= 4)




if __name__ == '__main__':
    unittest.main()