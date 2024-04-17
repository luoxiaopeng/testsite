FROM python:3.11.2-slim as base

WORKDIR /app
COPY . /app/

ENV PYTHONDONTWRITEBYTECODE 1
ARG PIP
ENV PIP_CONFIG_FILE ${PIP}

RUN pip install -U setuptools
RUN pip install -r requirements.txt


# Now multistage builds
FROM python:3.11.2-slim

COPY --from=base /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/

WORKDIR /app
COPY . /app/

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /app:$PYTHONPATH
ARG PIP
ENV PIP_CONFIG_FILE ${PIP}

ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV PROJECT_NAME main

ARG SOURCES
RUN if [[ -z "$SOURCES" ]] ; then sed -i "s@http://\(deb\|security\).debian.org@https://mirrors.aliyun.com@g" /etc/apt/sources.list ; else echo SOURCES is $SOURCES ; fi
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
        git \
        nano \
        gcc \
        default-libmysqlclient-dev \
        mariadb-client \
        pkg-config \
        && rm -rf /var/lib/apt/lists/*

RUN pip install -U setuptools
RUN pip install -r requirements-new.txt

EXPOSE 80
