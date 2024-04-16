FROM python:3.12.3
RUN apt-get update; apt-get install -y python3-pip libmariadb-dev
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY app/ ./
EXPOSE 8080
ENTRYPOINT [ "sh", "entrypoint.sh" ]