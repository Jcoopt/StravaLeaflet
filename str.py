# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 15:10:29 2018

@author: Joseph
"""
import matplotlib.pyplot as plt
import mplleaflet

from stravalib.client import Client

def getLatLongData(act_id,client,types):
    streams = client.get_activity_streams(act_id, types=types, resolution='medium')
    if 'latlng' in streams.keys():
        latlongData=streams['latlng'].data
    
    return latlongData
def arrangeLatLonData(latlongData):
    lat=[]
    lon=[]
    for coord in latlongData:
        lat.append(coord[0])
        lon.append(coord[1])
    return lat,lon

def plotData(lat,lon):
    plt.plot(lon, lat, 'b') # Draw blue line
    plt.plot(lon, lat, 'rs')

def main():
    """this is the main function for the cycle mapping program. It calls everything else"""
    act_dict={}
    client=Client(access_token="ACCESS_TOKEN_HERE ")
    activities = client.get_activities(limit=1)
    for activity in activities:
        act_dict[activity.name]=activity.id
    print(act_dict)
    types = ['time', 'latlng', 'altitude', 'heartrate', 'temp', ]
    for item in act_dict:
        rawLatLong=getLatLongData(act_dict[item],client,types)
        lat,long=arrangeLatLonData(rawLatLong)
        plotData(lat,long)
    mplleaflet.show()
main()