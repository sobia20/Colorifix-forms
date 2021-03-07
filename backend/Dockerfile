FROM python:3.7

MAINTAINER Sobia Khalid "sobia.khalid.2126@gmail.com"

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt 

COPY . /

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]