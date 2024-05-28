FROM python:latest

RUN apt-get update && apt-get install -y \
    python3-pip

#copy the code to the container
COPY . /app
# pip install reqiurements file
RUN pip install -r /app/requirements.txt
