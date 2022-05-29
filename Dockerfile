FROM python:3.9.13-slim-buster
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
# EXPOSE 8123

ENTRYPOINT gunicorn app:app -b 0.0.0.0:80