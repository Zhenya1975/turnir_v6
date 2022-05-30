FROM python:3.9.13-alpine3.16
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
CMD ["gunicorn", "-k", "eventlet", "-w", "1", "--reload", "-b", "0.0.0.0:8888", "app:app"]
# ENTRYPOINT gunicorn app:app -b 0.0.0.0:80