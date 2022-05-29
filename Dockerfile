FROM python:3.9.13-alpine3.16
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
# EXPOSE 8123
CMD ["gunicorn"  , "-b", "0.0.0.0:8888", "app:app"]
# ENTRYPOINT gunicorn app:app -b 0.0.0.0:80