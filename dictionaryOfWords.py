"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

word_definitions = {
    "stuff": "matter, material, articles, or activities of a specified or indeterminate kind that are being referred to, indicated, or implied",
    "thing": "an object that one need not, cannot, or does not wish to give a specific name to"
}

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["name"] = "a word or set of words by which a person, animal, place, or thing is known, addressed, or referred to"
word_definitions["breed"] = "a stock of animals or plants within a species having a distinctive appearance and typically having been developed by deliberate selection"
word_definitions["age"] = "the length of time that a person has lived or a thing has existed"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for (key, value) in word_definitions.items():
    print((f'The definition of {key} is {value}'))
