# Experiment 1: Text Generation Using Pre-Trained Foundation Models
from transformers import pipeline

def main():
    print("--- Text Generation using GPT-2 ---")
    # Initialize the pipeline for text generation
    # We use gpt2 as a standard, readily available open-source foundation model
    generator = pipeline('text-generation', model='gpt2')
    
    prompt = "The future of Artificial Intelligence is"
    print(f"Prompt: {prompt}\n")
    
    # Generate text based on the prompt
    result = generator(prompt, max_length=50, num_return_sequences=1, pad_token_id=50256)
    
    print("Generated Text:")
    print(result[0]['generated_text'])

if __name__ == "__main__":
    main()
