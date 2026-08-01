# Experiment 2: Prompt Engineering Techniques For Content Generation, Reasoning And Task Automation
from transformers import pipeline

def main():
    print("--- Prompt Engineering Techniques ---")
    # We use a text generation model to demonstrate prompt engineering strategies
    generator = pipeline('text-generation', model='gpt2')
    
    # 1. Zero-shot prompting
    # Asking the model to perform a task without any examples
    print("\n1. Zero-shot Prompting:")
    zero_shot_prompt = "Classify the following text as Positive or Negative.\nText: I love this new phone!\nSentiment:"
    print("Prompt:\n", zero_shot_prompt)
    result = generator(zero_shot_prompt, max_new_tokens=10, num_return_sequences=1, pad_token_id=50256)
    print("Output:\n", result[0]['generated_text'])

    # 2. Few-shot prompting
    # Providing the model with a few examples to guide its output
    print("\n2. Few-shot Prompting:")
    few_shot_prompt = """
    Text: The weather is terrible today.
    Sentiment: Negative
    
    Text: I had a great time at the park.
    Sentiment: Positive
    
    Text: The food at this restaurant is disgusting.
    Sentiment: Negative
    
    Text: This movie is absolutely fantastic!
    Sentiment:"""
    print("Prompt:\n", few_shot_prompt)
    result2 = generator(few_shot_prompt, max_new_tokens=10, num_return_sequences=1, pad_token_id=50256)
    print("Output:\n", result2[0]['generated_text'])

if __name__ == "__main__":
    main()
