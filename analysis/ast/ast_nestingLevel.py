import ast


def rec_walk(node, cnt=0):
	max_child_lvl=0
	n_child = 0

	for child in ast.iter_child_nodes(node):
		n_child += 1 #To find leaves of the tree
		
		if isinstance(child, ast.For) or \
			isinstance(child, ast.AsyncFor) or \
			isinstance(child, ast.While) or \
			isinstance(child, ast.Try) or \
			isinstance(child, ast.With) or \
			isinstance(child, ast.AsyncWith) or \
			isinstance(child, ast.FunctionDef) or \
			isinstance(child, ast.AsyncFunctionDef) or \
			isinstance(child, ast.ClassDef) or \
			isinstance(child, ast.If):

			child_lvl = rec_walk(child, cnt+1)
		else:
			child_lvl = rec_walk(child, cnt)
		if child_lvl > max_child_lvl:
			max_child_lvl = child_lvl

	if n_child == 0: # The node is a leaf
		return cnt
	else:
		return max_child_lvl



def ctrlstr_nstlvl(pyfile, max=-1):
	with open(pyfile, 'r') as source:
		tree = ast.parse(source.read())

	ast.NodeVisitor()
	print(rec_walk(tree))

if __name__ == '__main__':
	pyfile = "../../src/my_power.py"
	# pyfile = "ast_nestingLevel.py"
	ctrlstr_nstlvl(pyfile)


