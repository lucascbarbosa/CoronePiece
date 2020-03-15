from datetime import datetime as dt
from getCases import getCases
from getEpisodes import getEpisodes
import facebook 


def post(cases):
    access_token = 'EAAC5zB5is18BAFla93ZCHmGJ9YUn9j4yhCDlsQXPZAg1lvlTUd8PqYNTxihO8opkg6E4bjL8lbT8hFb2Yk50Wo2lpaplng2Fp3ICVRzN76arPQQ1YWiO4ZCfcyNCZCnPmk8m89wTsDUOdSMZCSP2IGRswBt8oTZBRHLCGEjQcYke33cBVwDwWaJF4J2r3SwiIZD'
    fb = facebook.GraphAPI(access_token=access_token)
    title = episodes[episodes['Chapter']==str(cases)]['Title'].values[0]
    date = dt.now().strftime("%d/%m/%y")
    message = 'Dia %s:\n\nNúmero de Casos: %d\n\nEpisódio: %s'%(date,cases,title)
    image = open('imgs/%d.jpg'%cases,'rb');
    fb.put_photo(image=image,message=message)    

def main():
    episodes = getEpisodes()
    day = dt.now().day
    ready = True
    while True:
        if dt.now().day != day:
            ready = True
            day = dt.now().day
        if dt.now().hour == 19 and ready:
            cases = getCases()
            post(cases)
            ready = False
        else:
            pass
    
if __name__ == "__main__":
    main()