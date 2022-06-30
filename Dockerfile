FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y tzdata\
    python3 python3-pip \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
    curl unzip wget \
    xvfb && \
    apt-get -y install sudo && \
    sudo apt-get install -y libgbm1 && \
    pip3 install --no-cache-dir \
        behave                  \
        kafka-python             \
        names


ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN ["chmod", "655", "scripts/regression.sh"]

ENTRYPOINT ["script/regression.sh"]