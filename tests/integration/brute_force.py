from src.authenticate import authenticate
import itertools


def bruteForce(username):
	chars = "0123456789abcdefghijklmnopqrstuvwxyz"

	for fake_passwords in itertools.product(chars, repeat=10):
		result = authenticate(username, "".join(fake_passwords))
		if result == 'Pass':
			return "".join(fake_passwords)


if __name__ == "__main__":
	print(bruteForce('Victor'))