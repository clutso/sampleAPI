import influxdb_client
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from datahandler import  ConnData

class Requester(ConnData):
    start_date="2015-07-31T00:00:00.000Z"
    stop_date="2015-08-31T13:00:00Z"
    def query(self, sensor):
        query_api = self.influx_client.query_api()    
        
        query = ' from(bucket: "'+self.influx_bucket+'")\
            |> range(start: '+self.start_date+', stop: '+self.stop_date+')\
            |> filter(fn: (r) => r["_measurement"] == "'+self.influx_device+'")\
            |> filter(fn: (r) => r["_field"] == "'+sensor+'")\
            |> max()'
        print (query)
        result = query_api.query(org=self.influx_org, query=query)
        return result
