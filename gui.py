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
        self.surface_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.surface_btn.setObjectName("surface_btn")
        self.surface_btn.setEnabled(False)
        self.horizontalLayout.addWidget(self.surface_btn)
        self.browse_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.browse_btn.setObjectName("browse_btn")
        self.horizontalLayout.addWidget(self.browse_btn)
        self.ray_casting_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.ray_casting_btn.setObjectName("ray_casting_btn")
        self.ray_casting_btn.setEnabled(False)
        self.horizontalLayout.addWidget(self.ray_casting_btn)
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
        self.surface_viewer = QtWidgets.QFrame(self.centralwidget)
        self.surface_viewer.setGeometry(QtCore.QRect(30, 50, 401, 401))
        self.surface_viewer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.surface_viewer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.surface_viewer.setObjectName("surface_viewer")
        self.ray_casting_viewer = QtWidgets.QFrame(self.centralwidget)
        self.ray_casting_viewer.setGeometry(QtCore.QRect(480, 50, 411, 401))
        self.ray_casting_viewer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ray_casting_viewer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ray_casting_viewer.setObjectName("ray_casting_viewer")
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
        self.surface_btn.setText(_translate("MainWindow", "Surface Rendering"))
        self.browse_btn.setText(_translate("MainWindow", "Load Images"))
        self.ray_casting_btn.setText(_translate("MainWindow", "Ray Casting Rendering"))
        self.range.setText(_translate("MainWindow", "range"))

