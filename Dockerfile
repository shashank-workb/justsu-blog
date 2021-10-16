FROM python:3.9.0

WORKDIR /jutsu_blog

ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt