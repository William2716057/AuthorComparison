import matplotlib as plt
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
    
#print(text_sample_1)
#print(text_sample_2)