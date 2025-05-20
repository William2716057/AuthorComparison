import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import re
import nltk
from nltk.util import ngrams
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
    
#preprocess text removing punctuation and capitalisation
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return word_tokenize(text)

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
#print(authorA_punct)
#print(authorB_punct)
all_puncts = sorted(set(authorA_punct.keys()).union(set(authorB_punct.keys())))
counts_A = [authorA_punct.get(p, 0) for p in all_puncts]
counts_B = [authorB_punct.get(p, 0) for p in all_puncts]
x = range(len(all_puncts))

def sequence_matches(text1, text2, min_len=3, max_len=6):
    tokens1 = preprocess(text1)
    tokens2 = preprocess(text2)

    matches = set()
    
    for n in range(min_len, max_len +1):
        ngrams1 = set(ngrams(tokens1, n))
        ngrams2 = set(ngrams(tokens2, n))
        
        common = ngrams1.intersection(ngrams2)
        matches.update(common)
        
    return [' '.join(ng) for ng in sorted(matches)]

matches = sequence_matches(text_sample_1, text_sample_2)
for match in matches:
    print("matches: ", match)

#plt.figure(figsize=(12, 6))
#fig, top = plt.subplots(2, 4, figsize=(16, 8))
fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(3, 4, height_ratios=[1, 1, 2])  # Two rows for top grid, one for bottom bar chart
fig.suptitle("Similarities and Differences between Authors", fontsize=16)
# Top 2x4 grid (empty boxes for now)
top = []
for row in range(2):
    for col in range(4):
        ax = fig.add_subplot(gs[row, col])
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(f"Box {row*4 + col + 1}", fontsize=10)
        ax.boxplot([[]])  
        top.append(ax)

#for punctuation bar chart        
plt.bar(x, counts_A, width=0.4, label='Author A', align='center', alpha=0.7, color='skyblue')
plt.bar([i + 0.4 for i in x], counts_B, width=0.4, label='Author B', align='center', alpha=0.7, color='salmon')

plt.xticks([i + 0.2 for i in x], all_puncts, fontsize=12)
plt.figtext(0.13, 0.98, f"Avg Sentence Length Author A: {average_A:.2f}", fontsize=10, ha='left')
plt.figtext(0.13, 0.94, f"Avg Sentence Length Author B: {average_B:.2f}", fontsize=10, ha='left')

plt.title("Punctuation Style Frequency", fontsize=14)
plt.xlabel("Punctuation Mark", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()