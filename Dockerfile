# pull the official base image
FROM python:3.8.3-slim-buster

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# install python dependencies
COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade pip
RUN pip install poetry \
  && poetry export -f requirements.txt > requirements.txt --dev --without-hashes \
  && pip install -r requirements.txt

# add app
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
