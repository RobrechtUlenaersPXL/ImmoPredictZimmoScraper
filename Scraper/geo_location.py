import requests
import pandas as pd
from os import listdir


src_directory = './data'
for file in listdir(src_directory):
    file_location = src_directory + "/" + file
    print("[i] now getting geolocation for province" + str(file_location))
    API_KEY = "eQc0edWZzHTk5nZWqpfEjNb-SUe2jg-qX_CJR6DK_KE"
    lat = []
    lng = []
    df = pd.read_csv(file_location,delimiter=',')
    line_count = 0
    
    for row in df.iterrows():
        if row[1]['lat'] == "placeholder":
            address = row[1]['full adress']
            if isinstance(address, str):
                address = str.replace(address,' ','+')
                address = str.replace(address,'-','+')
                response = requests.get(f"https://geocode.search.hereapi.com/v1/geocode?q=@{address}&apiKey={API_KEY}")
                dictionary = dict(response.json())
                lat.append(dictionary['items'][0]['position']['lat'])
                lng.append(dictionary['items'][0]['position']['lng'])
                print(str(dictionary['items'][0]['position']['lat']) +" -- " + str(dictionary['items'][0]['position']['lng']))
                line_count += 1
            else:
                address = row[1]['locality']
                if not isinstance(address,str):
                    address = "Belgique"
                    #print('ERROR no municipality' + str(address))
                address = address + " Belgique"
                response = requests.get(f"https://geocode.search.hereapi.com/v1/geocode?q=@{address}&apiKey={API_KEY}")
                dictionary = dict(response.json())
                lat.append(dictionary['items'][0]['position']['lat'])
                lng.append(dictionary['items'][0]['position']['lng'])
                line_count += 1
        else:
            lat.append(row[1]['lat'])
            lng.append(row[1]['lng'])
    df['lat'] = (lat)
    df['lng'] = (lng)
    df.to_csv(file_location, index=False)