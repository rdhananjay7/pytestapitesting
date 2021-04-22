FROM python:latest
MAINTAINER rdhananjay7@yahoo.co.in

RUN mkdir /apitests
COPY ./ssd-cneos-api-suites /apitests/

WORKDIR /apitests
RUN python3 setup.py install

