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

# create directory for the app user
# RUN mkdir -p /home/app


# create the app user
# RUN addgroup -S app && adduser -S app -G app
# Notice that we created a non-root user? By default, 
# Docker runs container processes as root inside of a container. 
# This is a bad practice since attackers can gain root access to 
# the Docker host if they manage to break out of the container. 
# If you're root in the container, you'll be root on the host.


# create the appropriate directories
ENV APP_HOME=/app
# ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME

RUN mkdir -p $APP_HOME/staticfiles
RUN mkdir -p $APP_HOME/mediafiles
# Docker Compose normally mounts named volumes as root. And since 
# we're using a non-root user, we'll get a permission denied error 
# when the collectstatic command is run if the directory does 
# not already exist

WORKDIR $APP_HOME
# copy requirements.txt to the current working directory
COPY requirements.txt ./
# COPY staticfiles/ ./staticfiles/
# execute the pip install upgrade first and then install requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
# RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.sh

# RUN chmod +x $APP_HOME/entrypoint.sh
# RUN ["chmod", "+x", "/app/entrypoint.sh"]

# copy project
COPY . .

# chown all the files to the app user
# RUN chown -R app:app $APP_HOME

# change to the app user
# USER app

# copy the content of the current directory to the working directory
# COPY . .

# COPY ./entrypoint.sh /

# run entrypoint.sh
# ENTRYPOINT ["sh", "/app/entrypoint.sh"]
