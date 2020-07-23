FROM python:3.8.3-slim-buster

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies

COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry export -f requirements.txt > requirements.txt \
  && pip install -r requirements.txt
# add app
COPY . .
