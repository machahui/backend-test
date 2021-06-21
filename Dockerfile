FROM python:3.8.5-alpine
RUN apk add --no-cache mariadb-connector-c-dev bash
RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base

RUN apk add netcat-openbsd


WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 80
ENTRYPOINT [ "/bin/bash", "entrypoint.sh"]