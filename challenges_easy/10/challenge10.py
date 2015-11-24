#/usr/bin/python3
import re
phoneValidation = re.compile('^((\(?0\d{4}\)?\s?\d{3}\s?\d{3})|(\(?0\d{3}\)?\s?\d{3}\s?\d{4})|(\(?0\d{2}\)?\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$')

userPhone = input("Please enter a phone number ")

match = phoneValidation.match(userPhone)

if match.group() == userPhone:
	print("This is a correct phone number!")
else:
	print("INCORRECT!")
