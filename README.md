# Quote Generation using GPT2 with FastAPI and Docker

GPT2 language model has been finetuned for the task of quote generation for a given prompt. The trained model has been uploaded to HuggingFace Hub for easy inference. 

```
from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained("nandinib1999/quote-generator")
model = AutoModelWithLMHead.from_pretrained("nandinib1999/quote-generator")
```

To serve the model, an API has been developed using FastAPI framework which has been containerized using Docker for easy portability. You can run the API on your local system with/without the Docker.

If you wish to set up the API without Docker,

1. Clone the repository
```
git clone https://github.com/nandinib1999/gpt2_quote_generation_fastapi.git
```
2. Install all the dependencies
```
pip install torch==1.10.2+cpu torchvision==0.11.3+cpu torchaudio==0.10.2+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
pip install --no-cache-dir -r requirements.txt
```
3. Run the app
```
uvicorn app.main:app
```
You can then follow the link http://127.0.0.1:8000/docs once the model download is completed. This will take you to FastAPI Swagger UI for testing the API.

If you wish to set up the API using Docker, (Please ensure `Docker` is already installed in your system)

1. Clone the repository
```
git clone https://github.com/nandinib1999/gpt2_quote_generation_fastapi.git
```
2. Build the Docker image
```
docker build -t myimage .
```
3. Run the container 
```
docker run --name mycontainer -p 80:80 myimage
```
You can then follow the link http://0.0.0.0/docs. It will take you to the FastAPI Swagger UI for testing the API.
