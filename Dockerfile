FROM python:3.10.11-slim
 
WORKDIR /usr/src/app
 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update\
    && apt-get install -y postgresql-server-dev-all gcc python3-dev musl-dev
RUN apt install -y netcat

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
 
COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

