FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install bash
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

ENTRYPOINT [ "sh", "-c" ]
