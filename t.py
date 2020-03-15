import facebook
from PIL import Image
from poster.encode import *
from poster.streaminghttp import register_openers

def put_photo(self, source, album_id=None, message=""):
    object_id = album_id or "me"

    register_openers()
    content_type,body = multipart_encode( [ ('message',message),('access_token',self.access_token),('source',source) ] )

    req = urllib2.Request("https://graph.facebook.com/%s/photos" % object_id, content_type,body )

    try:
        data = urllib2.urlopen(req).read()
    except urllib2.HTTPError as e:
        data = e.read() 
    try:
        response = _parse_json(data)
        if response.get("error"):
            raise GraphAPIError(response["error"].get("code", 1),response["error"]["message"])
    except ValueError:
        response = data

    return response

access_token = 'EAAC5zB5is18BAEjdgKrSZAnATZBZA3sydYNCZCDBW3A7Hi61IwONaeVccnFcAcVKAffVmbohsVYayeF5256ukCN68PZA9Jju3cPZAq6qVlOKZCaViRWdfELidNx1NMt9ZBoc2LSSSsZCLRapF82b4bc1ScPVlI4GACAaO8kQq20iPUjyUbhQt8WhiJxzQDWzMcsZAhGqxKyg2a1wZDZD'
fb = facebook.GraphAPI(access_token=access_token)
message = 'COMI CU DE CURIOSO'
image = Image.open('imgs/10.jpg')
fb.put_photo(image,message=message,)