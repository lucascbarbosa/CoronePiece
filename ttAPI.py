import tweepy
import time
from datetime import datetime as dt
from getCases import getCases
from getEpisodes import getEpisodes


# Authenticate to Twitter
auth = tweepy.OAuthHandler("RYOP7vU2iJX5BNonpaQkkolqq", "LiugL6Tx7X9dPcH2UK68Yl3Mz5R78vktb1ZDa2gMlPJwUsA9Js")
auth.set_access_token("1076894136312176640-YAENb5bSxk4eopWy8gcJzEdQkobWNt", "kSOIyg3HWz5IjJj0RYAbHSA2udWq66070BnWUKY34ZikE")
def post(cases):
    access_token = 'EAAC5zB5is18BAFla93ZCHmGJ9YUn9j4yhCDlsQXPZAg1lvlTUd8PqYNTxihO8opkg6E4bjL8lbT8hFb2Yk50Wo2lpaplng2Fp3ICVRzN76arPQQ1YWiO4ZCfcyNCZCnPmk8m89wTsDUOdSMZCSP2IGRswBt8oTZBRHLCGEjQcYke33cBVwDwWaJF4J2r3SwiIZD'
    api = tweepy.API(auth)
    title = episodes[episodes['Chapter']==str(cases)]['Title'].values[0]
    date = dt.now().strftime("%d/%m/%y")
    message = 'Dia %s:\n\nNúmero de Casos: %d\n\nEpisódio: %s'%(date,cases,title)
    image = 'imgs/%d.jpg'%cases
    api.update_with_media(image,message)


def main():
    episodes = getEpisodes()
    cases = getCases()
    print('Casos =%d'%cases)
    while True:
        new_cases = getCases()
        if new_cases != cases:
            print('mudou')
            cases = new_cases
            print('Casos =%d'%cases)d
            post(cases)
        else:
            pass
        time.sleep(1)

if __name__ == "__main__":
    main()