import re 

def convertRomanNumeralToArabicNumber(s):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    prev = 0
    total = 0
    for c in s:
        if c not in roman_values:
            return False
        val = roman_values[c]
        if val > prev:
            total += val - 2 * prev
        else:
            total += val
        prev = val
    return True

def validateRomanNumeral(s):
    # create new function to validate roman numeral
    # return true if valid
    # return false if invalid
    # use regex to validate

    # check if string is empty
    if s == "":
        return False

    # check if string is a valid roman numeral
    if not re.match(r'^[MDCLXVI]+$', s):
        return False
    else: 
        return True
