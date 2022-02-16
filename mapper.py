#!/usr/bin/env python
import sys
import re
# import to use functions from sys
# import re for regular expressions

# list of punctuation types for our regular expression
pattern = r"[.?!*&()\[],:;'']+"

# stdin = standard input (similar to using the actual input function)
# All words in the text will be read as a separate input
for line in sys.stdin:

    #strip white spaces at beginning and end of line
    line = line.strip()

    #split each line up
    words = line.split()

    # iterate through the word in "words"
    for word in words:
        # Now, use a regular expression to eliminate all digits from any words
        word = re.sub(r'[0-9]+','',word)
        # Reg expression to extract punctuation
        word = re.findall(r"[\w']+|[.,!?;]", word)
        
        # Pass over any blank spaces
        for word in word:
            if word == '':
                pass
            # Assign each lower case word a value of 1
            else:
                print(word.lower() + "\t" + '1')
        
#In terminal: Use the following to test
#echo 'a quick brown! fox?? jumps, 8over a &* lazy dog 99'|./mapper.py


#shebang
#mapper - breaking up words into units
