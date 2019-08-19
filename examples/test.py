#!/bin/env python

# config
HOST="crava.ch"
USER='pifou'
PASS='plop'
TOPIC="rooms/main/+"

import os
import sys

import bottle
from bottle import route, run, template

import paho.mqtt.client as mqtt

def init_mqtt():

    def on_message(client, userdata, message):
        print("message received " ,str(message.payload.decode("utf-8")))
        print("message topic=",message.topic)
        print("message qos=",message.qos)
        print("message retain flag=",message.retain)

    client = mqtt.Client("base") #create new instance

    client.on_message = on_message
    client.username_pw_set(USER, PASS)

    client.connect(HOST)

    client.loop_start()    #start the loop
    client.subscribe(TOPIC)
    return client

# http routing

@bottle.get('/static/<name:path>')
def index(name):
    return bottle.static_file(name, os.path.abspath('.'))

@bottle.get('/')
def index():
    return template('./templates/index.html')

mqtt_runner = init_mqtt()
try:
    run(host='localhost', port=8080)
except Exception as e:
    print("byebye")
    mqtt_runner.loop_stop()
