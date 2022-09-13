# syntax=docker/dockerfile:1
FROM python:3.9.14-buster

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
