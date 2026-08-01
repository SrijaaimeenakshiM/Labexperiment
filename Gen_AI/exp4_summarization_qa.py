# Experiment 4: Text Summarization And Question-Answering System Using Large Language Models
from transformers import pipeline

def main():
    print("--- Text Summarization and Question Answering ---")
    
    text = """
    Generative artificial intelligence (generative AI) is a type of AI that can create new content and ideas, including conversations, stories, images, videos, and music. AI technologies attempt to mimic human intelligence in nontraditional computing tasks like image recognition, natural language processing (NLP), and translation. Generative AI is the next step in artificial intelligence. You can train it to learn human language, programming languages, art, chemistry, biology, or any complex subject matter. It reuses the training data to solve new problems. For example, it can learn English vocabulary and create a poem from the words it processes. Your organization can use generative AI for various purposes, such as chatbots, media creation, and product design and development.
    """
    
    # 1. Summarization
    # Using a pre-trained model for abstractive text summarization
    print("\n1. Summarization:")
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    summary = summarizer(text, max_length=50, min_length=20, do_sample=False)
    print(summary[0]['summary_text'])
    
    # 2. Question Answering
    # Using an extractive QA model to find answers within the provided context
    print("\n2. Question Answering:")
    qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    
    question1 = "What can Generative AI create?"
    print(f"Q: {question1}")
    result1 = qa_pipeline(question=question1, context=text)
    print(f"A: {result1['answer']}")

    question2 = "What are the purposes organizations can use generative AI for?"
    print(f"\nQ: {question2}")
    result2 = qa_pipeline(question=question2, context=text)
    print(f"A: {result2['answer']}")

if __name__ == "__main__":
    main()
