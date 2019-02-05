# tachycardia.py

def main():
	tachy_out = is_tachycardic()

def is_tachycardic():

	""" User inputs a word and the program returns whether 'tachycardic' is present in the word

	:param in_word: a string argument containing a single word

	:return: a boolean value of True or False depending on the presence of the word 'tachycardic' in any form in the input
	"""
	in_word = input("Enter the word: ")

	if "tachycardic" in in_word.lower():
		tachy_out = True
	else:
		tachy_out = False

	print(tachy_out)
	return tachy_out


if __name__ == "__main__":
    main()