FROM python:3.9.6
# FROM ubuntu:20.04

# set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1 
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
RUN date

# Install system packages, python packages
# Purge build deps in the same run
# All in one run to allow for a smaller docker layer
RUN apt-get update \
    && apt-get install -y software-properties-common \
    && add-apt-repository -y ppa:ubuntu-toolchain-r/ppa \
    && apt-get install -y wget bash nano vim git zip unzip less sqlite3 bsdmainutils bc \
    && apt-get clean

# set working directory
RUN mkdir -p /app
WORKDIR /app
ADD . /app/
# copy requirements.txt to the current working directory
COPY requirements.txt ./
# COPY staticfiles/ ./staticfiles/
# execute the pip install upgrade first and then install requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy the content of the current directory to the working directory
COPY . .