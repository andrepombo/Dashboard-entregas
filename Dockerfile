
FROM python:3.8-slim-buster

# setting work directory
WORKDIR /usr/src/app

# env variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1

# install psycopg dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip pipenv flake8
COPY Pipfile* ./
RUN pipenv install --system --ignore-pipfile

COPY . .

# lint
#RUN flake8 --ignore=E501,F401 .


# FROM python:3.8

# ENV FLASK_APP run.py

# COPY manage.py gunicorn-cfg.py requirements.txt .env ./
# COPY app app
# COPY authentication authentication
# COPY core core

# RUN pip install -r requirements.txt

# RUN python manage.py makemigrations
# RUN python manage.py migrate

# EXPOSE 5005
# CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]