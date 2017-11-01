FROM python:3.5
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD . /code/
RUN pip install -r requirements/requirements.txt -r requirements/test-requirements.txt
RUN chmod +x boot.sh