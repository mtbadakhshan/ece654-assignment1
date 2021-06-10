import ast

def get_identifiers(pyfile):
	with open(pyfile, 'r') as source:
		tree = ast.parse(source.read())
	identifiers = []
	# The definition of identifiers is selected according to 
	# https://docs.python.org/3/library/ast.html
	for node in ast.walk(tree):
		if hasattr(node, 'name'):
			# print('name: ',node.name)
			identifiers.append(node.name)
		elif hasattr(node, 'id'):
			# print('id: ',node.id)
			identifiers.append(node.id)

		elif hasattr(node, 'attr'):
			# print('attr: ',node.attr)
			identifiers.append(node.attr)

		elif hasattr(node, 'arg'):
			# print('arg: ',node.arg)
			identifiers.append(node.arg)

		elif hasattr(node, 'asname'):
			# print('asname: ',node.asname)
			identifiers.append(node.asname)
		
	return set(identifiers)
	


if __name__ == '__main__':
	pyfile = "../../src/my_sum.py"
	print(get_identifiers(pyfile))

