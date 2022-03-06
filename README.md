# CS F469: Information Retrieval

This repository contains Assignments for Information Retrieval for SEM-2 AY-2022

## A1: Boolean Retrieval System
1. This assignment is aimed at designing and developing Boolean Information Retrieval System,
i.e., to return those documents (specifically their names from corpus/dataset given: point 7 of
General Instructions) which satisfy Boolean (AND, OR and NOT with their combinations).

2. The Boolean Information Retrieval System should include the following features / pre-processing
steps:
    - Stopword Removal: Remove the common stop words from the corpus.
    - Stemming or Lemmatization: Employ either one of the techniques for normalisation.
    - Wildcard Query Handling: Any one of the techniques among Permuterm or K-Gram
index should be used for wildcard query management.
    - Spelling Correction: Edit Distance Method should be employed to correct misspelled
words.

3. Try to vectorise your code as much as possible to make your computations faster and more
efficient. Do not hard code any parts of the implementation unless it is indispensable. 

### Tech Stack 
1. NLTK
2. NumPy
3. Pandas
4. Matplotlib