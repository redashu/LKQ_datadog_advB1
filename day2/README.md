## Revision of DogstatsD and custom metrics consideration 

<img src="dogs.png">

## Understanding API in datadog 

<img src="datadogapi.png">

## to connect with datadog we need the correct API URL 

<img src="apiurl.png">

### curl tool to get dashbaord list 

```
curl -X GET "https://api.us5.datadoghq.com/api/v1/dashboard" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: " \
-H "DD-APPLICATION-KEY: "


```