from datahandler import  ConnData
import pandas
import os

#influx 
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

class DataLoader(ConnData):

    def init(self, fileName):
        data = pandas.read_csv(fileName)
        write_api = self.influx_client.write_api(write_options=SYNCHRONOUS)
        for i in range (len(data)):
            try:
                p = influxdb_client.Point("test_Mote")\
                    .tag("type", "multi_sensor_dev") \
                    .field("power",  data["power"][i])\
                    .field("temp", data["temp"][i])\
                    .field("humidity", data["humidity"][i])\
                    .field("light", data["light"][i])\
                    .field("CO2", data["CO2"][i])\
                    .field("dust", data["dust"][i])\
                    .time(data["time"][i])
                write_api.write(bucket=self.influx_bucket, org=self.influx_org, record=p)
            except:
                print("failed at entry: "+ str(i))
                continue
        return True 
        


    