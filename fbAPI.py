import time
from datetime import datetime as dt
from getCases import getCases
from getEpisodes import getEpisodes
import facebook 


def post(cases,episodes):
    access_token = 'EAAC5zB5is18BAEov3LI7sdUeGkBzdCnCCRFZBBHUYPHirgYW4ryKASVSZBamo4nJNbnw9TYfLgXiK3geahqJjjvPkjd47BcldnAmQBXY5q8JHLTWEuoRhO4wlK3ml9UoiqusvBcoWGyBmQjLw1KoSitRMODuiQEVazLHlnGmGdiX37NvUoDScq2rBgGZB8ZD'
    fb = facebook.GraphAPI(access_token=access_token)
    title = episodes[episodes['Chapter']==str(cases)]['Title'].values[0]
    date = dt.now().strftime("%d/%m/%y")
    time = '{:d}:{:02d}'.format(dt.now().hour,dt.now().minute)
    message = 'Dia %s %s\n\nNúmero de Casos: %d\n\nEpisódio: %s'%(date,time,cases,title)
    image = open('imgs/%d.jpg'%cases,'rb');
    fb.put_photo(image=image,message=message)    

def main():
    episodes = getEpisodes()
    cases = getCases()
    post(cases,episodes)
    print('Casos =%d'%cases)
    while True:
        new_cases = getCases()
        if new_cases != cases:
            print('mudou')
            cases = new_cases
            print('Casos =%d'%cases)
            post(cases,episodes)
        else:
            pass
        time.sleep(1)


    
if __name__ == "__main__":
    main()