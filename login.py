import os
from sys import argv
#script, user_name = argv

password = {'trungnt': 'msb123', 'thanhnt': 'sea123'}

print("Hello world!")
user = raw_input("Enter user name: ")
pas  = raw_input("Enter pass word: ")
if user in ['trungnt', 'thanhnt']:
	if pas == password[user]:
		print "Welcome to TKT,", user
	else:
		print "Password is wrong"
else:
	print "User %s doesn't exist, please exit now." % user

finish = raw_input("\nClear screen: Y/N?	")
while finish not in ['Y', 'y', 'N', 'n']:
	finish = raw_input("Clear screen: Y/N?	")

if finish == "Y" or finish == "y":
	os.system('cls')