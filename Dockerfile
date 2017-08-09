FROM python:3.6

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends curl git software-properties-common && \
    \
    apt-get clean -y && \
    apt-get purge -y && \
    apt-get autoclean -y && \
    apt-get autoremove -y && \
    \
    rm -rf /usr/share/locale/* && \
    rm -rf /var/cache/debconf/*-old && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /usr/share/doc/* && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/*

COPY requirements /usr/src/app/requirements

RUN pip install --no-cache-dir -r requirements/production.txt

EXPOSE 8080
