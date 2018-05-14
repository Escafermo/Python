def two_words_same_first_letter(text):
    textlst = text.split()
    if textlst[0][0].lower() == textlst[1][0].lower():
        return True
    else:
        return False