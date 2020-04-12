import pandas as pd

def fetchData(baseUrl=None,dataKeys=None):
    
    if baseUrl is None:
        baseUrl = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_"
    
    else:
        baseUrl = baseUrl
    
    if dataKeys is None:
        dataKeys = ["confirmed_US","confirmed_global","deaths_US","deaths_global","recovered_global"]
    
    else:
        dataKeys = dataKeys
    
    df = {}
    
    for key in dataKeys:
        fullurl = baseUrl+key+".csv"
        df[key] = pd.read_csv(fullurl)
        # print(len(df[key]))
    return df


if __name__ == "__main__":
    df = fetchData()
    for data in df.values():
        print(data.head())

