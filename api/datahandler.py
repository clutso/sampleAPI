#influx 
import influxdb_client
import os

class ConnData:
    #inlfux vars
    influx_bucket = os.getenv('INFLUX_BUCKET')
    influx_db = os.getenv('INFLUX_DB')
    influx_org =  os.getenv('INFLUX_ORG')
    influx_token =  os.getenv("INFLUX_TOKEN")
    influx_url="http://"+influx_db+":8086"
    influx_device="test_Mote"
    
    influx_client = influxdb_client.InfluxDBClient(
            url=influx_url,
            token=influx_token,
            org=influx_org
        )
    