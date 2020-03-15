from datetime import datetime as dt
from getCases import getCases
from getEpisodes import getEpisodes
import facebook 

cases = getCases()
episodes = getEpisodes()


def post(cases):
    access_token = 'EAAC5zB5is18BAH7daxDjgNQUpCZCQt21XZBpSWLt44MiMzJEEd1fFCuuTO8fbsSNPKvzcYBZAaYcZCdNDVedGZAAzNSbI8ZCFWvl3zfApMvEJzZAVbE6upbI0cbfueYsKxJSqRl09baUK2AsPx4VrcRQLtGwtiHJ7v2OZCCRMiYz1XHLb02SPMo5eglYMQsrDJAZD'
    fb = facebook.GraphAPI(access_token=access_token)
    title = episodes[episodes['Chapter']==cases]['Title']
    date = dt.now().strftime("%m/%d/%y")
    message = 'Dia %s:\n\nNúmero de Casos: %d\n\nEpisódio: %s'%(date,cases,title)
    image = open('imgs/%d.png'%cases).read()
    fb.put_object(parent_object='me',connection_name='feed',message=message,source=image)
    

post(cases)


"""day = dt.now().day
ready = False
while True:
    if dt.now().day != day:
        ready = True
        day = dt.now().day
    if dt.now().hour == 12 and ready:
        post()
    else:
        pass"""