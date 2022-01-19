FROM python:3.9-alpine
RUN apk --no-cache --update-cache add gcc python3-dev gfortran py-pip libpng-dev openblas-dev
RUN apk add --no-cache git automake autoconf libtool g++ protobuf protobuf-dev make cmake
RUN apk add build-base
RUN pip install -U pip
RUN pip install -U setuptools
RUN apk add curl
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"
RUN cargo --help
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
COPY ./start.sh /start.sh
RUN chmod +x /start.sh
COPY ./app /app
CMD ["./start.sh"]