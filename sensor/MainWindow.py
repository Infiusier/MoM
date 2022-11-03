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
        
        self.list_of_sensors = {}
        
        '''Configura as telas'''
        self.prepare_initial_screen()

        self.begin_button.clicked.connect(self.init_application)
        self.create_button.clicked.connect(self.init_sensor)
        self.ok_button.clicked.connect(self.edit_sensor)
        self.delete_button.clicked.connect(self.delete_sensor)
        self.sensor_name_combobox.currentIndexChanged.connect(self.display_sensor_info)
#--------------------------------------------------- PREPARE SCREENS ------------------------------------------------------
    def prepare_initial_screen(self):
        self.frame_9.setEnabled(False)
        self.frame_10.setEnabled(False)

#---------------------------------------------------BEGIN TESTS CALLBACKS---------------------------------------------------

    def init_application(self):
        self.frame_2.setEnabled(False)
        self.frame_9.setEnabled(True)
        self.frame_10.setEnabled(True)
        
    def init_sensor(self):
        
        if len(self.sensor_name_line_input.text()) == 0:
            return

        sensor_type = self.sensor_type_combobox.currentText()
        sensor_name = self.sensor_name_line_input.text()
        current_value = self.current_value_input.value()
        max_value = self.max_value_input.value()
        min_value = self.min_value_input.value()
        
        discover_topic = self.discover_topic_line_input.text()
        mqtt_broker = self.mqtt_broker_line_input.text()
        mqtt_port = self.mqtt_port_line_input.value()
        
        topic = {'Temperature' : self.temperature_topic_line_input.text(),
                 'Humidity' : self.humidity_topic_line_input.text(),
                 'Speed' : self.speed_topic_line_input.text()}
        
        app = Application(sensor_type,
                          sensor_name,
                          current_value,
                          max_value,
                          min_value,
                          discover_topic,
                          topic[sensor_type],
                          mqtt_broker,
                          mqtt_port
                          )
        
        self.list_of_sensors[sensor_name] = app
        self.list_of_sensors[sensor_name].start()
        
        self.sensor_name_line_input.clear()
        self.sensor_name_combobox.addItem(sensor_name)
        
    def display_sensor_info(self):
        if self.sensor_name_combobox.currentText() == '':
            self.max_value_label.setText("")
            self.min_value_label.setText("")
            self.sensor_value_input.setValue(0)
            return
        
        sensor_name = self.sensor_name_combobox.currentText()
        max_value = self.list_of_sensors[sensor_name].max_value
        min_value = self.list_of_sensors[sensor_name].min_value
        current_value = self.list_of_sensors[sensor_name].current_value
        
        self.max_value_label.setText(str(max_value))
        self.min_value_label.setText(str(min_value))
        self.sensor_value_input.setValue(current_value)
        
    def edit_sensor(self):
        if self.sensor_name_combobox.currentText() == '':
            return
        
        sensor_name = self.sensor_name_combobox.currentText()
        self.list_of_sensors[sensor_name].current_value = self.sensor_value_input.value()
        
        self.sensor_name_combobox.setCurrentIndex(0)
        self.display_sensor_info()
        
    def delete_sensor(self):
        if self.sensor_name_combobox.currentText() == '':
            return
        
        sensor_name = self.sensor_name_combobox.currentText()
        self.list_of_sensors[sensor_name].stop = True
        
        self.sensor_name_combobox.removeItem(self.sensor_name_combobox.currentIndex())
        self.sensor_name_combobox.setCurrentIndex(0)
        self.sensor_value_input.setValue(0)
        
        
            