'''
    An interactive dictionary using data from a json file
'''

import json
# import difflib # library to compare text
from difflib import get_close_matches

data = json.load(open("data.json")) # to load data

def translate(word):
    word = word.lower() # makes input case sensitive

    # need to handle edge cases
    if word in data:
        return data[word]
    elif word.title() in data:    # if user enters a proper noun
        return data[word.title()] # also if user enters 'texas' over 'Texas'
                                  # code will not break
    elif word.upper() in data: # in case user enters USA or NATO
        return data[word.upper()]
    # let the user know if the word entered was incorrect
    elif len(get_close_matches(word, data.keys())) > 0:
        # the \ here separates multiline code
        # yn is yes or no
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " \
                    % get_close_matches(word, data.keys())[0])
        # the below if condition is the same as if (yn == "Y" || yn == "y")
        if yn in ("Y", "y"): # if yes, using tuple for edge case
            return data[get_close_matches(word, data.keys())[0]]
        elif yn in ("N", "n"):
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand your query."
    else:
        return "The word doesn't exist. Please double check it"

word = input("Enter word: ") # ask for user input

# print(translate(word))
output = translate(word)

# pretty printing
# Note: This will iterate through the else message and print each char on
# its own line if not checked properly!
if type(output) == list: # so if output is list
    for item in output:
        print(item)
else: # else (it would be a string)
    print(output)
