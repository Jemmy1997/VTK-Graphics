# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(921, 824)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 610, 641, 99))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.browse = QtWidgets.QPushButton(self.layoutWidget)
        self.browse.setObjectName("browse")
        self.horizontalLayout.addWidget(self.browse)
        self.mode_select = QtWidgets.QComboBox(self.layoutWidget)
        self.mode_select.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mode_select.setObjectName("mode_select")
        self.mode_select.addItem("")
        self.mode_select.addItem("")
        self.mode_select.addItem("")
        self.horizontalLayout.addWidget(self.mode_select)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(140, 490, 641, 91))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.iso = QtWidgets.QSlider(self.layoutWidget1)
        self.iso.setMaximum(1000)
        self.iso.setSingleStep(5)
        self.iso.setSliderPosition(500)
        self.iso.setOrientation(QtCore.Qt.Horizontal)
        self.iso.setObjectName("iso")
        self.horizontalLayout_2.addWidget(self.iso)
        self.range = QtWidgets.QLabel(self.layoutWidget1)
        self.range.setAlignment(QtCore.Qt.AlignCenter)
        self.range.setObjectName("range")
        self.horizontalLayout_2.addWidget(self.range)
        self.frame1_viewer = QtWidgets.QFrame(self.centralwidget)
        self.frame1_viewer.setGeometry(QtCore.QRect(30, 50, 401, 401))
        self.frame1_viewer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1_viewer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1_viewer.setObjectName("frame1_viewer")
        self.frame2_viewer = QtWidgets.QFrame(self.centralwidget)
        self.frame2_viewer.setGeometry(QtCore.QRect(480, 50, 411, 401))
        self.frame2_viewer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2_viewer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2_viewer.setObjectName("frame2_viewer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 921, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browse.setText(_translate("MainWindow", "Load Images"))
        self.mode_select.setItemText(0, _translate("MainWindow", "Choose Mode"))
        self.mode_select.setItemText(1, _translate("MainWindow", "Surface Rendering"))
        self.mode_select.setItemText(2, _translate("MainWindow", "Ray Casting Rendering"))
        self.range.setText(_translate("MainWindow", "range"))

