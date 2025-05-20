# Author Comparison Tool

A Python script that helps analyse and compare writing styles between two text samples. This can be useful in determining authorship by highlighting stylistic similarities and differences by assessing various linguistic features.

## Features

### 1. Preprocessing
- Converts all text to lowercase.
- Removes punctuation.
- Tokenizes text using NLTK's word_tokenize for consistent word-level analysis.

### 2. Sentence Length Analysis
- Tokenizes sentences using NLTK's sent_tokenize.
- Calculates the number of words per sentence.
- Computes the average sentence length for each author.
- Useful to detect verbosity or concise writing patterns.

### 3. Punctuation Style
- Counts the frequency of each punctuation mark such as question marks, periods or commas.
- Compares usage patterns visually between both samples.
- Helps detect stylistic nuances such as the use of ellipses, dashes, or exclamation points.

### 4. Matching Phrase Sequences

-Generates overlapping n-grams (3–6 word phrases) from both texts.
- Identifies common multi-word expressions or repeated structures.
- Useful for finding common phrases or quotes that individuals may use in writing. 

### 5. Function word usage 
- Focuses on common grammatical words that serve to express relationship between other words ("the", "and", "but", "or", "if", "when", "while", "as", "to", "in", "of", "on", "with", "by", "at", "for").
- These can serve as stylistic fingerprints.
- Visual comparison can show which words are favored by each author.

### 6. Lexical Richness
- Calculates the Type-Token Ratio (TTR):
- This can show richness and complexity in vocabulary
```
TTR = Unique Words / Total Words
```
- Higher values imply varied vocabulary; lower values may suggest repetition or simplicity.

### 7. Visual Comparison (via matplotlib)
- Bar charts and subplots clearly display:
- Punctuation frequency
- Function word usage
- Lexical richness
- Summary insights with common phrases and average sentence lengths

## Usage
1. Place your two text files in the same directory (e.g., authorA.txt and authorB.txt).
2. install dependencies
```
pip install matplotlib nltk numpy
```
3. Run the script in Python:
```
python3 AuthorComparison.py
```

![sample](https://github.com/user-attachments/assets/d8c2af76-9829-49a7-bec9-658dbf5dc040)
