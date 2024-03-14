
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

#Load NLP model and TextBlob Extenstion
nlp = spacy.load('en_core_web_sm')
nlp2 = spacy.load('en_core_web_md')
nlp.add_pipe('spacytextblob')

#Load Dataset
df = pd.read_csv('amazon_product_reviews.csv')

#Function for preprocessing / cleaning text
def text_cleaning (review):
    doc = nlp(review)
    #Removes any white spaces and converts each letter into a lowercase if it isn't a stop word or has a punctuation.
    cleaned_tokens = [token.text.lower().strip() for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(cleaned_tokens)
          
#Function for analysing sentiment, deciding either it's positive or negative
def sentiment(cleaned_data):
    sentiments = []
    for review in cleaned_data:
        doc = nlp(review)
        # Calculate sentiment score
        sentiment_score = doc._.blob.polarity
        # Classify as positive, negative, or neutral based on sentiment score
        sentiment_verdict = 'Positive' if sentiment_score > 0 else 'Negative' if sentiment_score < 0 else 'Neutral'
        sentiments.append((sentiment_verdict, sentiment_score))
    return sentiments

#Function for determining if they are similar or not
def similarity(review1, review2):
    doc1 = nlp2(review1)
    doc2 = nlp2(review2)
    #Calculates similarity score
    similarity_score = doc1.similarity(doc2)
    #Depending on the score, class it if it's similar or not
    similarity_verdict = 'Similar' if similarity_score >= 0.5 else 'Not Similar' 
    return similarity_score, similarity_verdict
        
#Selecting 'reviews.text' column in the dataset
reviews_data = df['reviews.text']

#Remove any missing values in the dataset.
clean_data = reviews_data.dropna()

#Select reviews from the cleaned data 'reviews.text' column from the following index.
selected_index = [1, 34, 54, 643, 356, 8652, 2345, 8775, 7574, 5345, 354, 689, 6534, 532]
selected_reviews = clean_data.iloc[selected_index]

#Text Cleaning
review_clean = [text_cleaning(review) for review in selected_reviews]

#Analyse the sentiment of each review.
sentiment_review = sentiment(review_clean)

print (f'Sentiment Analysis:\n')
#Goes through each review we've chosen and prints out all the data we've appplied to it.
for i in range(len(selected_reviews)):
    review = selected_reviews.iloc[i]
    cleaned_review = review_clean[i]
    sentiment_verdict, sentiment_score = sentiment_review[i]
    print(f"Review {i+1}: {review}")
    print(f"Cleaned Text: {cleaned_review}")
    print(f"Sentiment: {sentiment_verdict}, Score: {sentiment_score}")
    print()

#Comparing the similarity of 2 random reviews in the dataset.
#Selects 2 random 2 reviews
review_1 = clean_data.sample().iloc[0]
review_2 = clean_data.sample().iloc[0]

#Cleans the reviews using the 'text_cleaning' function.
review_1_clean = text_cleaning(review_1)
review_2_clean = text_cleaning(review_2)

#Compares the 2 random reviews to see if they're similar or not.
similarity_score, similarity_verdict = similarity(review_1_clean, review_2_clean)

# Prints out the results
print (f'Similarity Analysis:\n')
print(f"Review 1: {review_1}\nCleaned Review 1: {review_1_clean}\n")
print(f"Review 2: {review_2}\nCleaned Review 2: {review_2_clean}\n")
print(f"Similarity: {similarity_verdict}, Score: {similarity_score}\n")

