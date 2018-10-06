def SwapCase(Str):
    Final_Str = ""
    for letter in Str:
        if letter.isupper():
            Final_Str += letter.lower()
        elif letter.islower():
            Final_Str += letter.upper()
        else:
            Final_Str += letter
    return Final_Str
