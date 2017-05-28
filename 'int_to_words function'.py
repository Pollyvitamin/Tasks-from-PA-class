"""
Create an function int_to_words that translates integers to words.
For a given positive integer convert it into its English representation. 
All words are lower case and are separated with one space. 
No trailing spaces are allowed. Integer will be up to a million (including).
int_to_words(15) # => 'fifteen'
 
Writing of the word 'and' isn't enforced, but very welcomed.
int_to_words(12356) # => 'twelve thousand three hundred and fifty six'
"""

def int_to_words(number):
  """Function that translates integers to words"""
  numbers_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                  6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                  11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                  15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
                  19: 'nineteen', 20: 'twenty',
                  30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
                  70: 'seventy', 80: 'eighty', 90: 'ninety'}

  kilo = 1000
  million = kilo * 1000
  billion = million * 1000

  if number >= 0:

    if number < 20:
      return numbers_dict[number]

    if number < 100:
      if number % 10:
        return numbers_dict[(number // 10) * 10] + ' ' + numbers_dict[number % 10]
      else:
        return numbers_dict[number]

    if number < kilo:
      if number % 100:
        return numbers_dict[number // 100] + ' hundred and ' + int_to_words(number % 100)
      else:
        return numbers_dict[number // 100] + ' hundred'

    if number < million:
      if number % kilo:
        return int_to_words(number // kilo) + ' thousand ' + int_to_words(number % kilo)
      else:
        return int_to_words(number // kilo) + ' thousand'

    if number < billion:
      if number % million:
        return int_to_words(number // million) + ' million ' + int_to_words(number % million)
      else:
        return int_to_words(number // million) + ' million'
        
    if number >= billion:
      return 'You entered too large number'
      
  else:
    return 'You entered negative number'
