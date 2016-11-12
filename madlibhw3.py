# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")

import nltk # requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
import random

# import nltk
nltk.download('book')
from nltk.book import *

from nltk import word_tokenize,sent_tokenize

debug = False #True

# get file from user to make mad lib out of
if debug:
	print ("Getting information from file madlib_test.txt...\n")
fname = "madlibtest2.txt" # need a file with this name in directory

tok_lst = text2[:151]
print (type(tok_lst))

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "AV":"a adverb"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1, "AV": .10}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

print ("".join([spaced(word) for word in tok_lst]))


final_words = []

tagged_tokens = nltk.pos_tag(tok_lst)
for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))

print("\n\nEND*******")
#print new
#goal is to learn NLTK, learn about looping and Github



'''
Questions:

Where do I get text2? How do I call/incorporate it?
What is a token?
Are parts of speech built into NLTK?
How do I do 15 percent of the time? (choose random number thru 100 and if it is 1-15 then yes?)
Replace with what?
'''