# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_01.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 539)
        MainWindow.setMinimumSize(QtCore.QSize(740, 0))
        MainWindow.setMaximumSize(QtCore.QSize(740, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 30, 371, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.verticalLayoutWidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 290, 141, 71))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_h = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_h.setObjectName("label_h")
        self.verticalLayout_2.addWidget(self.label_h)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(550, 290, 141, 71))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_o = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_o.setObjectName("label_o")
        self.verticalLayout_3.addWidget(self.label_o)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 370, 91, 31))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.h_head = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.h_head.setObjectName("h_head")
        self.verticalLayout_4.addWidget(self.h_head)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(130, 370, 91, 31))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.h_t = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.h_t.setObjectName("h_t")
        self.verticalLayout_5.addWidget(self.h_t)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(20, 420, 91, 31))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.h_abd = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.h_abd.setObjectName("h_abd")
        self.verticalLayout_6.addWidget(self.h_abd)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(130, 420, 91, 31))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.h_abd_cut = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.h_abd_cut.setObjectName("h_abd_cut")
        self.verticalLayout_7.addWidget(self.h_abd_cut)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(20, 470, 91, 31))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.h_pelvis = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.h_pelvis.setObjectName("h_pelvis")
        self.verticalLayout_8.addWidget(self.h_pelvis)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(620, 370, 91, 31))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.o_t = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.o_t.setObjectName("o_t")
        self.verticalLayout_9.addWidget(self.o_t)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(620, 420, 91, 31))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.o_abd_cut = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.o_abd_cut.setObjectName("o_abd_cut")
        self.verticalLayout_10.addWidget(self.o_abd_cut)
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(510, 370, 91, 31))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.o_head = QtWidgets.QPushButton(self.verticalLayoutWidget_11)
        self.o_head.setObjectName("o_head")
        self.verticalLayout_11.addWidget(self.o_head)
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(620, 470, 91, 31))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.o_pelvis = QtWidgets.QPushButton(self.verticalLayoutWidget_12)
        self.o_pelvis.setObjectName("o_pelvis")
        self.verticalLayout_12.addWidget(self.o_pelvis)
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(510, 420, 91, 31))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.o_abd = QtWidgets.QPushButton(self.verticalLayoutWidget_13)
        self.o_abd.setObjectName("o_abd")
        self.verticalLayout_13.addWidget(self.o_abd)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(240, 290, 256, 192))
        self.listView.setObjectName("listView")
        self.verticalLayoutWidget_14 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(310, 490, 111, 25))
        self.verticalLayoutWidget_14.setObjectName("verticalLayoutWidget_14")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_14)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.outputButton = QtWidgets.QPushButton(self.verticalLayoutWidget_14)
        self.outputButton.setObjectName("outputButton")
        self.verticalLayout_14.addWidget(self.outputButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 270, 101, 20))
        self.label.setObjectName("label")
        self.verticalLayoutWidget_15 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_15.setGeometry(QtCore.QRect(130, 470, 91, 31))
        self.verticalLayoutWidget_15.setObjectName("verticalLayoutWidget_15")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_15)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.h_v = QtWidgets.QPushButton(self.verticalLayoutWidget_15)
        self.h_v.setObjectName("h_v")
        self.verticalLayout_15.addWidget(self.h_v)
        self.verticalLayoutWidget_16 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_16.setGeometry(QtCore.QRect(510, 470, 91, 31))
        self.verticalLayoutWidget_16.setObjectName("verticalLayoutWidget_16")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_16)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.o_v = QtWidgets.QPushButton(self.verticalLayoutWidget_16)
        self.o_v.setObjectName("o_v")
        self.verticalLayout_16.addWidget(self.o_v)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_h.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">健保</span></p></body></html>"))
        self.label_o.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">自費</span></p></body></html>"))
        self.h_head.setText(_translate("MainWindow", "三點頭長"))
        self.h_t.setText(_translate("MainWindow", "四點T"))
        self.h_abd.setText(_translate("MainWindow", "四點腹"))
        self.h_abd_cut.setText(_translate("MainWindow", "四腹裁"))
        self.h_pelvis.setText(_translate("MainWindow", "六點骨盆"))
        self.o_t.setText(_translate("MainWindow", "四點T"))
        self.o_abd_cut.setText(_translate("MainWindow", "四腹裁"))
        self.o_head.setText(_translate("MainWindow", "三點頭長"))
        self.o_pelvis.setText(_translate("MainWindow", "六點骨盆"))
        self.o_abd.setText(_translate("MainWindow", "四點腹"))
        self.outputButton.setText(_translate("MainWindow", "輸出"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">事件紀錄</span></p></body></html>"))
        self.h_v.setText(_translate("MainWindow", "V"))
        self.o_v.setText(_translate("MainWindow", "V"))
