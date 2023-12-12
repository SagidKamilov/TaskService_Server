FROM python:3.11.1-slim

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN alembic init alembic
RUN alembic revision -m "initial migration"
RUN alembic upgrade head

COPY . .
