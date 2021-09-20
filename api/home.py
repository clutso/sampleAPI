import json
import falcon
from defaultresponse import  defaultResponseClass

class index(defaultResponseClass):
    def on_get(self, request, response):
        response.text ='\
        Welcome to sampleAPI built from Falcon Python with Gunicorn and influxdb running in an Alpine Linux container.\n\n\n\
        You can get the maximun value of a sensor in a data set using GET and POST methods\n\n\n\
        The GET method looks inside the parameters for the sensor to watch.\n\
        Your request could be performed as folllows:\n\n\
        http://host/max?sensor=CO2\n\n\n\n\
        For the POST method, you must include a json file with the request.\n\
        for example, using cUrl you can use:\n\n\
        curl -X POST -d "{\"sensor\":\"CO2\"}" 127.0.0.1/max\n\n\n\
        Available sensors for this data set are: CO2, dust, humidity, light, power and temp\n\n\
        GIVE IT A TRY!'
        