#!usr/bin/python3
morseInput = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.-- "
morseLetters = {
".-":"a",
"-...":"b",
"-.-.":"c",
"-..":"d",
".":"e",
"..-.":"f",
"--.":"g",
"....":"h",
"..":"i",
".---":"j",
"-.-":"k",
".-..":"l",
"--":"m",
"-.":"n",
"---":"o",
".--.":"p",
"--.-":"q",
".-.":"r",
"...":"s",
"-":"t",
"..-":"u",
"...-":"v",
".--":"w",
"-..-":"x",
"-.--":"y",
"--..":"z",
"/":" "
}
number = 0
tempMorse = []
tempLetter = []
for x in morseInput:
	if morseInput[number] == " ":
		tempMorse.append("")
		tempString = ''.join(tempMorse)
		tempLetter.append(morseLetters.get(tempString))
		tempMorse = []
	elif morseInput[number] == "-" or morseInput[number] == "." or morseInput[number] == "/":
		tempMorse.append(morseInput[number])

	number = number + 1
print(''.join(tempLetter))
