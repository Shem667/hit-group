import string
from collections import Counter

def get_top_words(file_path):
    # Read the content of the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()

    # Split the text into words
    words = text.split()

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Get the top 30 most common words
    top_words = word_counts.most_common(30)

    return top_words

# The path to text file
file_path = 'C:/Users/Admin/Documents/GitHub/hit-group/combined_text.txt'
top_words = get_top_words(file_path)

# Print the top 30 most common words
for word, count in top_words:
    print(f"{word}: {count}")
    
    pip install transformers

from transformers import AutoTokenizer
from collections import Counter

def count_unique_tokens(text, model_name='bert-base-uncased'):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokens = tokenizer.tokenize(text)
    token_counts = Counter(tokens)
    return token_counts.most_common(30)

text_file_path = 'C:/Users/Admin/Documents/GitHub/hit-group/combined_text.txt'
model_name = 'bert-base-uncased'

with open(text_file_path, 'r') as file:
    text = file.read()

top_30_tokens = count_unique_tokens(text)
print(top_30_tokens)