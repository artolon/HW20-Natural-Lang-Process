#!/usr/bin/env python
import sys

# These are all just placeholders 
current_word = None
current_count = 0
word = None
# take all the words from the mapper and count the existence of the words

# lines passed from the mapper.py program
for line in sys.stdin:

    # strip the white spaces from beginning/end of line
    line = line.strip()

    # split the words and assign count of 1
    word, count = line.split("\t", 1) # split only on a single tab

    # Now, we need to aggregate them together
    # Make sure it is an integer
    count = int(count)

    # sorted values from command line are passed in and 
    # if we have two of the same word, we increment the count per instance of the word
    if current_word == word:
        current_count += count
    
    else:
        # if there IS a current word and it's not "None" 
        if current_word:
            print(str(current_count) + "\t" + current_word)

        current_count = count 
        current_word = word
# Ensure current count is first so that we can sort by frequency in command line    
if current_word == word:
    print(str(current_count) + "\t" + current_word)

# In terminaL:
# echo 'a quick brown fox! jumps over a lazy FOX? fox *& fox'|./mapper.py|sort|./reducer.py|sort
# cat cats_txt.txt | python mapper.py | sort | python reducer.py | sort -g

