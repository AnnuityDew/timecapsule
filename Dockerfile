# FastAPI optimized
# https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
FROM python:3.8
ENV APP_HOME /app
WORKDIR ${APP_HOME}
COPY requirements.txt ./
RUN pip install --trusted-host pypi.python.org -r requirements.txt
COPY . ./
CMD exec gunicorn --config python:src.gunicorn_config --bind :$PORT src.main:app
