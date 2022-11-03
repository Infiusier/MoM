# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sensor_interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(798, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 800, 600))
        self.frame.setStyleSheet(u"background-color: rgb(160, 160, 160);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 171, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color:#E5E5E5;\n"
"color: #313132;\n"
"border-radius: 10px;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 90, 221, 391))
        self.frame_2.setStyleSheet(u"background-color: rgb(196, 196, 196);\n"
"border-radius: 5px;\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frame_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 30, 221, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.verticalLayoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.mqtt_broker_line_input = QLineEdit(self.frame_3)
        self.mqtt_broker_line_input.setObjectName(u"mqtt_broker_line_input")
        self.mqtt_broker_line_input.setGeometry(QRect(0, 20, 221, 20))
        self.mqtt_broker_line_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 221, 20))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.verticalLayoutWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 221, 20))
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.mqtt_port_line_input = QSpinBox(self.frame_4)
        self.mqtt_port_line_input.setObjectName(u"mqtt_port_line_input")
        self.mqtt_port_line_input.setGeometry(QRect(0, 20, 221, 20))
        self.mqtt_port_line_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.mqtt_port_line_input.setAlignment(Qt.AlignCenter)
        self.mqtt_port_line_input.setMaximum(10000)
        self.mqtt_port_line_input.setValue(1883)

        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.verticalLayoutWidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 221, 20))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.discover_topic_line_input = QLineEdit(self.frame_5)
        self.discover_topic_line_input.setObjectName(u"discover_topic_line_input")
        self.discover_topic_line_input.setGeometry(QRect(0, 20, 221, 20))
        self.discover_topic_line_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")

        self.verticalLayout.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.verticalLayoutWidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 221, 20))
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.temperature_topic_line_input = QLineEdit(self.frame_7)
        self.temperature_topic_line_input.setObjectName(u"temperature_topic_line_input")
        self.temperature_topic_line_input.setGeometry(QRect(0, 20, 221, 20))
        self.temperature_topic_line_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")

        self.verticalLayout.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.verticalLayoutWidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 221, 20))
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.humidity_topic_line_input = QLineEdit(self.frame_8)
        self.humidity_topic_line_input.setObjectName(u"humidity_topic_line_input")
        self.humidity_topic_line_input.setGeometry(QRect(0, 20, 221, 20))
        self.humidity_topic_line_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")

        self.verticalLayout.addWidget(self.frame_8)

        self.frame_6 = QFrame(self.verticalLayoutWidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 221, 20))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.speed_topic_line_input = QLineEdit(self.frame_6)
        self.speed_topic_line_input.setObjectName(u"speed_topic_line_input")
        self.speed_topic_line_input.setGeometry(QRect(0, 20, 221, 20))
        self.speed_topic_line_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")

        self.verticalLayout.addWidget(self.frame_6)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 91, 21))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.begin_button = QPushButton(self.frame_2)
        self.begin_button.setObjectName(u"begin_button")
        self.begin_button.setGeometry(QRect(70, 352, 75, 23))
        self.begin_button.setStyleSheet(u"QPushButton{\n"
"border-radius:5px;\n"
"background-color: #ebc000;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius:5px;\n"
"background-color: #605e5e;\n"
"border: 1px solid black;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-radius:5px;\n"
"background-color: #ebc000;\n"
"border: 1px solid black;\n"
"color: black;\n"
"}")
        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(310, 90, 261, 211))
        self.frame_9.setStyleSheet(u"background-color: rgb(196, 196, 196);\n"
"border-radius: 5px;\n"
"\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 101, 16))
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.sensor_type_combobox = QComboBox(self.frame_9)
        self.sensor_type_combobox.addItem("")
        self.sensor_type_combobox.addItem("")
        self.sensor_type_combobox.addItem("")
        self.sensor_type_combobox.setObjectName(u"sensor_type_combobox")
        self.sensor_type_combobox.setGeometry(QRect(109, 27, 101, 22))
        self.sensor_type_combobox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 30, 91, 16))
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 60, 47, 16))
        self.sensor_name_line_input = QLineEdit(self.frame_9)
        self.sensor_name_line_input.setObjectName(u"sensor_name_line_input")
        self.sensor_name_line_input.setGeometry(QRect(109, 60, 141, 16))
        self.sensor_name_line_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"")
        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 90, 81, 16))
        self.current_value_input = QSpinBox(self.frame_9)
        self.current_value_input.setObjectName(u"current_value_input")
        self.current_value_input.setGeometry(QRect(109, 90, 71, 16))
        self.current_value_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"")
        self.current_value_input.setAlignment(Qt.AlignCenter)
        self.current_value_input.setMaximum(1000)
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 120, 81, 16))
        self.max_value_input = QSpinBox(self.frame_9)
        self.max_value_input.setObjectName(u"max_value_input")
        self.max_value_input.setGeometry(QRect(109, 120, 71, 16))
        self.max_value_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"")
        self.max_value_input.setAlignment(Qt.AlignCenter)
        self.max_value_input.setMaximum(1000)
        self.label_14 = QLabel(self.frame_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 150, 81, 16))
        self.min_value_input = QSpinBox(self.frame_9)
        self.min_value_input.setObjectName(u"min_value_input")
        self.min_value_input.setGeometry(QRect(109, 150, 71, 16))
        self.min_value_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"")
        self.min_value_input.setAlignment(Qt.AlignCenter)
        self.min_value_input.setMaximum(1000)
        self.create_button = QPushButton(self.frame_9)
        self.create_button.setObjectName(u"create_button")
        self.create_button.setGeometry(QRect(90, 180, 75, 23))
        self.create_button.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"background-color: #49B9F8;\n"
