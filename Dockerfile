FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir code
WORKDIR /code/
COPY . /code
RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get install -yyq netcat
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary
COPY ./entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]