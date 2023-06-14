###########
# BUILDER #
###########

# pull official base image
FROM python:3.11.0-alpine as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add g++ gcc libc-dev libffi-dev krb5-pkinit krb5-dev krb5 snappy-dev python3-dev musl-dev bash

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

#########
# FINAL #
#########

# pull official base image
FROM python:3.11.0-alpine

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# install dependencies
RUN apk update && apk add libpq g++ gcc libc-dev libffi-dev krb5-pkinit krb5-dev krb5 snappy-dev bash
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY ./compose/production/django/start /home/app/web/start
# RUN sed -i 's/\r$//g' /home/app/web/start
RUN chmod +x /home/app/web/start

COPY ./compose/production/django/entrypoint.sh /home/app/web/entrypoint.sh
# RUN sed -i 's/\r$//g' /home/app/web/entrypoint.sh
RUN chmod +x /home/app/web/entrypoint.sh

COPY ./compose/production/django/celery/worker/start /home/app/web/start-celeryworker
# RUN sed -i 's/\r$//g' /home/app/web/start-celeryworker
RUN chmod +x /home/app/web/start-celeryworker

COPY ./compose/production/django/celery/beat/start /home/app/web/start-celerybeat
# RUN sed -i 's/\r$//g' /home/app/web/start-celerybeat
RUN chmod +x /home/app/web/start-celerybeat

COPY ./compose/production/django/celery/flower/start /home/app/web/start-flower
# RUN sed -i 's/\r$//g' /home/app/web/start-flower
RUN chmod +x /home/app/web/start-flower

# copy project
COPY . $APP_HOME

ENTRYPOINT ["/home/app/web/entrypoint.sh"]
