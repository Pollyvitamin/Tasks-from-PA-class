"""
Create an autocomplete function that will take in an input string and a dictionary array
and return the values from the dictionary that start with the input string. 
If there are more than 5 matches, restrict your output to the first 5 results. 
If there are no matches, return an empty array. Any input that is NOT a letter should be 
treated as if it is not there. For example, an input of "$%^" should be treated as "" 
and an input of "ab*&1cd" should be treated as "abcd".
Example:
autocomplete('ai', ['airplane','airport','apple','ball']) = ['airplane','airport']
For this assignment, the dictionary will always be a valid array of strings. 
Please return all results in the order given in the dictionary, even if they're not 
always alphabetical. The search should NOT be case sensitive, but the case of the 
word should be preserved when it's returned. For example, "Apple" and "airport" would 
both return for an input of 'a'. However, they should return as "Apple" and "airport" 
in their original cases.
"""

from collections import OrderedDict

animal_dict=OrderedDict([('babirusa', 'large wild swine'),
                         ('baboon', 'large gregarious primates'),
                         ('badger', 'any of various burrowing mammals'),
                         ('bald eagle', 'an eagle of North America'),
                         ('bandicoot', 'small chiefly insectivorous and herbivorous marsupial mammals'),
                         ('banteng', 'a wild ox of southeastern Asia'),
                         ('bear', 'large heavy mammals'),
                         ('ant', 'colonial hymenopterous insects'),
                         ('alpaca', 'a domesticated mammal especially of Peru'),
                         ('arctic fox', 'a small migratory Holarctic fox')])

def autocomlete(req_definition, dictionary=animal_dict):
    """Function for searching wild animals"""
    keys =dictionary.keys()
    req_definition = "".join(filter(lambda symbol: symbol.isalpha(), req_definition))
    count = 0
    result=[]
    for key in keys:
        if count < 5 and req_definition !="":
            if req_definition.lower() == key[0:len(req_definition)]:
                count += 1
                result.append(key)
        else:
            break
    print("We found next animals:", result)

autocomlete('!!!1B23A')
