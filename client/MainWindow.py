# coding: utf-8
import argparse

from PySide2.QtCore import (QPropertyAnimation, QCoreApplication, QDate, QDateTime, QMetaObject,QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2 import QtWidgets, QtCore    
from PySide2.QtCore import *
from screen import Ui_MainWindow
from Application import *

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow,QtCore.QObject):
    
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        
        self.app_thread = Application()
        
        '''Configura as telas'''
        self.prepare_initial_screen()

        self.begin_button.clicked.connect(self.init_application)
        self.app_thread.gui_controller.widget_signal.connect(self.handle_gui_signals)
        self.available_sensors_combobox.currentIndexChanged.connect(self.listen_to_sensor_combobox)
        self.monitor_sensor_checkbox.stateChanged.connect(self.add_sensor_to_listen_list)
            
#--------------------------------------------------- PREPARE SCREENS ------------------------------------------------------
    def prepare_initial_screen(self):
        self.frame_9.setEnabled(False)

#---------------------------------------------------BEGIN TESTS CALLBACKS---------------------------------------------------
    
    def init_application_inputs(self):
        self.app_thread.discover_topic = self.discover_topic_line_input.text()
        self.app_thread.temperature_topic = self.temperature_topic_line_input.text()
        self.app_thread.humidity_topic = self.humidity_topic_line_input.text()
        self.app_thread.speed_topic = self.speed_topic_line_input.text()
        self.app_thread.mqtt_broker = self.mqtt_broker_line_input.text()
        self.app_thread.mqtt_port = self.mqtt_port_line_input.value()

    def init_application(self):
        self.frame_2.setEnabled(False)
        self.frame_9.setEnabled(True)
        self.init_application_inputs()
        self.app_thread.start()
        
    def listen_to_sensor_combobox(self):
        if not(self.available_sensors_combobox.currentText() in self.app_thread.sensors_list):
            return
               
        state = self.app_thread.sensors_list[self.available_sensors_combobox.currentText()]
        self.monitor_sensor_checkbox.setChecked(state)

    def add_sensor_to_listen_list(self):
        if self.monitor_sensor_checkbox.isChecked():
            self.app_thread.sensors_list[self.available_sensors_combobox.currentText()] = 1
        
        else:
            self.app_thread.sensors_list[self.available_sensors_combobox.currentText()] = 0
            
    def add_to_log(self,json_data):
        
        sensor_type = json_data['sensor_type']
        msg = "Sensor: %s ;Current Value: %d ;Warning: %s" % (json_data['sensor_name'],json_data['sensor_value'],json_data['warning'])
        
        if sensor_type == 'Temperature':
            self.temperature_log.append(msg)
            
        elif sensor_type == 'Humidity':
            self.humidity_log.append(msg)
            
        elif sensor_type == 'Speed':
            self.speed_log.append(msg)
            
    def add_sensor_to_list(self,sensor_name):
        self.available_sensors_combobox.addItem(sensor_name)
        
    def handle_gui_signals(self,parameters):
        if parameters[0] == 'log':
            self.add_to_log(parameters[1])
        
        if parameters[0] == 'discover':
            self.add_sensor_to_list(parameters[1])
        