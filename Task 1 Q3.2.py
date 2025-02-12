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