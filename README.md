# Amazon-Reviews---NLP-Sentiment-and-Similairy
Python program that performs sentiment and similarity analysis using a NLP model

## Table of Contents:
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Overview:
Python application designed to perform sentiment analysis on customer reviews obtained from the Amazon Product Reviews dataset. 
It utilizes natural language processing (NLP) techniques to analyze the sentiment expressed in each review and provides insights into whether the sentiment is positive, negative, or neutral.
Also compares the similarity between two reviews.

## Features:
- Preprocessing: The program includes preprocessing steps such as tokenization, lowercasing, stop word removal, and punctuation removal to prepare the text data for sentiment analysis.
- Sentiment Analysis: It applies sentiment analysis techniques to determine the overall sentiment polarity of each review, classifying it as positive, negative, or neutral based on the sentiment score.
- Similarity Comparison: Additionally, the program compares the similarity between two randomly selected reviews from the dataset.

## Installation:
1. Make sure you have Python and Pip installed onto your system.
2. Install the "amazon_product_reviews.rar".
3. Install the following Python packages:
   - Pandas - pip install pandas.
   - Spacy - pip install spacy.
   - Spacytextblob - pip install spacytextblob.
4. Install NLP models:
   - English Small NLP model - python -m spacy download en_core_web_sm.
   - English Medium NLP model - python -m spacy download en_core_web_md.

## Usage:
   1. Clone the repository into a folder in your local machine.
   2. Extract the "amazon_product_reviews.rar" file into the same directory.
   3. Run Python file (sentiement_analysis.py).
   4. Compare the sentiment analysis on any Amazon reviews by changing the selected index on line 50.
![Screenshot](https://github.com/manfoonhau/Amazon-Reviews---NLP-Sentiment-and-Similairy/blob/main/sentiment.png)
   5. Run the Python script.

## Credits:
Developer - [Calvin Hau](https://github.com/manfoonhau) 



