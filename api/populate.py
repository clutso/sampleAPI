import json
import falcon
from defaultresponse import  defaultResponseClass
from dataloader import DataLoader 

class DbLoader(defaultResponseClass):
    loader= DataLoader()
    def on_get(self, request, response):
        self.loader.init("sensor-data.csv")
        response.text ='Done loading'

