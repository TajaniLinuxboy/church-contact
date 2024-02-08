FROM python:latest

WORKDIR home

COPY . . 

RUN pip install -r requirements/requirements.txt

