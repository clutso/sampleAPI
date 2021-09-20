# sampleAPI

This is a Generic API using Falcon-Python,  Gunicorn and influxdb. It could be runned using the docker-compose.yml file.

# INSTRUCTIONS

1)	Clone the repository 

    `git clone https://github.com/clutso/sampleAPI.git`

2)	Enter the foder containing the docker-compose.yml file

    `cd sampleAPI`

3)	Run: 
    
        `docker-compose up -d `

4)	Wait about 5 minutes for the containers to be created configured and the data is loaded into the DB  (**NOTE** :'sampleapi'-container will output "done" when everything is ready to start)

5) Test the API

You have the following endpoints:
    
- Index page, contains a brief of the API and use intructions    
    
    `http://<api_host>`
    
- Get the maximun vale of any sensor 

    `http://<api_host>/max`
    
GET and POST methods are supported:

- The GET method looks inside the parameters for the sensor to watch. The request could be performed as folllows:

    ```
    http://<api_host>/max?sensor=<sensor>
    
    http://<api_host>/max?sensor=CO2
    
    .....
    
    http://<api_host>/max?sensor=dust 
    
    etc..
    ```
- For the POST method, you must include a json file with the request:

    `{“sensor”:”<sensor>” }`

For instance, using cUrl would be something like this:

    curl -X POST -d "{\"sensor\":\"CO2\"}" 127.0.0.1/max
