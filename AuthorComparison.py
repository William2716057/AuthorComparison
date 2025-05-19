import matplotlib.pyplot as plt
import re
import nltk
from numpy import count_nonzero
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize, word_tokenize
import string
from collections import Counter
#from spellchecker import Spellchecker

region_dict = {
    "color": "colour",
    "flavor": "flavour",
    "honor": "honour",
    "organize": "organise",
    "realize": "realise",
    "analyze": "analyse",
    "center": "centre",
    "meter": "metre",
    "theater": "theatre",
    "defense": "defence",
    "offense": "offence",
    "traveling": "travelling",
    "canceled": "cancelled",
    "modeling": "modelling",
    "labeled": "labelled",
    "check": "cheque",  
    "gray": "grey",
    "plow": "plough",
    "aluminum": "aluminium",
    "program": "programme",  
}


#add two text samples
#use various algorithms to get fingerprints of each text
#use matplotlib to display similarities visually
#let user interpret results

#average sentence length
#punctuation style
#word sequence matches
#identify region
#spellcheck
#if digit or alpha digit compare to text 2
#sentiment analysis 

text_sample_1 = "authorA.txt"
text_sample_2 = "authorB.txt"

with open(text_sample_1, "r", encoding="utf-8") as file:
    text_sample_1 = file.read()
    
with open(text_sample_2, "r", encoding="utf-8") as file:
    text_sample_2 = file.read()
    
def sentence_length(text1):
    sentences = sent_tokenize(text1)
    sentence_lengths = []  
    for sentence in sentences:
        words = word_tokenize(sentence)
        sentence_lengths.append(len(words))  
    
    return sentence_lengths 

# Call the function for text_sample_1 and print the results
sentenceLengthAuthorA = sentence_length(text_sample_1)
sentenceLengthAuthorB = sentence_length(text_sample_2)
average_A = sum(sentenceLengthAuthorA) / len(sentenceLengthAuthorA)
average_B = sum(sentenceLengthAuthorB) / len(sentenceLengthAuthorB)

#punctuation style
def count_punctuation(text):
    punctuation_marks = [char for char in text if char in string.punctuation]
    return dict(Counter(punctuation_marks))

authorA_punct = count_punctuation(text_sample_1)
authorB_punct = count_punctuation(text_sample_2)
print(authorA_punct)
print(authorB_punct)

all_puncts = sorted(set(authorA_punct.keys()).union(set(authorB_punct.keys())))
counts_A = [authorA_punct.get(p, 0) for p in all_puncts]
counts_B = [authorB_punct.get(p, 0) for p in all_puncts]

x = range(len(all_puncts))

plt.bar(x, counts_A, width=0.4, label='Author A', align='center', alpha=0.7)
plt.bar([i + 0.4 for i in x], counts_B, width=0.4, label='Author B', align='center', alpha=0.7)

authorA_average = f"Average Sentence Length Author A:\n{average_A}"
authorB_average = f"Average Sentence Length Author B:\n{average_B}"
# Add the text to the plot
plt.figure(figsize=(10, 6))
plt.text(0.1, 1.1, authorA_average, fontsize=12, color='black', wrap=True, ha='left', va='center')
plt.text(0.5, 1.1, authorB_average, fontsize=12, color='black', wrap=True, ha='left', va='center')

plt.axis('off')
plt.show()