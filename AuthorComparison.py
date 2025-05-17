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
#print("Author A")
#print(sentenceLengthAuthorA)

# Optionally, you can call the function for text_sample_2 as well
sentenceLengthAuthorB = sentence_length(text_sample_2)
plt.figure(figsize=(10, 6))

# Plot the histogram
plt.hist(sentenceLengthAuthorA, bins=5, color='blue', alpha=0.7)

# Add title and labels
#plt.title("Sentence Length Distribution - Author A")
#plt.xlabel("Sentence Length (Words)")
#plt.ylabel("Frequency")

# Add a label with text (e.g., list of sentence lengths)
text = f"Sentence lengths: {', '.join(map(str, sentenceLengthAuthorA))}"
# Position the text at an appropriate location
plt.text(15, 3, text, fontsize=10, color='black', wrap=True)

# Show the plot
plt.show()
#.hist(sentenceLengthAuthorA, bins=20, color='blue', alpha=0.7)  # Plot histogram
# Add labels and title
#plt.title("Sentence Length Distribution - Author A")
#plt.xlabel("Sentence Length (Words)")
#plt.ylabel("Frequency")

# Display the plot

#print("Author B")
#print(sentenceLengthAuthorB)
#def sentence_length(text1, text2): 
        #split sentences 
        
        #two_texts = text1 + " " + text2
        
#        sentences_1 = re.split(r'(?<=[.!?]) +', text1)
        #text1 = sentences(two_texts)
#        print("Author A")
#        for sentence in sentences_1:
            
#            print(len(sentence))

        #sentence_lengths = [len(sentences) for sentence in sentences]
 #       sentences_2 = re.split(r'(?<=[.!?]) +', text2)
#        print("Author B")
 #       for sentence in sentences_2:
#            print(len(sentence))
        
        #return sentence_lengths
#sentence_length(text_sample_1, text_sample_2)
#lengths = sentence_length(text_sample_1, text_sample_2)
#print(lengths)

#print(text_sample_1)
#print(text_sample_2)