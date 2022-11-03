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
    
    def __init__(self):
        super(Application,self).__init__()
        
        self.discover_topic = ''
        self.temperature_topic = ''
        self.humidity_topic = ''
        self.speed_topic = ''
        
        self.mqtt_broker = ''
        self.mqtt_port = 0
        
        client_id = f'MoM-{random.randint(0, 10000)}'
        username = ''
        password = ''
        
        self.sensors_list = {}
        
        self.gui_controller=GUI_Controller()
        
    def start(self):
        self.mqtt = Mqtt(client_id, username, password, self.mqtt_broker, self.mqtt_port)
        self.mqtt.client.on_message = self.on_message
        
        self.mqtt.subscribe(self.discover_topic)
        self.mqtt.subscribe(self.temperature_topic)
        self.mqtt.subscribe(self.humidity_topic)
        self.mqtt.subscribe(self.speed_topic)
        
        self.mqtt.loop_forever()
        thread = threading.Thread(target=self.run,args=())
        thread.start()
        
    def run(self):
        '''Função que roda o loop principal'''
        self.stop=False

        while self.stop == False:
            delay = random.randint(1,5)
            time.sleep(delay)
            
        print("Stopping")
            
    def on_message(self, client, userdata, msg):
        response = msg.payload.decode()
        response = response.replace("\'", '\"')
        print(response)
        json_response = json.loads(response)
        
        topic = msg.topic
        
        if topic == self.discover_topic:
            self.discover_topic_msg_handler(json_response)
            
        else:
            self.warning_topic_msg_handler(json_response)
            
    def warning_topic_msg_handler(self,json_data):
        if json_data['sensor_name'] not in self.sensors_list:
            return
        
        if self.sensors_list[json_data['sensor_name']] == 1:
            self.gui_controller.send_warning(json_data)
            
            
    def discover_topic_msg_handler(self,json_data):
        if json_data['sensor_name'] not in self.sensors_list:
            self.sensors_list[json_data['sensor_name']] = 0
            self.gui_controller.add_sensor(json_data['sensor_name'])
        
class GUI_Controller(QtCore.QObject):
    '''Sinais que comunicam com a thread da GUI'''
    widget_signal=QtCore.Signal(object)
    
    def __init__(self):
        super(GUI_Controller,self).__init__()
        
    def add_sensor(self,sensor_name):
        command = ['discover',sensor_name]
        self.widget_signal.emit(command)
        
    def send_warning(self,json_data):
        command = ['log',json_data]
        self.widget_signal.emit(command)
    