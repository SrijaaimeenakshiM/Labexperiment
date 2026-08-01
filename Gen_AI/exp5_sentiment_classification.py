# Experiment 5: Sentiment Analysis And Document Classification Using Foundation Models
from transformers import pipeline

def main():
    print("--- Sentiment Analysis & Classification ---")
    
    # 1. Sentiment Analysis
    print("\n1. Sentiment Analysis:")
    # Using a model pre-trained on the SST-2 dataset for sentiment analysis
    sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    
    texts_to_analyze = [
        "I am incredibly happy with the new update! It works flawlessly.",
        "The customer service was terrible and completely unhelpful.",
        "It's an okay product, nothing too special."
    ]
    
    for text in texts_to_analyze:
        result = sentiment_pipeline(text)[0]
        print(f"Text: '{text}' -> Sentiment: {result['label']}, Score: {result['score']:.4f}")

    # 2. Document / Zero-Shot Classification
    print("\n2. Zero-Shot Document Classification:")
    # Using zero-shot classification to categorize a document into predefined labels without explicit training
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    
    document = "Tesla has announced a new electric vehicle with a range of over 500 miles on a single charge. The car will feature autonomous driving capabilities."
    candidate_labels = ["technology", "sports", "politics", "automotive", "entertainment"]
    
    print(f"Document: '{document}'")
    result = classifier(document, candidate_labels)
    
    print("\nClassification Scores:")
    for label, score in zip(result['labels'], result['scores']):
        print(f"- {label}: {score:.4f}")

if __name__ == "__main__":
    main()
