# Readability test is the Coleman-Liau index.
# The Coleman-Liau index of a text is designed to output what
# grade level is needed to understand the text

from cs50 import get_string
import re

text  = get_string("Text: ")

#Calculate number of sentences in given text
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
s = len(sentences) - 1

#Calculate count of words in given text
words = text.split()
w = len(words)

#Clean text, remove all spaces and spacial characters
clean_text = re.sub(r'[^a-zA-Z]',r'', text)
l = 0
for letters in clean_text:
    l += 1

#Readability index calculation:
#0.0588 * L - 0.296 * S - 15.8
#where L is the average number of letters per 100 words in the text,
#and S is the average number of sentences per 100 words in the text.
index = 0.0588 * (100 * l / w) - 0.296 * (100 * s / w) - 15.8
grade = int(round(index, 0))

#Print out Grade
if grade < 1:
    print("Before Grade 1")
elif grade >= 1 and grade <= 16:
    print("Grade " + str(grade))
else:
    print("Grade 16+")
