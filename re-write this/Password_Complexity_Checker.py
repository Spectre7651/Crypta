password = input("Enter the password to test: ")
lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz'
uppercase_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '.,:/\!"£$%^&*()-+[]{}@#~?<>|¬` @łe¶ŧ←↓→øþæßðđŋħĸł«»¢“”nµ'
flag = 0
if len(password) >= 9:
	for i in range(len(password)):
		if password[i] in uppercase_alphabet:
			flag = flag + 1
		elif password[i] in lowercase_alphabet:
			flag = flag + 1
		elif password[i] in numbers:
			flag = flag + 1
		elif password[i] in symbols:
			flag = flag + 1
	if flag >= 3:
		print("\nThis password is complex enough")
	else:
		print("\nPassword is too basic")
else:
	print("\nPassword is too short")
