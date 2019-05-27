# Installation
```pip install wynum```

# Getting started
Very easy to use. Create a ```Client``` and you're ready to go.
## API Credentials
The ```Client``` needs Wynum credentials.You can either pass these directly to the constructor.
```
from wynum import Client

secret = "your_secret_key"
token = "project_token"
client = Client(secret, token)
```


## Get schema
call ```getschema``` on ```Client``` to get the keys and types for the data. This will return a ```list``` of ```Schema``` objects.  ```Schema.key``` will return the key and ```Schema.type``` will return the Wynum type. Following is the mapping from Wynum type to python type.

| Wynum type            | Python type              |
| --------------------- | ------------------------ |
| Text                  | ```str```                |
| Date                  | ```str``` (dd/mm/yyyy)   |
| Number                | ```int``` or ```float``` |
| Choice (Or)           | ```int``` or ```float``` |
| Multiple Choice (And) | ```list``` of ```str```  |
| Time                  | ```str``` (hh:mm)        |
| File                  | ```File```               |

```
schemas = client.getschema()
for schema in schemas:
    print(schema.key, schema.type)
```

## Post data
the ```postdata``` method accepts a single parameter data which is ```dict``` containing the post key:value. Every data ```dict``` should contain the 'identifier'. You can get identifier key if you have called ```getschema```. You can retrieve it using ```client.identifier```.

```
client.getschema()
identifer_key = client.identifier
data = {'key1':val1, 'key2':val2, identifer_key:'id_string'}
res = client.postdata(data)
```
If the call is successful it returns the ```dict``` containing the created data instance. If there is some error the ```dict``` will contain ```_error``` and ```_message``` keys.  You should check this to check for errors.

## Get data
Call ```getdata``` to get the data. This will return ```list``` of ```dict```
```
data = client.getdata()
```

## Updating data
The ```update``` method is same as that of ```postdata``` method.
```
client.getschema()
identifer_key = client.identifier
data = {'key1':val1, 'key2':val2, identifer_key:'id_string'}
res = client.update(data)
```