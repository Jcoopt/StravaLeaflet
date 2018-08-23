# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 12:06:34 2018
This program doesn't actually map anythin, but is useful for showing the logic
@author: Joseph
"""
import matplotlib.pyplot as plt
import mplleaflet

from stravalib.client import Client

def main():
    """this is the main function for the cycle mapping program. It calls everything else"""
    act_dict={}
    client=Client(access_token="ACCESS_TOKEN_HERE ")
    activities = client.get_activities(limit=1)
    for activity in activities:
        act_dict[activity.name]=activity.id
        streams = client.get_activity_streams(activity.id,types = ['time', 'latlng', 'altitude', 'heartrate', 'temp', ], resolution='medium')
        print(streams.keys())
    print(act_dict)
main()
