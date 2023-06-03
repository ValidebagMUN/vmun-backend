FROM python:3.11.0-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
# first install the snappy c library for python-snappy
RUN apk add --no-cache g++ gcc libc-dev libffi-dev krb5-pkinit krb5-dev krb5 snappy-dev
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .