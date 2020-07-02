import random
def password_gen(website):
	lower = "abcdefghijklmnopqrstuvwxyz"
	capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	symbol = "!@#$%^&*()"
	characters = lower + capital + symbol
	length = 12
	password = "".join(random.sample(characters,length))
	full_string = "\n" + website + ": " + password
	f = open("passwords.txt","a+")
	f.write(full_string)
	f.close()

password_gen("gmail")