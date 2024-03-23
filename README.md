# Amazon-Reviews---NLP-Sentiment-and-Similairy
Python program that performs sentiment and similarity analysis using a NLP model

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

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
2. Clone the repository into a folder in your local machine
3. Install the "amazon_product_reviews.rar" file and extract into the same directory.
4. Install the following Python packages:
   - Pandas - pip install pandas
   - Spacy - pip install spacy
   - Spacytextblob - pip install spacytextblob
5. Install NLP models:
   - English Small NLP model - python -m spacy download en_core_web_sm
   - English Medium NLP model - python -m spacy download en_core_web_md
