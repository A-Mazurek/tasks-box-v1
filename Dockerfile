FROM python:3.8

COPY tasks_box /app

WORKDIR /app

COPY tasks_box/requirements.txt requirements.txt

RUN pip install -r requirements.txt
