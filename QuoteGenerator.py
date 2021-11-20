from transformers import pipeline, set_seed, AutoTokenizer, AutoModelWithLMHead
from transformers.pipelines import TextGenerationPipeline
import re
import random


class QuoteGenerator:
    def __init__(self):
        self.quote_generator: TextGenerationPipeline
        self.tokenizer = AutoTokenizer.from_pretrained("nandinib1999/quote-generator")
        self.model = AutoModelWithLMHead.from_pretrained("nandinib1999/quote-generator")   
        self.default_prompts = ['life is not fair', 'she is a warrior', 'friendship is like', 'you cannot find light']

    def load_generator(self) -> None:
        self.quote_generator = pipeline('text-generation', model = self.model, tokenizer = self.tokenizer)

    def clean_text(self, quote):
        quote = quote.strip()
        # Remove any special characters
        quote = re.sub(r'[~`^*&%$@#|]', ' ', quote)
        # Remove extra spaces
        quote = re.sub("\s\s+", " ", quote)
        # Remove space before punctuation
        quote = re.sub(r'\s[.,;!?]', r'\1', quote)
        # Sentence case
        quote = quote.capitalize()
        return quote

    def generate_quote(self, prompt_start: str, min_length=3, max_length=25, temperature=1.0):
        if len(prompt_start.strip()) == 0:
            rand_index = random.randint(0, len(self.default_prompts))
            prompt_start = self.default_prompts[rand_index]
        quote_gen = self.generator(prompt_start.strip(), min_length = min_length, max_length = max_length, temperature = temperature, top_k = 5, top_p = 0.9)
        quote = quote_gen[0]['generated_text']
        quote_clean = self.clean_text(quote)
        return quote_clean