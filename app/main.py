from fastapi import FastAPI
from .QuoteGenerator import QuoteGenerator
from .logger_config import LogConfig
import logging
from logging.config import dictConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("quote_api")
app = FastAPI()

quote_generator = QuoteGenerator()
quote_generator.load_generator()

@app.get("/")
def root():
    return {"message": "This is Quote Generation API test"}

@app.post("/generate_quote")
def generate_quote_for_user(prompt):
    generated_quote = quote_generator.generate_quote(prompt)
    return generated_quote
