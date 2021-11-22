FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir code
WORKDIR /code/
RUN apt-get update \
    && apt-get install -yyq netcat
COPY ./requirements.txt/ .
RUN pip install -r requirements.txt
COPY ./entrypoint.sh .
COPY . /code/

ENTRYPOINT ["./entrypoint.sh"]