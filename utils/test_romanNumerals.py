import unittest
from romanNumerals import convertRomanNumeralToArabicNumber, validateRomanNumeral

class TestRomanNumerals(unittest.TestCase):

    def test_convertRomanNumeralToArabicNumber(self):
        self.assertEqual(convertRomanNumeralToArabicNumber("I"), 1)
        self.assertEqual(convertRomanNumeralToArabicNumber("IV"), 4)
        self.assertEqual(convertRomanNumeralToArabicNumber("IX"), 9)
        self.assertEqual(convertRomanNumeralToArabicNumber("LVIII"), 58)
        self.assertEqual(convertRomanNumeralToArabicNumber("MCMXCIV"), 1994)

    def test_validateRomanNumeral(self):
        self.assertTrue(validateRomanNumeral("I"))
        self.assertTrue(validateRomanNumeral("IV"))
        self.assertTrue(validateRomanNumeral("IX"))
        self.assertTrue(validateRomanNumeral("LVIII"))
        self.assertTrue(validateRomanNumeral("MCMXCIV"))
        self.assertFalse(validateRomanNumeral("IIII"))
        self.assertFalse(validateRomanNumeral("VX"))
        self.assertFalse(validateRomanNumeral("ABC"))
        self.assertFalse(validateRomanNumeral(""))

if __name__ == '__main__':
    unittest.main()