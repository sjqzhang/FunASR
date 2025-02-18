#!/bin/bash


source venv/bin/activate


nohup python runtime/html5/h5Server.py 2>&1 &

python runtime/python/websocket/funasr_wss_server.py 

