FROM python:2.7
MAINTAINER Daniel Andrei Minca @dminca

LABEL org.label-schema.name="PythonScraper" \
  org.label-schema.description="A simple implementation of Web Scraper written in Python" \
  org.label-schema.vcs-url="https://github.com/dminca/pyscraper" \
  org.label-schema.schema-version="1.0" \
  org.label-schema.docker-cmd="docker run --rm -ti dminca/pyscraper ash"

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

