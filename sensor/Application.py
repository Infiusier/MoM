# coding: utf-8
from ast import Return
import time,threading,os,json
from datetime import datetime
from intelhex import IntelHex
from queue import Queue
from enum import Enum,auto
import random

from PySide2.QtCore import QThread
from PySide2 import QtCore

from mqtt import *

class Application():
    
    def __init__(self,sensor_type,sensor_name,current_value,max_value,min_value,discover_topic,topic,mqtt_broker,mqtt_port):
        super(Application,self).__init__()
        
        self.sensor_type = sensor_type
        self.sensor_name = sensor_name
        self.current_value = current_value
        self.max_value = max_value
        self.min_value = min_value
        
        self.discover_topic = discover_topic
        self.topic = topic
        
        self.mqtt_broker = mqtt_broker
        self.mqtt_port = mqtt_port
        
        client_id = f'MoM-{random.randint(0, 10000)}'
        username = ''
        password = ''
        
        self.mqtt = Mqtt(client_id, username, password, self.mqtt_broker, self.mqtt_port)
        #self.mqtt.loop_forever()
        
        
    def start(self):
        thread = threading.Thread(target=self.run,args=())
        thread.start()
        
    def run(self):
        '''Função que roda o loop principal'''
        self.stop=False

        while self.stop == False:
            delay = random.randint(1,5)
            time.sleep(delay)
            
            self.send_discover_signal()
            self.send_current_value()
            
        print("Stopping")
            
    def send_discover_signal(self):
        json_payload = {}
        json_payload['sensor_type'] = self.sensor_type
        json_payload['sensor_name'] = self.sensor_name
        
        str_payload = "{}".format(json_payload)
        
        self.mqtt.publish(self.discover_topic,str_payload)
    
    def send_current_value(self):
        
        if not (self.current_value > self.max_value or self.current_value < self.min_value):
            return
        
        if self.current_value > self.max_value:
            warning_msg = "Sensor beyond threshold!"
            
        elif self.current_value < self.min_value:
            warning_msg = "Sensor bellow threshold!"    
        
        json_payload = {}
        json_payload['sensor_name'] = self.sensor_name
        json_payload['sensor_type'] = self.sensor_type
        json_payload['sensor_value'] = self.current_value
        json_payload['warning'] = warning_msg
        
        str_payload = "{}".format(json_payload)
        
        self.mqtt.publish(self.topic,str_payload)
        
        