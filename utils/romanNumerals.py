import re 

def convertRomanNumeralToArabicNumber(s):
    # create new function to convert roman numeral to arabic number
    # return arabic number
    # use dictionary to map roman numeral to arabic number

    # create dictionary to map roman numeral to arabic number
    romanToArabic = {
        "M": 1000,
        "D": 500, 
        "C": 100, 
        "L": 50, 
        "X": 10, 
        "V": 5, 
        "I": 1
    }

    # create variable to hold arabic number
    arabicNumber = 0

    # loop through roman numeral
    for i in range(len(s)):
        # check if current roman numeral is less than next roman numeral
        if i + 1 < len(s) and romanToArabic[s[i]] < romanToArabic[s[i + 1]]:
            # subtract current roman numeral from arabic number
            arabicNumber -= romanToArabic[s[i]]
        else:
            # add current roman numeral to arabic number
            arabicNumber += romanToArabic[s[i]]

    # return arabic number
    return arabicNumber

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
