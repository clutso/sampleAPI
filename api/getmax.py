import json
import falcon
from defaultresponse import  defaultResponseClass
from datarequester import Requester 
from datetime import datetime, timedelta

class GetMax(defaultResponseClass):
    valid_keys=["sensor","Sensor", "SENSOR", "sENSOR"]    
    '''            
    get_key_name(request) function take falcon.request and look ONLY for the first parameter, ignoring any other (if included). returns the parameter received and the key_value wich corresponds to the desired sensor.
    '''
    def get_key_name(self, request):
        key= list(self.request_keys)
        key_name=request.get_param(key[0]) 
        return key[0],key_name
    
    def get_json_content(self, request):
        key_name=""
        starts= ""
        ends=""
        try:
            key_name= request["sensor"]
            starts= request["start"]
            ends= request["end"]  
        except:
            pass
        return key_name,starts, ends
    '''            
    For the GET method the API looks in the parameters for the sensor to watch.
    Request is performed as folllows:

        http://host/max?sensor=CO2
    '''
    def on_get(self, request, response):
        num_params=self.validate_params(request)
        # This method requires only one parameter ignore extra parameters
        if num_params>0:
            key_name, target=self.get_key_name(request)
            if key_name in self.valid_keys:
                result=[]
                try:
                    results= Requester().query(target)
                    for table in results:
                        for record in table.records:
                            result.append((record.get_field(), record.get_value()))
                except:
                    response.text = json.dumps({"error":"bad request"})
                if len(result) >0:
                    if num_params==1:      
                            response.text = json.dumps({target:result[0][1]})    
                    else:
                        response.text =response.text = json.dumps({target:result[0][1], "warning": "ignoring extra params"})
                else:
                    response.text = json.dumps({"error":"unkown sensor <"+ target+"> "})
            else:
                response.text = json.dumps({"error": "param <"+ key_name+"> invalid"})
        #
        # This method requires one parameter and NONE has given
        if num_params==0:
            response.text = json.dumps({"error":"no parameters given"})
        # Means an exception has been raised when validating parameters
        if num_params==-1:
            response.text = json.dumps({"error":"runtime exception"})            
    '''            
    For the POST method the API looks into the json sent as request content.
    Request is performed as folllows(cUrl example):

    curl -X POST -d "{\"sensor\":\"CO2\"}" 127.0.0.1/max
    '''
    def on_post(self, request, response):
        has_content=self.validate_json_input(request)
        if has_content:
            
            target, start_date, end_date=self.get_json_content(self.request_content)
            request= Requester()
            if start_date != "":
                request.start_date=start_date
            if end_date != "":
                request.stop_date=end_date
            '''
            #TODO time range validation
            if a> b:
                response.text = json.dumps({"error":"Start date is greater than End"} ,ensure_ascii=False)
            '''
            if target != "":
                result=[]
                try:
                    results= request.query(target)
                    for table in results:
                        for record in table.records:
                            result.append((record.get_field(), record.get_value()))
                except:
                    response.text = json.dumps({"error":"bad request"})
                if   len(result)>0: 
                    response.text = json.dumps({target:result[0][1]},ensure_ascii=False)
                else :
                    response.text = json.dumps({"error":"no results"},ensure_ascii=False)
            else:
                response.text = json.dumps({"error":"bad request"}, ensure_ascii=False)
            #after OPS should return 
            #response.text = json.dumps(self.response_content)
        else: 
            response.text = json.dumps({"error":"empty request"})
          