"padding:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius:5px;\n"
"background-color: #379ed6;\n"
"border: 1px solid black;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-radius:5px;\n"
"background-color: #ebc000;\n"
"border: 1px solid black;\n"
"color: black;\n"
"}")
        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(310, 310, 261, 171))
        self.frame_10.setStyleSheet(u"background-color: rgb(196, 196, 196);\n"
"border-radius: 5px;\n"
"\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 0, 81, 31))
        self.label_15.setFont(font1)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 40, 81, 16))
        self.sensor_name_combobox = QComboBox(self.frame_10)
        self.sensor_name_combobox.addItem("")
        self.sensor_name_combobox.setObjectName(u"sensor_name_combobox")
        self.sensor_name_combobox.setGeometry(QRect(90, 38, 161, 22))
        self.sensor_name_combobox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.sensor_value_input = QSpinBox(self.frame_10)
        self.sensor_value_input.setObjectName(u"sensor_value_input")
        self.sensor_value_input.setGeometry(QRect(90, 68, 161, 22))
        self.sensor_value_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"")
        self.sensor_value_input.setAlignment(Qt.AlignCenter)
        self.sensor_value_input.setMaximum(1000)
        self.label_17 = QLabel(self.frame_10)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(11, 70, 75, 16))
        self.delete_button = QPushButton(self.frame_10)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(180, 140, 75, 23))
        self.delete_button.setStyleSheet(u"QPushButton{\n"
"border-radius:5px;\n"
"background-color: red;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius:5px;\n"
"background-color: #605e5e;\n"
"border: 1px solid black;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-radius:5px;\n"
"background-color: #ebc000;\n"
"border: 1px solid black;\n"
"color: black;\n"
"}")
        self.ok_button = QPushButton(self.frame_10)
        self.ok_button.setObjectName(u"ok_button")
        self.ok_button.setGeometry(QRect(10, 140, 75, 23))
        self.ok_button.setStyleSheet(u"QPushButton{\n"
"border-radius:5px;\n"
"background-color: #ebc000;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius:5px;\n"
"background-color: #605e5e;\n"
"border: 1px solid black;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-radius:5px;\n"
"background-color: #ebc000;\n"
"border: 1px solid black;\n"
"color: black;\n"
"}")
        self.label_19 = QLabel(self.frame_10)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 100, 71, 16))
        self.label_20 = QLabel(self.frame_10)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(130, 100, 71, 16))
        self.max_value_label = QLabel(self.frame_10)
        self.max_value_label.setObjectName(u"max_value_label")
        self.max_value_label.setGeometry(QRect(70, 100, 47, 20))
        self.max_value_label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.max_value_label.setAlignment(Qt.AlignCenter)
        self.min_value_label = QLabel(self.frame_10)
        self.min_value_label.setObjectName(u"min_value_label")
        self.min_value_label.setGeometry(QRect(190, 100, 47, 20))
        self.min_value_label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.min_value_label.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 0, 800, 20))
        self.label_18.setStyleSheet(u"background-color: #ebc000;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IoT Sensor Monitor", None))
        self.mqtt_broker_line_input.setText(QCoreApplication.translate("MainWindow", u"broker.hivemq.com", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MQTT Broker", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"MQTT Port", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Discover Topic", None))
        self.discover_topic_line_input.setText(QCoreApplication.translate("MainWindow", u"MoM Discover", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Temperature Topic", None))
        self.temperature_topic_line_input.setText(QCoreApplication.translate("MainWindow", u"MoM Temperature", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Humidity Topic", None))
        self.humidity_topic_line_input.setText(QCoreApplication.translate("MainWindow", u"MoM Humidity", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Speed Topic", None))
        self.speed_topic_line_input.setText(QCoreApplication.translate("MainWindow", u"MoM Speed", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Configurations", None))
        self.begin_button.setText(QCoreApplication.translate("MainWindow", u"Begin", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Create Sensors", None))
        self.sensor_type_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.sensor_type_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.sensor_type_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Speed", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Sensor Type:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Current Value:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Max Value:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Min Value:", None))
        self.create_button.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Edit Sensor", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Sensor Name:", None))
        self.sensor_name_combobox.setItemText(0, "")

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Current Value:", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.ok_button.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Max Value:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Min Value:", None))
        self.max_value_label.setText("")
        self.min_value_label.setText("")
        self.label_18.setText("")
    # retranslateUi

