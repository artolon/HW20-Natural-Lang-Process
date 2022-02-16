# Homework20 - Natural Language Processing

This homework assignment focused on natural language processing. Primary skills included: Map and reduce, regular expressions, tokenizing words/sentences, stemming, lematizing, and sentiment analysis. 

### 1. Write a python program (not a Jupyter notebook, but a py file you run from the command line) that accepts the cats_txt.txt file as input and counts the frequency of all words and punctuation in that text file, ordered by frequency. Make sure to handle capital and lowercase versions of words and count them together.
- The code for this question can be found in the mapper.py and reducer.py files, which are both saved to this repo

### 2. Document how to run the program you created in question 1 in a readme.md file in your repo. Be as clear as possible. Use proper markdown, and consider using screenshots. Be sure to briefly discuss why this kind of exercise might be helpful for NLP in your markdown.

**How to run this program**
- First, open a terminal, whether through the command prompt, git bash, or within VSCode, etc. 
- Next call the text file and/or string that you would like to input
-  If using a file, please use the following syntax

$ cat cats_txt.txt | python mapper.py | sort | python reducer.py | sort -g

- 'cat' concatenates the file and properly reads it in. 
- The | operator is next. Then we pipe in the 'python mapper.py' command, which prompts the application of the python program
- We use another | to sort the words
- Next, we call the reducer python program on our file
- Finally, we sort the entire output
- the -g at the end allows us to sort anything that "looks like a number" as a number
- The resulting output should separate words and punctuation like so:


![mr_sn1](https://user-images.githubusercontent.com/59490033/154196280-c1803bae-178e-4e3e-ab56-51aae2ca349d.PNG)
![mr_sn2](https://user-images.githubusercontent.com/59490033/154196305-571143fb-d2fe-4459-a187-1c2d3c4196a3.PNG)

- If running the code on a string, simply pass in the string as follows:
- *Please note: This sentence intentionally has a lot of random characters, simply to display how the program operates. This program was also designed to remove numbers.*

![mr_sn3](https://user-images.githubusercontent.com/59490033/154196401-ca92a450-2db6-4f78-a432-b5e794cf6f61.PNG)
![mr_sn4](https://user-images.githubusercontent.com/59490033/154196534-2e86911e-94ee-4565-9cb9-d24d19e8953a.PNG)

**How this can be helpful for NLP**

- In order to analyze large volumes of text, it can be essential to strip words of punctuation and capitalization. This allows us to more easily count word frequencies and/or later compute higher level analyses. For example, this can allow us to run a sentiment analysis on larger bodies of text. Basically, converting language to numerical data can help us gain insight into what would otherwise be unstructed and less practical for modeling. 
