# tachycardia.py


def main():
    in_word = input("Enter the word: ")
    tachy_out = is_tachycardic(in_word)


def is_tachycardic(in_word):

    """ User inputs a word and the script returns whether 'tachycardic' is present

    :param in_word: string argument containing a single word

    :return: boolean value depending on presence of 'tachycardic' in the input
    """
    if "tachycardic" in in_word.lower():
        tachy_out = True
    else:
        tachy_out = False

    print(tachy_out)
    return tachy_out


if __name__ == "__main__":
    main()
