FROM python:3.9.0-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
RUN apt-get update && apt-get -y install \
	python-pip python-dev default-libmysqlclient-dev

RUN python -m pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install ez_setup && \
    pip install mysqlclient --user

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN pip install --upgrade django-cors-headers

COPY . .