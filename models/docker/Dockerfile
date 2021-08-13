FROM python:3.7-slim

# This is the working directory inside container where all commands are executed
WORKDIR /app

COPY requirements.txt ./

# Layer cache
# Setup all the packages required for installing apache beam
RUN apt-get update && apt-get install -y build-essential \
      && pip3 install --no-cache-dir -r requirements.txt

COPY __main__.py .

ENTRYPOINT python3 __main__.py
