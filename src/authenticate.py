from hashlib import sha256
import csv




def gen_hashed_credentials():
	with open ('hashed-credentials.csv', 'w') as hcred_csv:
		h_credentials = csv.writer(hcred_csv)
		with open('credentials.csv', 'r') as cred_csv:
			credentials = csv.reader(cred_csv)
			for row in credentials:
				row[1] = sha256(row[1].encode()).hexdigest()[0:4]
				h_credentials.writerow(row)

def authenticate(username, password):
	with open('./src/hashed-credentials.csv', 'r') as hcred_csv:
		h_credentials = csv.reader(hcred_csv)
		for row in h_credentials:
			if row[0] == username:
				if row[1] == sha256(password.encode()).hexdigest()[0:4]:
					return 'Pass'
	return 'Fail'

if __name__ == "__main__":
	gen_hashed_credentials()
	print(authenticate('Alice', 'pass123'))