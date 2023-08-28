# Image
FROM python:3.10

# Display the Python output through the terminal
ENV PYTHONUNBUFFERED: 1

# Set work directory
WORKDIR /usr/src/app

# Add Python dependencies
## Update pip
RUN  pip install --upgrade pip
## Copy requirements
COPY requirements.txt ./requirements.txt
## Install requirements
RUN pip3 install -r requirements.txt

COPY setup_14.sh ./setup_14.sh

RUN apt-get update && bash setup_14.sh && apt-get install -y nodejs npm

RUN npm install -D tailwindcss 
