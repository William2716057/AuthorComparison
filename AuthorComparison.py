import matplotlib.pyplot as plt
import re
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize, word_tokenize
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
#sum = for i in sentenceLength i + i
#average = sum / len(sentenceLength) 
total_length = sum(sentenceLengthAuthorA)
average_A = total_length /len(sentenceLengthAuthorA)
#print(average_A)
total_length = sum(sentenceLengthAuthorB)
average_B = total_length /len(sentenceLengthAuthorB)

plt.figure(figsize=(10, 6))

authorA_average = f"Author A:\n{average_A}"
authorB_average = f"Author B:\n{average_B}"
# Add the text to the plot
plt.text(0.1, 1.1, authorA_average, fontsize=12, color='black', wrap=True, ha='left', va='center')
plt.text(0.5, 1.1, authorB_average, fontsize=12, color='black', wrap=True, ha='left', va='center')

plt.axis('off')
plt.show()