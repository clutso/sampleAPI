import pandas
from datetime import datetime
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import os
import time

#influx vars
influx_db = os.getenv('INFLUX_DB')
bucket = "pLunaBucket"
org = "pLunaOrg"
token = "IQyrPlPpb8EZo4ktGmSkUvKUv9vChzzkXrkfwLjFIAODypDjyGhAemoqddgyTqng9utVFH8tsE0SPRo7yCm9xw=="
url="http://"+influx_db+":8086"
client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)
write_api = client.write_api(write_options=SYNCHRONOUS)


#csv vars
file = "sensor-data.csv"
data = pandas.read_csv(file)
colName=data.columns
tStamp=""

print("sending stuff to "+ url)
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
        write_api.write(bucket=bucket, org=org, record=p)
    except:
        print("Failed populating at entry: "+ str(i))
        continue