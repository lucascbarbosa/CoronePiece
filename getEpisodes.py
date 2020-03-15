import requests
import pandas as pd
import numpy as np
import lxml.html as lh
import json
from pandas.io.json import json_normalize
from bs4 import BeautifulSoup
from urllib.request import Request,urlopen
import csv

def cleanTitles(title):
    try:
        title.split("Transcription")[0].split('""')[-1]
        try:
            return title.split("Transcription")[0].split('""')[-1].split('" "')[-1][:-1]
        except:
            pass
    except:
        pass

def getEpisodes():
    urls = ['https://en.wikipedia.org/wiki/List_of_One_Piece_episodes_(seasons_1-8)','https://en.wikipedia.org/wiki/List_of_One_Piece_episodes_(seasons_9-14)','https://en.wikipedia.org/wiki/List_of_One_Piece_episodes_(seasons_15-current)']
    useful_tables= [8,6,6]
    dfs=[]
    for url in urls:
        i = urls.index(url)
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content)
        tables = soup.findAll('table',{'class':'wikitable'})
        for table in tables:
            j = tables.index(table)
            if j < useful_tables[i]:
                df=pd.read_html(str(table),encoding='utf-8')
                dfs.append(df[0])
        

    chaps = np.array([])
    for i in range(len(dfs)):
        if i < 5:
            chaps_df= np.array(dfs[i].iloc[:,0].values)
            chaps = list(chaps)+list(chaps_df)
            chaps = np.array(chaps)
        else:
            data = np.array(dfs[i].iloc[:,2].values)
            chaps_df= np.array(dfs[i].iloc[:,0].values)
            chaps = list(chaps)+list(chaps_df)
            chaps = np.array(chaps)
    titles=np.array([])
    for i in range(len(dfs)):
        if i < 5:
            titles_df = np.array(dfs[i].iloc[:,2].values)
            titles = list(titles)+list(titles_df)
            titles = np.array(titles)
        else:
            data = np.array(dfs[i].iloc[:,1].values)
            titles = list(titles)+list(data)
            titles = np.array(titles)

    titles = list(map(cleanTitles,list(titles)))
    res = pd.DataFrame(columns ='Chapter Title'.split(' '))
    res['Chapter'] = chaps
    res['Title'] = titles
    return res