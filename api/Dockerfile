FROM python:3.8-buster

EXPOSE 80

RUN pip install pandas gunicorn falcon influxdb-client 
#WORKDIR .
COPY . /app
WORKDIR /app
CMD ["sh", "init.sh"]