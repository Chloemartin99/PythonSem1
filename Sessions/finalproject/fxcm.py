import pandas as pd
import json
import requests
import fxcmpy
from socketIO_client import SocketIO

TRADING_API_URL = 'https://api-demo.fxcm.com:443'
WEBSOCKET_PORT = 443

ACCESS_TOKEN = "c9828dd51da672e51cf4afcb8d51b625a2fefea3"

def on_connect():
    print('Websocket Connected: ' + socketIO._engineIO_session.id)

def on_close():
    print('Websocket Closed.')

socketIO = SocketIO(TRADING_API_URL, WEBSOCKET_PORT, params={'access_token': ACCESS_TOKEN})

socketIO.on('connect', on_connect) #llamalo al method pero si no haces click no - lo pasa por encima??
socketIO.on('disconnect', on_close)

bearer_access_token = "Bearer " + socketIO._engineIO_session.id + ACCESS_TOKEN

print(bearer_access_token)

method = '/candles/1/H1'

hist_response = requests.get(TRADING_API_URL + method,
                             headers = {
                                 'User-Agent': 'request',
                                 'Authorization': bearer_access_token,
                                 'Accept': 'application/json',
                                 'Content-Type': 'application/x-www-form-urlencoded'
                             },
                             params = {
                                 'num': 1000,
                                 'from': 1494086400,
                                 'to': 1503835200
                             })

print(hist_response)

print(hist_response.json()) #json is to return data
