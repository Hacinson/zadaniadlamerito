def decapitalize_first_letter(s):
    if len(s) == 0:
        return ''
    else:
        return s[0].lower() + s[1:]

string = "Cheval Where Are You???"
result = decapitalize_first_letter(string)
print(string)
print(result)
