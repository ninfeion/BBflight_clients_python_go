# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\BBflight\python_ninfeion\eric_workspace\pyqt_demo1\main_3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import global_variable
import bbapi,threading,time

class Ui_BBUI(object):
    def __init__(self):
        super().__init__()
        self._recieveTextBrowserUpdate = True

    def setupUi(self, BBUI):
        BBUI.setObjectName("BBUI")
        BBUI.setEnabled(True)

        BBUI.resize(900, 725)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BBUI.sizePolicy().hasHeightForWidth())
        BBUI.setSizePolicy(sizePolicy)

        BBUI.setMinimumSize(QtCore.QSize(900, 725))
        BBUI.setMaximumSize(QtCore.QSize(1400, 800))
        BBUI.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        BBUI.setMouseTracking(False)
        BBUI.setWindowTitle("BBflight Clients")
        self.centralwidget = QtWidgets.QWidget(BBUI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.gridLayout_1_1 = QtWidgets.QGridLayout()
        self.gridLayout_1_1.setObjectName("gridLayout_1_1")
        spacerItem = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_1_1.addItem(spacerItem, 1, 3, 1, 2)
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setObjectName("connect_button")
        self.gridLayout_1_1.addWidget(self.connect_button, 1, 0, 1, 1)
        self.battery_progress = QtWidgets.QProgressBar(self.centralwidget)
        self.battery_progress.setProperty("value", 100)
        self.battery_progress.setTextVisible(False)
        self.battery_progress.setObjectName("battery_progress")
        self.gridLayout_1_1.addWidget(self.battery_progress, 1, 6, 1, 1)
        self.address_setting_button = QtWidgets.QPushButton(self.centralwidget)
        self.address_setting_button.setObjectName("address_setting_button")
        self.gridLayout_1_1.addWidget(self.address_setting_button, 1, 1, 1, 1)
        self.link_quality_progress = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.link_quality_progress.sizePolicy().hasHeightForWidth())
        self.link_quality_progress.setSizePolicy(sizePolicy)
        self.link_quality_progress.setProperty("value", 100)
        self.link_quality_progress.setTextVisible(False)
        self.link_quality_progress.setObjectName("link_quality_progress")
        self.gridLayout_1_1.addWidget(self.link_quality_progress, 1, 8, 1, 1)
        self.link_quality_label = QtWidgets.QLabel(self.centralwidget)
        self.link_quality_label.setObjectName("link_quality_label")
        self.gridLayout_1_1.addWidget(self.link_quality_label, 2, 8, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_1_1.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.battery_label = QtWidgets.QLabel(self.centralwidget)
        self.battery_label.setObjectName("battery_label")
        self.gridLayout_1_1.addWidget(self.battery_label, 2, 6, 1, 1)
        self.verticalLayout_1.addLayout(self.gridLayout_1_1)
        self.gridLayout.addLayout(self.verticalLayout_1, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.page_flight_control = QtWidgets.QWidget()
        self.page_flight_control.setObjectName("page_flight_control")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_flight_control)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.expansion_function_groupbox = QtWidgets.QGroupBox(self.page_flight_control)
        self.expansion_function_groupbox.setObjectName("expansion_function_groupbox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.expansion_function_groupbox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.led_mode_label = QtWidgets.QLabel(self.expansion_function_groupbox)
        self.led_mode_label.setObjectName("led_mode_label")
        self.gridLayout_7.addWidget(self.led_mode_label, 0, 0, 1, 1)
        self.led_mode_combobox = QtWidgets.QComboBox(self.expansion_function_groupbox)
        self.led_mode_combobox.setObjectName("led_mode_combobox")
        self.gridLayout_7.addWidget(self.led_mode_combobox, 0, 1, 1, 1)
        self.expansion_function_groupbox_checkBox_2 = QtWidgets.QCheckBox(self.expansion_function_groupbox)
        self.expansion_function_groupbox_checkBox_2.setEnabled(False)
        self.expansion_function_groupbox_checkBox_2.setObjectName("expansion_function_groupbox_checkBox_2")
        self.gridLayout_7.addWidget(self.expansion_function_groupbox_checkBox_2, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.expansion_function_groupbox, 2, 0, 1, 1)
        self.basic_control_groupbox = QtWidgets.QGroupBox(self.page_flight_control)
        self.basic_control_groupbox.setObjectName("basic_control_groupbox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.basic_control_groupbox)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.roll_trim_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.basic_control_groupbox)
        self.roll_trim_doubleSpinBox.setObjectName("roll_trim_doubleSpinBox")
        self.gridLayout_5.addWidget(self.roll_trim_doubleSpinBox, 4, 1, 1, 1)
        self.flight_mode_label = QtWidgets.QLabel(self.basic_control_groupbox)
        self.flight_mode_label.setObjectName("flight_mode_label")
        self.gridLayout_5.addWidget(self.flight_mode_label, 1, 0, 1, 1)
        self.flight_mode_combobox = QtWidgets.QComboBox(self.basic_control_groupbox)
        self.flight_mode_combobox.setObjectName("flight_mode_combobox")
        self.gridLayout_5.addWidget(self.flight_mode_combobox, 1, 1, 1, 1)
        self.basic_control_groupbox_checkBox_1 = QtWidgets.QCheckBox(self.basic_control_groupbox)
        self.basic_control_groupbox_checkBox_1.setObjectName("basic_control_groupbox_checkBox_1")
        self.gridLayout_5.addWidget(self.basic_control_groupbox_checkBox_1, 7, 0, 1, 1)
        self.pitch_trim_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.basic_control_groupbox)
        self.pitch_trim_doubleSpinBox.setObjectName("pitch_trim_doubleSpinBox")
        self.gridLayout_5.addWidget(self.pitch_trim_doubleSpinBox, 6, 1, 1, 1)
        self.thrus_mode_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.basic_control_groupbox)
        self.thrus_mode_doubleSpinBox.setObjectName("thrus_mode_doubleSpinBox")
        self.gridLayout_5.addWidget(self.thrus_mode_doubleSpinBox, 3, 1, 1, 1)
        self.basic_control_groupbox_radioButton_3 = QtWidgets.QRadioButton(self.basic_control_groupbox)
        self.basic_control_groupbox_radioButton_3.setObjectName("basic_control_groupbox_radioButton_3")
        self.gridLayout_5.addWidget(self.basic_control_groupbox_radioButton_3, 8, 1, 1, 1)
        self.basic_control_groupbox_radioButton_2 = QtWidgets.QRadioButton(self.basic_control_groupbox)
        self.basic_control_groupbox_radioButton_2.setObjectName("basic_control_groupbox_radioButton_2")
        self.gridLayout_5.addWidget(self.basic_control_groupbox_radioButton_2, 8, 0, 1, 1)
        self.basic_control_groupbox_radioButton_1 = QtWidgets.QRadioButton(self.basic_control_groupbox)
        self.basic_control_groupbox_radioButton_1.setObjectName("basic_control_groupbox_radioButton_1")
        self.gridLayout_5.addWidget(self.basic_control_groupbox_radioButton_1, 7, 1, 1, 1)
        self.roll_trim_label = QtWidgets.QLabel(self.basic_control_groupbox)
        self.roll_trim_label.setObjectName("roll_trim_label")
        self.gridLayout_5.addWidget(self.roll_trim_label, 4, 0, 1, 1)
        self.pitch_trim_label = QtWidgets.QLabel(self.basic_control_groupbox)
        self.pitch_trim_label.setObjectName("pitch_trim_label")
        self.gridLayout_5.addWidget(self.pitch_trim_label, 6, 0, 1, 1)
        self.thrust_mode_label = QtWidgets.QLabel(self.basic_control_groupbox)
        self.thrust_mode_label.setObjectName("thrust_mode_label")
        self.gridLayout_5.addWidget(self.thrust_mode_label, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.basic_control_groupbox, 0, 0, 1, 1)
        self.adcanced_flight_control_groupBox = QtWidgets.QGroupBox(self.page_flight_control)
        self.adcanced_flight_control_groupBox.setObjectName("adcanced_flight_control_groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.adcanced_flight_control_groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.max_angle_rate_label = QtWidgets.QLabel(self.adcanced_flight_control_groupBox)
        self.max_angle_rate_label.setObjectName("max_angle_rate_label")
        self.gridLayout_6.addWidget(self.max_angle_rate_label, 0, 0, 1, 1)
        self.max_yaw_angle_rate_label = QtWidgets.QLabel(self.adcanced_flight_control_groupBox)
        self.max_yaw_angle_rate_label.setObjectName("max_yaw_angle_rate_label")
        self.gridLayout_6.addWidget(self.max_yaw_angle_rate_label, 1, 0, 1, 1)
        self.slewlimit_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.adcanced_flight_control_groupBox)
        self.slewlimit_doubleSpinBox.setObjectName("slewlimit_doubleSpinBox")
        self.gridLayout_6.addWidget(self.slewlimit_doubleSpinBox, 4, 1, 1, 1)
        self.min_thrust_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.adcanced_flight_control_groupBox)
        self.min_thrust_doubleSpinBox.setObjectName("min_thrust_doubleSpinBox")
        self.gridLayout_6.addWidget(self.min_thrust_doubleSpinBox, 3, 1, 1, 1)
        self.thrust_lowering_slewrate_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.adcanced_flight_control_groupBox)
        self.thrust_lowering_slewrate_doubleSpinBox.setObjectName("thrust_lowering_slewrate_doubleSpinBox")
        self.gridLayout_6.addWidget(self.thrust_lowering_slewrate_doubleSpinBox, 5, 1, 1, 1)
        self.max_thrust_label_2 = QtWidgets.QLabel(self.adcanced_flight_control_groupBox)
        self.max_thrust_label_2.setObjectName("max_thrust_label_2")
        self.gridLayout_6.addWidget(self.max_thrust_label_2, 2, 0, 1, 1)
        self.min_thrust_label = QtWidgets.QLabel(self.adcanced_flight_control_groupBox)
        self.min_thrust_label.setObjectName("min_thrust_label")
        self.gridLayout_6.addWidget(self.min_thrust_label, 3, 0, 1, 1)
        self.slewlimit_label = QtWidgets.QLabel(self.adcanced_flight_control_groupBox)
        self.slewlimit_label.setObjectName("slewlimit_label")
        self.gridLayout_6.addWidget(self.slewlimit_label, 4, 0, 1, 1)
        self.thrust_lowering_slewrate_label = QtWidgets.QLabel(self.adcanced_flight_control_groupBox)
        self.thrust_lowering_slewrate_label.setObjectName("thrust_lowering_slewrate_label")
        self.gridLayout_6.addWidget(self.thrust_lowering_slewrate_label, 5, 0, 1, 1)
        self.max_angle_doubleSpinBox = QtWidgets.QSpinBox(self.adcanced_flight_control_groupBox)
        self.max_angle_doubleSpinBox.setObjectName("max_angle_doubleSpinBox")
        self.gridLayout_6.addWidget(self.max_angle_doubleSpinBox, 0, 1, 1, 1)
        self.max_yaw_angle_doubleSpinBox = QtWidgets.QSpinBox(self.adcanced_flight_control_groupBox)
        self.max_yaw_angle_doubleSpinBox.setObjectName("max_yaw_angle_doubleSpinBox")
        self.gridLayout_6.addWidget(self.max_yaw_angle_doubleSpinBox, 1, 1, 1, 1)
        self.max_thrust_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.adcanced_flight_control_groupBox)
        self.max_thrust_doubleSpinBox.setObjectName("max_thrust_doubleSpinBox")
        self.gridLayout_6.addWidget(self.max_thrust_doubleSpinBox, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.adcanced_flight_control_groupBox, 1, 0, 1, 1)
        self.filght_status_groupbox = QtWidgets.QGroupBox(self.page_flight_control)
        self.filght_status_groupbox.setObjectName("filght_status_groupbox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.filght_status_groupbox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2_1 = QtWidgets.QGridLayout()
        self.gridLayout_2_1.setObjectName("gridLayout_2_1")
        self.thrust_label = QtWidgets.QLabel(self.filght_status_groupbox)
        self.thrust_label.setObjectName("thrust_label")
        self.gridLayout_2_1.addWidget(self.thrust_label, 1, 1, 1, 1)
        self.thrust_actual_lineEdit = QtWidgets.QLineEdit(self.filght_status_groupbox)
        self.thrust_actual_lineEdit.setObjectName("thrust_actual_lineEdit")
        self.gridLayout_2_1.addWidget(self.thrust_actual_lineEdit, 1, 3, 1, 1)
        self.resevered_label_1 = QtWidgets.QLabel(self.filght_status_groupbox)
        self.resevered_label_1.setObjectName("resevered_label_1")
        self.gridLayout_2_1.addWidget(self.resevered_label_1, 5, 1, 1, 1)
        self.thrust_target_lineEdit = QtWidgets.QLineEdit(self.filght_status_groupbox)
        self.thrust_target_lineEdit.setObjectName("thrust_target_lineEdit")
        self.gridLayout_2_1.addWidget(self.thrust_target_lineEdit, 1, 2, 1, 1)
        self.pitch_target_lineEdit = QtWidgets.QLineEdit(self.filght_status_groupbox)
        self.pitch_target_lineEdit.setObjectName("pitch_target_lineEdit")
        self.gridLayout_2_1.addWidget(self.pitch_target_lineEdit, 2, 2, 1, 1)
        self.yaw_label = QtWidgets.QLabel(self.filght_status_groupbox)
        self.yaw_label.setObjectName("yaw_label")
        self.gridLayout_2_1.addWidget(self.yaw_label, 4, 1, 1, 1)
        self.resevered_lineEdit_1 = QtWidgets.QLineEdit(self.filght_status_groupbox)
        self.resevered_lineEdit_1.setEnabled(False)
        self.resevered_lineEdit_1.setObjectName("resevered_lineEdit_1")
        self.gridLayout_2_1.addWidget(self.resevered_lineEdit_1, 5, 2, 1, 1)
        self.roll_label = QtWidgets.QLabel(self.filght_status_groupbox)
        self.roll_label.setObjectName("roll_label")
        self.gridLayout_2_1.addWidget(self.roll_label, 3, 1, 1, 1)
        self.yaw_actual_lineEdit = QtWidgets.QLineEdit(self.filght_status_groupbox)
        self.yaw_actual_lineEdit.setObjectName("yaw_actual_lineEdit")
        self.gridLayout_2_1.addWidget(self.yaw_actual_lineEdit, 4, 3, 1, 1)
        self.yaw_target_lineEdit = QtWidgets.QLineEdit(self.filght_status_groupbox)
        self.yaw_target_lineEdit.setObjectName("yaw_target_lineEdit")
        self.gridLayout_2_1.addWidget(self.yaw_target_lineEdit, 4, 2, 1, 1)
        self.roll_actual_lineEdit = QtWidgets.QLineEdit(self.filght_status_groupbox)
        self.roll_actual_lineEdit.setObjectName("roll_actual_lineEdit")
        self.gridLayout_2_1.addWidget(self.roll_actual_lineEdit, 3, 3, 1, 1)
        self.resevered_lineEdit_2 = QtWidgets.QLineEdit(self.filght_status_groupbox)
        self.resevered_lineEdit_2.setEnabled(False)
        self.resevered_lineEdit_2.setObjectName("resevered_lineEdit_2")
        self.gridLayout_2_1.addWidget(self.resevered_lineEdit_2, 5, 3, 1, 1)
        self.roll_target_lineEdit = QtWidgets.QLineEdit(self.filght_status_groupbox)
        self.roll_target_lineEdit.setObjectName("roll_target_lineEdit")
        self.gridLayout_2_1.addWidget(self.roll_target_lineEdit, 3, 2, 1, 1)
        self.pitch_label = QtWidgets.QLabel(self.filght_status_groupbox)
        self.pitch_label.setObjectName("pitch_label")
        self.gridLayout_2_1.addWidget(self.pitch_label, 2, 1, 1, 1)
        self.pitch_actual_lineEdit = QtWidgets.QLineEdit(self.filght_status_groupbox)
        self.pitch_actual_lineEdit.setObjectName("pitch_actual_lineEdit")
        self.gridLayout_2_1.addWidget(self.pitch_actual_lineEdit, 2, 3, 1, 1)
        self.target_label = QtWidgets.QLabel(self.filght_status_groupbox)
        self.target_label.setObjectName("target_label")
        self.gridLayout_2_1.addWidget(self.target_label, 0, 2, 1, 1)
        self.actual_label = QtWidgets.QLabel(self.filght_status_groupbox)
        self.actual_label.setObjectName("actual_label")
        self.gridLayout_2_1.addWidget(self.actual_label, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_2_1, 0, 0, 1, 1)
        self.verticalLayout_2_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2_2.setObjectName("verticalLayout_2_2")
        self.horizontalLayout_2_2_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2_2_1.setObjectName("horizontalLayout_2_2_1")
        self.Thr_label = QtWidgets.QLabel(self.filght_status_groupbox)
        self.Thr_label.setObjectName("Thr_label")
        self.horizontalLayout_2_2_1.addWidget(self.Thr_label)
        self.M1_label = QtWidgets.QLabel(self.filght_status_groupbox)
        self.M1_label.setObjectName("M1_label")
        self.horizontalLayout_2_2_1.addWidget(self.M1_label)
        self.M2_label = QtWidgets.QLabel(self.filght_status_groupbox)
        self.M2_label.setObjectName("M2_label")
        self.horizontalLayout_2_2_1.addWidget(self.M2_label)
        self.M3_label = QtWidgets.QLabel(self.filght_status_groupbox)
        self.M3_label.setObjectName("M3_label")
        self.horizontalLayout_2_2_1.addWidget(self.M3_label)
        self.M4_label = QtWidgets.QLabel(self.filght_status_groupbox)
        self.M4_label.setObjectName("M4_label")
        self.horizontalLayout_2_2_1.addWidget(self.M4_label)
        self.verticalLayout_2_2.addLayout(self.horizontalLayout_2_2_1)
        self.horizontalLayout_2_2_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2_2_2.setObjectName("horizontalLayout_2_2_2")
        self.Thr_progressBar = QtWidgets.QProgressBar(self.filght_status_groupbox)
        self.Thr_progressBar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Thr_progressBar.sizePolicy().hasHeightForWidth())
        self.Thr_progressBar.setSizePolicy(sizePolicy)
        self.Thr_progressBar.setProperty("value", 100)
        self.Thr_progressBar.setTextVisible(False)
        self.Thr_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.Thr_progressBar.setObjectName("Thr_progressBar")
        self.horizontalLayout_2_2_2.addWidget(self.Thr_progressBar)
        self.M1_progressBar = QtWidgets.QProgressBar(self.filght_status_groupbox)
        self.M1_progressBar.setProperty("value", 50)
        self.M1_progressBar.setTextVisible(False)
        self.M1_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.M1_progressBar.setObjectName("M1_progressBar")
        self.horizontalLayout_2_2_2.addWidget(self.M1_progressBar)
        self.M2_progressBar = QtWidgets.QProgressBar(self.filght_status_groupbox)
        self.M2_progressBar.setProperty("value", 50)
        self.M2_progressBar.setTextVisible(False)
        self.M2_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.M2_progressBar.setObjectName("M2_progressBar")
        self.horizontalLayout_2_2_2.addWidget(self.M2_progressBar)
        self.M3_progressBar = QtWidgets.QProgressBar(self.filght_status_groupbox)
        self.M3_progressBar.setProperty("value", 50)
        self.M3_progressBar.setTextVisible(False)
        self.M3_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.M3_progressBar.setObjectName("M3_progressBar")
        self.horizontalLayout_2_2_2.addWidget(self.M3_progressBar)
        self.M4_progressBar = QtWidgets.QProgressBar(self.filght_status_groupbox)
        self.M4_progressBar.setProperty("value", 50)
        self.M4_progressBar.setTextVisible(False)
        self.M4_progressBar.setOrientation(QtCore.Qt.Vertical)
        self.M4_progressBar.setObjectName("M4_progressBar")
        self.horizontalLayout_2_2_2.addWidget(self.M4_progressBar)
        self.verticalLayout_2_2.addLayout(self.horizontalLayout_2_2_2)
        self.gridLayout_2.addLayout(self.verticalLayout_2_2, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.flight_attitude_show = QtWidgets.QFrame(self.filght_status_groupbox)
        self.flight_attitude_show.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.flight_attitude_show.setFrameShadow(QtWidgets.QFrame.Raised)
        self.flight_attitude_show.setObjectName("flight_attitude_show")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.flight_attitude_show)
        self.gridLayout_13.setObjectName("gridLayout_13")
        spacerItem1 = QtWidgets.QSpacerItem(20, 405, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_13.addItem(spacerItem1, 0, 2, 1, 1)
        self.flight_angle_pic_label = QtWidgets.QLabel(self.flight_attitude_show)
        self.flight_angle_pic_label.setObjectName("flight_angle_pic_label")
        self.gridLayout_13.addWidget(self.flight_angle_pic_label, 0, 1, 1, 1)
        self.gridLayout_8.addWidget(self.flight_attitude_show, 1, 0, 2, 1)
        self.gridLayout_3.addWidget(self.filght_status_groupbox, 0, 1, 4, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 3, 0, 1, 1)
        self.tabWidget.addTab(self.page_flight_control, "")
        self.page_controller_setting = QtWidgets.QWidget()
        self.page_controller_setting.setObjectName("page_controller_setting")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_controller_setting)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.controlle_mapping_setting_groupBox = QtWidgets.QGroupBox(self.page_controller_setting)
        self.controlle_mapping_setting_groupBox.setObjectName("controlle_mapping_setting_groupBox")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.controlle_mapping_setting_groupBox)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.mapping_view_frame = QtWidgets.QFrame(self.controlle_mapping_setting_groupBox)
        self.mapping_view_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mapping_view_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mapping_view_frame.setObjectName("mapping_view_frame")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.mapping_view_frame)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.mapping_view_pic_label = QtWidgets.QLabel(self.mapping_view_frame)
        self.mapping_view_pic_label.setObjectName("mapping_view_pic_label")
        self.gridLayout_10.addWidget(self.mapping_view_pic_label, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.mapping_view_frame, 4, 0, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem3, 1, 1, 1, 1)
        self.dev_scan_pushButton = QtWidgets.QPushButton(self.controlle_mapping_setting_groupBox)
        self.dev_scan_pushButton.setObjectName("dev_scan_pushButton")
        self.gridLayout_9.addWidget(self.dev_scan_pushButton, 1, 0, 1, 1)
        self.dev_view_comboBox = QtWidgets.QComboBox(self.controlle_mapping_setting_groupBox)
        self.dev_view_comboBox.setObjectName("dev_view_comboBox")
        self.gridLayout_9.addWidget(self.dev_view_comboBox, 2, 1, 1, 1)
        self.controller_choose_label = QtWidgets.QLabel(self.controlle_mapping_setting_groupBox)
        self.controller_choose_label.setObjectName("controller_choose_label")
        self.gridLayout_9.addWidget(self.controller_choose_label, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.controlle_mapping_setting_groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.page_controller_setting, "")
        self.page_serial_port_debug = QtWidgets.QWidget()
        self.page_serial_port_debug.setObjectName("page_serial_port_debug")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.page_serial_port_debug)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_page_3_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_page_3_3.setObjectName("verticalLayout_page_3_3")
        self.prot_setting_groupBox = QtWidgets.QGroupBox(self.page_serial_port_debug)
        self.prot_setting_groupBox.setObjectName("prot_setting_groupBox")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.prot_setting_groupBox)
        self.gridLayout_12.setObjectName("gridLayout_12")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem4, 4, 0, 1, 1)
        self.gridLayout_page_3_3_1 = QtWidgets.QGridLayout()
        self.gridLayout_page_3_3_1.setObjectName("gridLayout_page_3_3_1")
        self.label_baud_rate = QtWidgets.QLabel(self.prot_setting_groupBox)
        self.label_baud_rate.setObjectName("label_baud_rate")
        self.gridLayout_page_3_3_1.addWidget(self.label_baud_rate, 1, 0, 1, 1)

        #port_comboBox
        self.port_comboBox = QtWidgets.QComboBox(self.prot_setting_groupBox)
        self.port_comboBox.setObjectName("port_comboBox")
        self.gridLayout_page_3_3_1.addWidget(self.port_comboBox, 0, 1, 1, 1)
        self.port_comboBox.activated.connect(self.serial_port_shut_down_action)
        self.port_comboBox.activated[str].connect(self.serial_port_select)

        #byte_size_comboBox
        self.byte_size_comboBox = QtWidgets.QComboBox(self.prot_setting_groupBox)
        self.byte_size_comboBox.setObjectName("byte_size_comboBox")
        self.gridLayout_page_3_3_1.addWidget(self.byte_size_comboBox, 2, 1, 1, 1)
        self.byte_size_comboBox.addItem('5')
        self.byte_size_comboBox.addItem('6')
        self.byte_size_comboBox.addItem('7')
        self.byte_size_comboBox.addItem('8')
        self.byte_size_comboBox.setCurrentIndex(3)
        self.byte_size_comboBox.activated[str].connect(self.serial_bytesize_setting)

        self.label_port = QtWidgets.QLabel(self.prot_setting_groupBox)
        self.label_port.setObjectName("label_port")
        self.gridLayout_page_3_3_1.addWidget(self.label_port, 0, 0, 1, 1)

        #checkout_bit_comboBox
        self.checkout_bit_comboBox = QtWidgets.QComboBox(self.prot_setting_groupBox)
        self.checkout_bit_comboBox.setObjectName("checkout_bit_comboBox")
        self.gridLayout_page_3_3_1.addWidget(self.checkout_bit_comboBox, 3, 1, 1, 1)
        self.checkout_bit_comboBox.addItem('None')
        self.checkout_bit_comboBox.addItem('Even')
        self.checkout_bit_comboBox.addItem('Odd')
        self.checkout_bit_comboBox.addItem('Mark')
        self.checkout_bit_comboBox.addItem('Space')
        self.checkout_bit_comboBox.activated[str].connect(self.serial_checkoutbit_setting)

        #stop_bits_comboBox
        self.stop_bits_comboBox = QtWidgets.QComboBox(self.prot_setting_groupBox)
        self.stop_bits_comboBox.setObjectName("stop_bits_comboBox")
        self.gridLayout_page_3_3_1.addWidget(self.stop_bits_comboBox, 4, 1, 1, 1)
        self.stop_bits_comboBox.addItem('1')
        self.stop_bits_comboBox.addItem('1.5')
        self.stop_bits_comboBox.addItem('2')
        self.stop_bits_comboBox.activated[str].connect(self.serial_stopbits_setting)

        #baud_rate_combobox
        self.baud_rate_comboBox = QtWidgets.QComboBox(self.prot_setting_groupBox)
        self.baud_rate_comboBox.setObjectName("baud_rate_comboBox")
        self.baud_rate_comboBox.addItem('9600')
        self.baud_rate_comboBox.addItem('19200')
        self.baud_rate_comboBox.addItem('38400')
        self.baud_rate_comboBox.addItem('115200')
        self.baud_rate_comboBox.addItem('Custom')
        self.baud_rate_comboBox.activated[str].connect(self.serial_baudrate_setting)
        self.baud_rate_comboBox.editTextChanged[str].connect(self.serial_baudrate_setting)
        self.gridLayout_page_3_3_1.addWidget(self.baud_rate_comboBox, 1, 1, 1, 1)

        #flow_control_comboBox
        self.flow_control_comboBox = QtWidgets.QComboBox(self.prot_setting_groupBox)
        self.flow_control_comboBox.setObjectName("flow_control_comboBox")
        self.gridLayout_page_3_3_1.addWidget(self.flow_control_comboBox, 5, 1, 1, 1)
        self.flow_control_comboBox.addItem('None')
        self.flow_control_comboBox.addItem(r'RTS/CTS')
        self.flow_control_comboBox.addItem(r'XON/XOFF')
        self.flow_control_comboBox.activated[str].connect(self.serial_flowcontrol_setting)

        self.label_byte_size = QtWidgets.QLabel(self.prot_setting_groupBox)
        self.label_byte_size.setObjectName("label_byte_size")
        self.gridLayout_page_3_3_1.addWidget(self.label_byte_size, 2, 0, 1, 1)
        self.label_checkout_bit = QtWidgets.QLabel(self.prot_setting_groupBox)
        self.label_checkout_bit.setObjectName("label_checkout_bit")
        self.gridLayout_page_3_3_1.addWidget(self.label_checkout_bit, 3, 0, 1, 1)
        self.label_stop_bits = QtWidgets.QLabel(self.prot_setting_groupBox)
        self.label_stop_bits.setObjectName("label_stop_bits")
        self.gridLayout_page_3_3_1.addWidget(self.label_stop_bits, 4, 0, 1, 1)
        self.label_flow_control = QtWidgets.QLabel(self.prot_setting_groupBox)
        self.label_flow_control.setObjectName("label_flow_control")
        self.gridLayout_page_3_3_1.addWidget(self.label_flow_control, 5, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_page_3_3_1, 1, 0, 1, 1)

        #scan_port_button
        self.scan_port_pushButton = QtWidgets.QPushButton(self.prot_setting_groupBox)
        self.scan_port_pushButton.setObjectName("scan_port_pushButton")
        self.scan_port_pushButton.clicked.connect(self.serial_scanport_buttonEvent)
        self.gridLayout_12.addWidget(self.scan_port_pushButton, 0, 0, 1, 1)

        self.verticalLayout_page_3_3.addWidget(self.prot_setting_groupBox)
        self.recieve_setting_groupBox = QtWidgets.QGroupBox(self.page_serial_port_debug)
        self.recieve_setting_groupBox.setObjectName("recieve_setting_groupBox")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.recieve_setting_groupBox)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.horizontalLayout_page_3_3_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_page_3_3_2.setObjectName("horizontalLayout_page_3_3_2")

        #radioButton_recieve_ascii
        self.radioButton_recieve_ascii = QtWidgets.QRadioButton(self.recieve_setting_groupBox)
        self.radioButton_recieve_ascii.setObjectName("radioButton_recieve_ascii")
        self.horizontalLayout_page_3_3_2.addWidget(self.radioButton_recieve_ascii)
        self.radioButton_recieve_ascii.toggled[bool].connect(self.serial_recieve_ascii_setting)
        self.radioButton_recieve_ascii.setChecked(True)

        #radioButton_recieve_hex
        self.radioButton_recieve_hex = QtWidgets.QRadioButton(self.recieve_setting_groupBox)
        self.radioButton_recieve_hex.setObjectName("radioButton_recieve_hex")
        self.horizontalLayout_page_3_3_2.addWidget(self.radioButton_recieve_hex)
        self.radioButton_recieve_hex.toggled[bool].connect(self.serial_recieve_hex_setting)
        self.gridLayout_14.addLayout(self.horizontalLayout_page_3_3_2, 0, 0, 1, 1)
        self.verticalLayout_page_3_3_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_page_3_3_3.setObjectName("verticalLayout_page_3_3_3")

        #checkbox_auto_line_feed
        self.checkBox_auto_line_feed = QtWidgets.QCheckBox(self.recieve_setting_groupBox)
        self.checkBox_auto_line_feed.setObjectName("checkBox_auto_line_feed")
        self.verticalLayout_page_3_3_3.addWidget(self.checkBox_auto_line_feed)
        self.checkBox_auto_line_feed.toggled[bool].connect(self.serial_auto_line_feed_setting)
        self.checkBox_auto_line_feed.setChecked(True)


        #checkbox_show_recieve_data
        self.checkBox_show_recieve_data = QtWidgets.QCheckBox(self.recieve_setting_groupBox)
        self.checkBox_show_recieve_data.setObjectName("checkBox_show_recieve_data")
        self.verticalLayout_page_3_3_3.addWidget(self.checkBox_show_recieve_data)
        self.checkBox_show_recieve_data.toggled[bool].connect(self.serial_show_recieve_data_setting)

        #checkbox_show_the_time
        self.checkBox_show_the_time = QtWidgets.QCheckBox(self.recieve_setting_groupBox)
        self.checkBox_show_the_time.setObjectName("checkBox_show_the_time")
        self.verticalLayout_page_3_3_3.addWidget(self.checkBox_show_the_time)
        self.checkBox_show_the_time.toggled[bool].connect(self.serial_show_the_time_setting)

        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_page_3_3_3.addItem(spacerItem5)
        self.gridLayout_14.addLayout(self.verticalLayout_page_3_3_3, 1, 0, 1, 1)
        self.verticalLayout_page_3_3.addWidget(self.recieve_setting_groupBox)
        self.send_setting_groupBox = QtWidgets.QGroupBox(self.page_serial_port_debug)
        self.send_setting_groupBox.setObjectName("send_setting_groupBox")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.send_setting_groupBox)
        self.gridLayout_15.setObjectName("gridLayout_15")

        #spinBox_repeat_par
        self.spinBox_repeat_par = QtWidgets.QSpinBox(self.send_setting_groupBox)
        self.spinBox_repeat_par.setObjectName("spinBox_repeat_par")
        self.gridLayout_15.addWidget(self.spinBox_repeat_par, 1, 1, 1, 1)
        self.spinBox_repeat_par.setSingleStep(100)
        self.spinBox_repeat_par.setMaximum(1000000) # maximum of 1000 second
        self.spinBox_repeat_par.valueChanged[int].connect(self.serial_repeat_send_parameter_setting)
        self.spinBox_repeat_par.setValue(1000)

        #checkBox_repeat_send
        self.checkBox_repeat_send = QtWidgets.QCheckBox(self.send_setting_groupBox)
        self.checkBox_repeat_send.setObjectName("checkBox_repeat_send")
        self.gridLayout_15.addWidget(self.checkBox_repeat_send, 1, 0, 1, 1)
        self.checkBox_repeat_send.toggled[bool].connect(self.serial_repeat_send_setting)

        #radioButton_send_ascii
        self.radioButton_send_ascii = QtWidgets.QRadioButton(self.send_setting_groupBox)
        self.radioButton_send_ascii.setObjectName("radioButton_send_ascii")
        self.gridLayout_15.addWidget(self.radioButton_send_ascii, 0, 0, 1, 1)
        self.radioButton_send_ascii.setChecked(True)  # will connect toggled
        self.radioButton_send_ascii.toggled[bool].connect(self.serial_send_ascii_setting)

        #radioButton_send_hex
        self.radioButton_send_hex = QtWidgets.QRadioButton(self.send_setting_groupBox)
        self.radioButton_send_hex.setObjectName("radioButton_send_hex")
        self.gridLayout_15.addWidget(self.radioButton_send_hex, 0, 1, 1, 1)
        self.radioButton_send_hex.toggled[bool].connect(self.serial_send_hex_setting)

        self.label_unit_ms = QtWidgets.QLabel(self.send_setting_groupBox)
        self.label_unit_ms.setObjectName("label_unit_ms")
        self.gridLayout_15.addWidget(self.label_unit_ms, 1, 2, 1, 1)
        self.verticalLayout_page_3_3.addWidget(self.send_setting_groupBox)
        self.gridLayout_11.addLayout(self.verticalLayout_page_3_3, 0, 1, 4, 2)
        self.gridLayout_page_3_1 = QtWidgets.QGridLayout()
        self.gridLayout_page_3_1.setObjectName("gridLayout_page_3_1")
        self.text_recieve_textBrowser = QtWidgets.QTextBrowser(self.page_serial_port_debug)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_recieve_textBrowser.sizePolicy().hasHeightForWidth())
        self.text_recieve_textBrowser.setSizePolicy(sizePolicy)
        self.text_recieve_textBrowser.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.text_recieve_textBrowser.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.text_recieve_textBrowser.setObjectName("text_recieve_textBrowser")
        self.gridLayout_page_3_1.addWidget(self.text_recieve_textBrowser, 0, 0, 1, 1)
        self.verticalLayout_page_3_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_page_3_2.setContentsMargins(-1, 6, -1, 0)
        self.verticalLayout_page_3_2.setSpacing(6)
        self.verticalLayout_page_3_2.setObjectName("verticalLayout_page_3_2")
        self.horizontalLayout_page_3_2_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_page_3_2_1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_page_3_2_1.setObjectName("horizontalLayout_page_3_2_1")

        #text_send_textEdit
        self.text_send_textEdit = QtWidgets.QTextEdit(self.page_serial_port_debug)
        self.text_send_textEdit.setObjectName("text_send_textEdit")
        self.horizontalLayout_page_3_2_1.addWidget(self.text_send_textEdit)

        #text_send_pushButton
        self.text_send_pushButton = QtWidgets.QPushButton(self.page_serial_port_debug)
        self.text_send_pushButton.setObjectName("text_send_pushButton")
        self.horizontalLayout_page_3_2_1.addWidget(self.text_send_pushButton)
        self.text_send_pushButton.clicked.connect(self.serial_text_send_action)

        self.verticalLayout_page_3_2.addLayout(self.horizontalLayout_page_3_2_1)
        self.horizontalLayout_page_3_2_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_page_3_2_2.setObjectName("horizontalLayout_page_3_2_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_page_3_2_2.addItem(spacerItem6)

        #start_pushButton
        self.start_pushButton = QtWidgets.QPushButton(self.page_serial_port_debug)
        self.start_pushButton.setObjectName("start_pushButton")
        self.horizontalLayout_page_3_2_2.addWidget(self.start_pushButton)
        self.start_pushButton.clicked.connect(self.serial_port_open_action)

        #pause_pushButton
        self.pause_pushButton = QtWidgets.QPushButton(self.page_serial_port_debug)
        self.pause_pushButton.setObjectName("pause_pushButton")
        self.horizontalLayout_page_3_2_2.addWidget(self.pause_pushButton)
        self.pause_pushButton.clicked.connect(self.serial_recieve_stop_action)

        #stop_pushButton
        self.stop_pushButton = QtWidgets.QPushButton(self.page_serial_port_debug)
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.horizontalLayout_page_3_2_2.addWidget(self.stop_pushButton)
        self.stop_pushButton.clicked.connect(self.serial_port_shut_down_action)

        #clean_pushButton
        self.clean_pushButton = QtWidgets.QPushButton(self.page_serial_port_debug)
        self.clean_pushButton.setObjectName("clean_pushButton")
        self.horizontalLayout_page_3_2_2.addWidget(self.clean_pushButton)
        self.clean_pushButton.clicked.connect(self.serial_clean_browser_action)

        #save_log_pushButton
        self.save_log_pushButton = QtWidgets.QPushButton(self.page_serial_port_debug)
        self.save_log_pushButton.setObjectName("save_log_pushButton")
        self.horizontalLayout_page_3_2_2.addWidget(self.save_log_pushButton)
        self.clean_pushButton.clicked.connect(self.serial_save_log_action)

        self.verticalLayout_page_3_2.addLayout(self.horizontalLayout_page_3_2_2)
        self.gridLayout_page_3_1.addLayout(self.verticalLayout_page_3_2, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_page_3_1, 0, 4, 4, 1)
        self.tabWidget.addTab(self.page_serial_port_debug, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        BBUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BBUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 17))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        BBUI.setMenuBar(self.menubar)

        #statusBar
        self.statusbar = QtWidgets.QStatusBar(BBUI)
        self.statusbar.setObjectName("statusbar")
        BBUI.setStatusBar(self.statusbar)
        self.statusbar.showMessage('Ready')

        self.actionLoading_Setting_File = QtWidgets.QAction(BBUI)
        self.actionLoading_Setting_File.setObjectName("actionLoading_Setting_File")
        self.actionSaving_Setting_File = QtWidgets.QAction(BBUI)
        self.actionSaving_Setting_File.setObjectName("actionSaving_Setting_File")
        self.actionExit = QtWidgets.QAction(BBUI)
        self.actionExit.setObjectName("actionExit")
        self.actionBBfilght = QtWidgets.QAction(BBUI)
        self.actionBBfilght.setObjectName("actionBBfilght")
        self.menuFile.addAction(self.actionLoading_Setting_File)
        self.menuFile.addAction(self.actionSaving_Setting_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionBBfilght)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(BBUI)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(BBUI)

    def serial_scanport_buttonEvent(self):
        self.port_comboBox.clear()
        serial_portlist = bbapi.serialScanPort()
        for i in range(len(serial_portlist)):
            self.port_comboBox.addItem(serial_portlist[i])

    def serial_port_select(self, port_name):
        bbapi.serialPortSelect(global_variable.BBSerial, port_name)

    def serial_bytesize_setting(self, bytesize):
        bbapi.serialByteSizeSetting(global_variable.BBSerial, bytesize)

    def serial_baudrate_setting(self, baudrate):
        import re
        if baudrate == 'Custom':
            self.baud_rate_comboBox.setEditable(True)
        elif re.match(r'^[1-9]\d*$', baudrate):
            bbapi.serialBaudRateSetting(global_variable.BBSerial, baudrate)

    def serial_checkoutbit_setting(self, checkoutbit):
        bbapi.serialPortSelect(global_variable.BBSerial, checkoutbit)

    def serial_flowcontrol_setting(self, flowcontrol):
        bbapi.serialFlowControlSetting(global_variable.BBSerial, flowcontrol)

    def serial_stopbits_setting(self, stopbits):
        bbapi.serialStopBitsSetting(global_variable.BBSerial, stopbits)

    def serial_recieve_ascii_setting(self, toggledbool):
        if toggledbool == True:
            global_variable.BBSerialRecieve.setRecieveMode('ASCII')

    def serial_recieve_hex_setting(self, toggledbool):
        if toggledbool == True:
            global_variable.BBSerialRecieve.setRecieveMode('Hex')

    def serial_send_ascii_setting(self, toggledbool):
        if toggledbool == True:
            global_variable.BBSerialSend.setSendMode('ASCII')
        self.text_send_textEdit.setText(r'Type the words <b>directly!</b>')
        self.text_send_textEdit.selectAll()

    def serial_send_hex_setting(self, toggledbool):
        if toggledbool == True:
            global_variable.BBSerialSend.setSendMode('Hex')
        self.text_send_textEdit.setText(r'Type the words with decimal ascii code like: <b>656667 -> ABC</b>')
        self.text_send_textEdit.selectAll()

    def serial_auto_line_feed_setting(self, toggledbool):
        global_variable.BBSerialRecieve.setAutoNewLine(toggledbool)

    def serial_show_recieve_data_setting(self, toggledbool):
        global_variable.BBSerialRecieve.setShowSend(toggledbool)

    def serial_show_the_time_setting(self, toggledbool):
        global_variable.BBSerialRecieve.setShowTheTime(toggledbool)

    def serial_repeat_send_setting(self, toggledbool):
        global_variable.BBSerialSend.setRepeatSend(toggledbool)
        bbapi.serialRepeatSend(toggledbool)

    def serial_repeat_send_parameter_setting(self, timepar):
        global_variable.BBSerialSend.setRepeatSendTime(timepar)

    def serial_text_send_action(self):
        tarstring = self.text_send_textEdit.toPlainText()
        if global_variable.BBSerialSend.sendData(global_variable.BBSerial, tarstring) == True:
            self.statusbar.showMessage('%s OPENED, %d >>   Rx: %d Bytes Tx: %d Bytes ' %
                                       (global_variable.BBSerial.name, global_variable.BBSerial.baudrate,
                                        global_variable.BBSerialRecieve.rxByteCount, global_variable.BBSerialSend.txByteCount))
        else:
            self.statusbar.showMessage('Send Fail!!!')

    def serial_port_open_action(self):
        partem = bbapi.serialPortOpen(global_variable.BBSerial, global_variable.BBSerialSend, global_variable.BBSerialRecieve)
        if partem == True:
            self.statusbar.showMessage('%s Open Success!' % global_variable.BBSerial.name)
            global_variable.BBSerialRecieve.recieveThreading(global_variable.BBSerial, True, 0.01)
            ui.serialRecieveTextBrowerUpdataThreading(global_variable.BBSerialRecieve, True, 0.01)

        elif partem == False:
            self.statusbar.showMessage('%s Open Fail!' % global_variable.BBSerial.name)
        elif partem == 'DataRecieveContinue':
            self.statusbar.showMessage('%s Recieving Open!' % global_variable.BBSerial.name)
            global_variable.BBSerialRecieve.recieveThreading(global_variable.BBSerial, True, 0.01)


    def serialRecieveTextBrowerUpdataThreading(self, serialrecieveclass, openorstop, refreshtime):
        if openorstop == True:
            self._recieveTextBrowserUpdate = True
            self.rtbThreading = threading.Thread(target=self.serialRecieveTextBrowserUpdate, args=(serialrecieveclass, refreshtime))
            self.rtbThreading.setDaemon(True)
            self.rtbThreading.start()
        elif openorstop == False:
            self._recieveTextBrowserUpdate = False
            self.rtbThreading.join()

    def serialRecieveTextBrowserUpdate(self, serialrecieveclass, refreshtime):
        while self._recieveTextBrowserUpdate == True:
            time.sleep(refreshtime)
            strtemp = serialrecieveclass.readBuffer()
            serialrecieveclass.writeBuffer('')

            if strtemp != '':
                self.text_recieve_textBrowser.append(strtemp)


    def serial_recieve_stop_action(self):
        global_variable.BBSerialRecieve.setRecieveSwitch(False)
        self.statusbar.showMessage('%s Recieving Stop!' % global_variable.BBSerial.name)

    def serial_port_shut_down_action(self):
        bbapi.serialPortShutDown(global_variable.BBSerial, global_variable.BBSerialSend, global_variable.BBSerialRecieve)
        if global_variable.BBSerial.name != None:
            self.statusbar.showMessage('%s CLOSED!!!' % global_variable.BBSerial.name)

    def serial_clean_browser_action(self):
        pass

    def serial_save_log_action(self):
        pass























































    def retranslateUi(self, BBUI):
        _translate = QtCore.QCoreApplication.translate
        self.connect_button.setText(_translate("BBUI", "Connect"))
        self.address_setting_button.setText(_translate("BBUI", "Address Setting"))
        self.link_quality_label.setText(_translate("BBUI", "Link quality:"))
        self.battery_label.setText(_translate("BBUI", "Battery:"))
        self.expansion_function_groupbox.setTitle(_translate("BBUI", "Expansion Function"))
        self.led_mode_label.setText(_translate("BBUI", "LED mode"))
        self.expansion_function_groupbox_checkBox_2.setText(_translate("BBUI", "Resevered"))
        self.basic_control_groupbox.setTitle(_translate("BBUI", "Basic Control"))
        self.flight_mode_label.setText(_translate("BBUI", "Flight mode"))
        self.basic_control_groupbox_checkBox_1.setText(_translate("BBUI", "Resevered"))
        self.basic_control_groupbox_radioButton_3.setText(_translate("BBUI", "Resevered"))
        self.basic_control_groupbox_radioButton_2.setText(_translate("BBUI", "Resevered"))
        self.basic_control_groupbox_radioButton_1.setText(_translate("BBUI", "Resevered"))
        self.roll_trim_label.setText(_translate("BBUI", "Roll Trim"))
        self.pitch_trim_label.setText(_translate("BBUI", "Pitch Trim"))
        self.thrust_mode_label.setText(_translate("BBUI", "Thrust mode"))
        self.adcanced_flight_control_groupBox.setTitle(_translate("BBUI", "Advanced Flight Control"))
        self.max_angle_rate_label.setText(_translate("BBUI", "Max angle(/rate)"))
        self.max_yaw_angle_rate_label.setText(_translate("BBUI", "Max Yaw angle(/rate)"))
        self.max_thrust_label_2.setText(_translate("BBUI", "Max thrust(%)"))
        self.min_thrust_label.setText(_translate("BBUI", "Min thrust(%)"))
        self.slewlimit_label.setText(_translate("BBUI", "SlewLimit(%)"))
        self.thrust_lowering_slewrate_label.setText(_translate("BBUI", "<p style = \"line-height:1.0\"><html><head/><body><p>Thrust lowering </p><p>slewrate(%/sec)</p></body></html>"))
        self.filght_status_groupbox.setTitle(_translate("BBUI", "Filght Status"))
        self.thrust_label.setText(_translate("BBUI", "Thrust"))
        self.resevered_label_1.setText(_translate("BBUI", "Resevered"))
        self.yaw_label.setText(_translate("BBUI", "Yaw"))
        self.roll_label.setText(_translate("BBUI", "Roll"))
        self.pitch_label.setText(_translate("BBUI", "Pitch"))
        self.target_label.setText(_translate("BBUI", "Target"))
        self.actual_label.setText(_translate("BBUI", "Actual"))
        self.Thr_label.setText(_translate("BBUI", "Thr"))
        self.M1_label.setText(_translate("BBUI", "M1"))
        self.M2_label.setText(_translate("BBUI", "M2"))
        self.M3_label.setText(_translate("BBUI", "M3"))
        self.M4_label.setText(_translate("BBUI", "M4"))
        self.flight_angle_pic_label.setText(_translate("BBUI", "<html><head/><body><p><img src=\":/mainwindow_pic/BB.bmp\"/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.page_flight_control), _translate("BBUI", "Flight Control"))
        self.controlle_mapping_setting_groupBox.setTitle(_translate("BBUI", "Controller Mapping Setting"))
        self.mapping_view_pic_label.setText(_translate("BBUI", "<html><head/><body><p><img src=\":/mainwindow_pic/BB.bmp\"/></p></body></html>"))
        self.dev_scan_pushButton.setText(_translate("BBUI", "Scan"))
        self.controller_choose_label.setText(_translate("BBUI", "Controller Choose"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.page_controller_setting), _translate("BBUI", "Controller Setting"))
        self.prot_setting_groupBox.setTitle(_translate("BBUI", "Port Setting"))
        self.label_baud_rate.setText(_translate("BBUI", "Baud Rate"))
        self.label_port.setText(_translate("BBUI", "Port"))
        self.label_byte_size.setText(_translate("BBUI", "Byte Size"))
        self.label_checkout_bit.setText(_translate("BBUI", "Checkout Bit"))
        self.label_stop_bits.setText(_translate("BBUI", "Stop Bits"))
        self.label_flow_control.setText(_translate("BBUI", "Flow Control"))
        self.scan_port_pushButton.setText(_translate("BBUI", "Scan Port"))
        self.recieve_setting_groupBox.setTitle(_translate("BBUI", "Recieve Setting"))
        self.radioButton_recieve_ascii.setText(_translate("BBUI", "ASCII"))
        self.radioButton_recieve_hex.setText(_translate("BBUI", "Hex"))
        self.checkBox_auto_line_feed.setText(_translate("BBUI", "Auto Line Feed"))
        self.checkBox_show_recieve_data.setText(_translate("BBUI", "Show What We Send"))
        self.checkBox_show_the_time.setText(_translate("BBUI", "Show The Time"))
        self.send_setting_groupBox.setTitle(_translate("BBUI", "Send Setting"))
        self.checkBox_repeat_send.setText(_translate("BBUI", "Repeat"))
        self.radioButton_send_ascii.setText(_translate("BBUI", "ASCII"))
        self.radioButton_send_hex.setText(_translate("BBUI", "Hex"))
        self.label_unit_ms.setText(_translate("BBUI", "ms"))
        self.text_send_pushButton.setText(_translate("BBUI", "Send"))
        self.start_pushButton.setText(_translate("BBUI", "Start"))
        self.pause_pushButton.setText(_translate("BBUI", "Pause"))
        self.stop_pushButton.setText(_translate("BBUI", "Stop"))
        self.clean_pushButton.setText(_translate("BBUI", "Clean"))
        self.save_log_pushButton.setText(_translate("BBUI", "Save Log"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.page_serial_port_debug), _translate("BBUI", "Serial Port Debug"))
        self.menuFile.setTitle(_translate("BBUI", "File"))
        self.menuAbout.setTitle(_translate("BBUI", "About"))
        self.actionLoading_Setting_File.setText(_translate("BBUI", "Loading Setting File"))
        self.actionSaving_Setting_File.setText(_translate("BBUI", "Saving Setting File"))
        self.actionExit.setText(_translate("BBUI", "Exit"))
        self.actionBBfilght.setText(_translate("BBUI", "BBfilght"))

#import ui_rc




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BBUI = QtWidgets.QMainWindow()
    ui = Ui_BBUI()
    ui.setupUi(BBUI)
    BBUI.show()


    sys.exit(app.exec_())

