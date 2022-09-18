# syntax=docker/dockerfile:1
FROM python:3.9.14-buster
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
