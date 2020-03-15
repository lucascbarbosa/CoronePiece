import pandas as pd 
def getCases():
    url = 'https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-total.csv'
    df = pd.read_csv(url,index_col=0,error_bad_lines=False)
    return(int(df.iloc[0,1]))
