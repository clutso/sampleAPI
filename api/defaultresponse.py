import json
import falcon

class defaultResponseClass:
    #API vars
    response_content = {}
    request_content={}
    request_keys:dict
    
    def validate_json_input(self, request):
        try:
            self.request_content= json.loads(request.stream.read())
            return True
        except:
            return False

    def validate_params(self, request):
        try:
            self.request_keys= request.params.keys()
            return (len(list(self.request_keys)))
        except:
            return -1

    def on_get(self, request, response):
        response.text ='Not implemented method.'
        response.status = falcon.HTTP_200
    
    def on_post(self, request, response):
        response.text = json.dumps({"not":"implemented"})
        response.status = falcon.HTTP_200
