# Author Comparison Tool

A Python script that helps analyse and compare writing styles between two text samples. This can be useful in determining authorship by highlighting stylistic similarities and differences by assessing various linguistic features.

## Features

1. Preprocessing
- Converts all text to lowercase.
- Removes punctuation.
- Tokenizes text using NLTK's word_tokenize for consistent word-level analysis.

2. Sentence Length Analysis
- Tokenizes sentences using NLTK's sent_tokenize.
- Calculates the number of words per sentence.
- Computes the average sentence length for each author.
- Useful to detect verbosity or concise writing patterns.

