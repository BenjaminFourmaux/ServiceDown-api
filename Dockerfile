# syntax=docker/dockerfile:1
FROM python:3.9.14-buster
ENV PYTHONUNBUFFERED=1

# Container datetime fix
RUN echo "Etc/UTC" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
