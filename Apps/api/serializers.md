Serializing objects

from Apps.api.Serializers import ProductSerializers

ser=ProductSerializers()  
ser.data
{'name': '', 'weight': None, 'price': None}

from rest_framework.renderers import JSONRenderer

 json = JSONRenderer().render(ser.data)  
 json
 b'{"name":"","weight":null,"price":null}'

Deserializing objects

import io
from rest_framework.parsers import JSONParser

 stream=io.BytesIO(json)
 data=JSONParser().parse(stream)
 sers=ProductSerializers(data=data)

 sers.is_valid()
 False
