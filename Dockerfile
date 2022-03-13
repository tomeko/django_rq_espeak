FROM python:3

# We want proper container logging
ENV PYTHONUNBUFFERED 1

# Move requirements file into container
ADD requirements.txt /django_rq_espeak/requirements.txt

# Set working directory to project
WORKDIR /django_rq_espeak/

# install espeak, ffmpeg
RUN apt update && apt install -y espeak ffmpeg

# Upgrade pip
RUN pip install --upgrade pip
# Install requirements
RUN pip install -r requirements.txt