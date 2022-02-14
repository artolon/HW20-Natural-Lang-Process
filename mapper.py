#!/usr/bin/env python
import sys
import re
# import to use functions from sys

# list of punctuation types
punctuation = '''!()-[];:'"\,<>./?@#$%^&*_~""'''

# stdin = standard input (similar to using the actual input function)
# All words in the text will be read as a separate input
for line in sys.stdin:

    #strip white spaces at beginning and end of line
    line = line.strip()

    #split each line up
    words = line.split()

    # iterate through the word in "words"
    for word in words:
        # iterate through characters in word
        for char in word:
            # see if a character is in the punctuation list
            if char in punctuation:
                # If so, replace it with nothing
                word = word.replace(char, "")
        
        # Now, use a regular expression to eliminate all digits from any words
        word = re.sub(r'[0-9]+','',word)
        
        # Check if a word is now empty (i.e. only special characters)
        # If empty, pass so we don't get errors in reducer
        if word == '':
            pass
        # If not empty, execute the following
        else:
            # Ensure the words are lowercase for the mapping
            # process each word and assign value of 1 to each word
            print(word.lower() + "\t" + '1')



#In terminal: Use the following to test
#echo 'a quick brown! fox?? jumps, 8over a &* lazy dog 99'|./mapper.py


#shebang
#mapper - breaking up words into units
