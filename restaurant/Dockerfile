FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /usr/src/restaurant
ADD . .

RUN apk add --update --no-cache --virtual .tmp-build-deps \
     gcc libc-dev linux-headers tree vim bash

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD python manage.py makemigrations && python manage.py migrate && python manage.py loaddata fixtures/initial_data.json && python manage.py runserver 0.0.0.0:8000
