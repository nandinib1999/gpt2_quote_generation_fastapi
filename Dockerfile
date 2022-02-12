FROM python:3.9

# Upgrading the pip module 
RUN pip install -U pip
RUN pip install -U setuptools

# Installing the required packages using requirements.txt
COPY ./requirements.txt /requirements.txt
RUN pip3 install torch==1.10.2+cpu torchvision==0.11.3+cpu torchaudio==0.10.2+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
RUN pip install --no-cache-dir -r /requirements.txt

# Shell script to run the fast-api
COPY ./start.sh /start.sh
RUN chmod +x /start.sh
COPY ./app /app
CMD ["./start.sh"]