FROM python:3.8-alpine

COPY . /app
WORKDIR /app

RUN pip install pipenv

RUN pipenv install --deploy

CMD pipenv run python app.py