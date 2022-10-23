FROM python:3.10.6 as builder

LABEL maintainer="GaBo <ag.consulting.dev@gmail.com>"

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

ENV PYTHONPATH=/code
EXPOSE 80

#ENV WORKERS_PER_CORE=3
#ENV GRACEFUL_TIMEOUT=120
#ENV TIMEOUT=180
#ENV KEEP_ALIVE=180

CMD ["uvicorn", "app.main:asgi_app", "--host", "0.0.0.0", "--port", "80"]
