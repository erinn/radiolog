# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\changeCallsignDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_changeCallsignDialog(object):
    def setupUi(self, changeCallsignDialog):
        changeCallsignDialog.setObjectName("changeCallsignDialog")
        changeCallsignDialog.resize(542, 290)
        font = QtGui.QFont()
        font.setPointSize(8)
        changeCallsignDialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(changeCallsignDialog)
        self.buttonBox.setGeometry(QtCore.QRect(248, 225, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.fleetField = QtWidgets.QLineEdit(changeCallsignDialog)
        self.fleetField.setEnabled(False)
        self.fleetField.setGeometry(QtCore.QRect(210, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.fleetField.setFont(font)
        self.fleetField.setReadOnly(True)
        self.fleetField.setObjectName("fleetField")
        self.deviceField = QtWidgets.QLineEdit(changeCallsignDialog)
        self.deviceField.setEnabled(False)
        self.deviceField.setGeometry(QtCore.QRect(390, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.deviceField.setFont(font)
        self.deviceField.setReadOnly(True)
        self.deviceField.setObjectName("deviceField")
        self.currentCallsignField = QtWidgets.QLineEdit(changeCallsignDialog)
        self.currentCallsignField.setEnabled(False)
        self.currentCallsignField.setGeometry(QtCore.QRect(210, 100, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.currentCallsignField.setFont(font)
        self.currentCallsignField.setObjectName("currentCallsignField")
        self.newCallsignField = QtWidgets.QLineEdit(changeCallsignDialog)
        self.newCallsignField.setGeometry(QtCore.QRect(210, 170, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.newCallsignField.setFont(font)
        self.newCallsignField.setText("")
        self.newCallsignField.setPlaceholderText("")
        self.newCallsignField.setClearButtonEnabled(False)
        self.newCallsignField.setObjectName("newCallsignField")
        self.label = QtWidgets.QLabel(changeCallsignDialog)
        self.label.setGeometry(QtCore.QRect(220, 60, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(changeCallsignDialog)
        self.label_2.setGeometry(QtCore.QRect(400, 60, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(changeCallsignDialog)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(changeCallsignDialog)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(changeCallsignDialog)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.fsFilterButton = QtWidgets.QToolButton(changeCallsignDialog)
        self.fsFilterButton.setGeometry(QtCore.QRect(476, 227, 47, 46))
        self.fsFilterButton.setText("...")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/radiolog_ui/icons/empty_filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fsFilterButton.setIcon(icon)
        self.fsFilterButton.setIconSize(QtCore.QSize(40, 40))
        self.fsFilterButton.setObjectName("fsFilterButton")

        self.retranslateUi(changeCallsignDialog)
        self.buttonBox.accepted.connect(changeCallsignDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(changeCallsignDialog.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(changeCallsignDialog)

    def retranslateUi(self, changeCallsignDialog):
        _translate = QtCore.QCoreApplication.translate
        changeCallsignDialog.setWindowTitle(_translate("changeCallsignDialog", "Change Callsign"))
        self.label.setText(_translate("changeCallsignDialog", "Fleet"))
        self.label_2.setText(_translate("changeCallsignDialog", "Device"))
        self.label_3.setText(_translate("changeCallsignDialog", "Current Callsign"))
        self.label_4.setText(_translate("changeCallsignDialog", "New Callsign"))
        self.label_5.setText(_translate("changeCallsignDialog", "FleetSync ID"))
import radiolog_ui_rc
