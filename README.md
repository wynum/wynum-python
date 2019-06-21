# Installation
```pip install wynum```
To install using github try
```pip install -U -e git+https://github.com/wynum/wynum-python#egg=wynum```

# Getting started
Very easy to use. Create a ```Client``` and you're ready to go.
## API Credentials
The ```Client``` needs Wynum credentials.You can either pass these directly to the constructor.
```python
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

```python
schemas = client.getschema()
for schema in schemas:
    print(schema.key, schema.type)
```

## Post data
the ```postdata``` method accepts a single parameter data which is ```dict``` containing the post key:value. Every data ```dict``` should contain the 'identifier'. You can get identifier key if you have called ```getschema```. You can retrieve it using ```client.identifier```.

```python
client.getschema()
identifer_key = client.identifier
data = {'key1':val1, 'key2':val2, identifer_key:'id_string'}
res = client.postdata(data)
```
If the call is successful it returns the ```dict``` containing the created data instance. If there is some error the ```dict``` will contain ```_error``` and ```_message``` keys.  You should check this to check for errors.

## Get data
Call ```getdata``` to get the data. This will return ```list``` of ```dict```. ```getdata``` accepts following keyword arguments
- ```limit```: ```int```
    <br>Number of records to return.
- ```order_by```: ```str```
    <br> Sorting order which can either be 'asc' or desc'
- ```ids```: ```list``` of ```str```
    <br> The list of ids to retrieve
- ```start```: ```int```
    <br> Record number to start from
- ```to```: ```int```
    <br> Record number to end at

```start``` and `to` can be used for pagination.

If no arguments are provided it will return the list of all data records.

```python
data = client.getdata()
```

## Updating data
The ```update``` method is same as that of ```postdata``` method.
```python
client.getschema()
identifer_key = client.identifier
data = {'key1':val1, 'key2':val2, identifer_key:'id_string'}
res = client.update(data)
```