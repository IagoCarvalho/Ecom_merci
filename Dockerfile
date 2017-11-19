FROM python:3.5

RUN mkdir /code
WORKDIR /code

ADD . /code/
RUN python3 setup.py install && \
    ecom_merci --version

CMD ecom_merci