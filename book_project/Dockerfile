###########
# BUILDER #
###########

FROM python:3.10.11-slim as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update\
    && apt-get install -y postgresql-server-dev-all gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install flake8==6.0.0

COPY . .

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

#########
# FINAL #
#########

FROM python:3.10.11-slim

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
ARG USER_ID="10000"
ARG GROUP_ID="10001"
ARG USER_NAME="app"

RUN groupadd -g "${GROUP_ID}" "${USER_NAME}" && \
  useradd -l -u "${USER_ID}" -m "${USER_NAME}" -g "${USER_NAME}"

# RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

# install dependencies
RUN apt-get update && apt-get install -y libpq-dev
RUN apt install -y netcat
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY ./entrypoint.sh $APP_HOME

COPY . $APP_HOME
 
RUN chown -R app:app $APP_HOME

USER app
 
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
