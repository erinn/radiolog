# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newEntryWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newEntryWidget(object):
    def setupUi(self, newEntryWidget):
        newEntryWidget.setObjectName("newEntryWidget")
        newEntryWidget.resize(952, 481)
        newEntryWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        newEntryWidget.setStyleSheet("")
        self.quickTextButton3 = QtWidgets.QPushButton(newEntryWidget)
        self.quickTextButton3.setGeometry(QtCore.QRect(630, 210, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.quickTextButton3.setFont(font)
        self.quickTextButton3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.quickTextButton3.setObjectName("quickTextButton3")
        self.quickTextButton6 = QtWidgets.QPushButton(newEntryWidget)
        self.quickTextButton6.setGeometry(QtCore.QRect(360, 310, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.quickTextButton6.setFont(font)
        self.quickTextButton6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.quickTextButton6.setCheckable(False)
        self.quickTextButton6.setFlat(False)
        self.quickTextButton6.setObjectName("quickTextButton6")
        self.line_3 = QtWidgets.QFrame(newEntryWidget)
        self.line_3.setGeometry(QtCore.QRect(110, 290, 731, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label = QtWidgets.QLabel(newEntryWidget)
        self.label.setGeometry(QtCore.QRect(0, 140, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.datumFormatLabel = QtWidgets.QLabel(newEntryWidget)
        self.datumFormatLabel.setEnabled(False)
        self.datumFormatLabel.setGeometry(QtCore.QRect(152, 127, 196, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.datumFormatLabel.setFont(font)
        self.datumFormatLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.datumFormatLabel.setObjectName("datumFormatLabel")
        self.quickTextButton9 = QtWidgets.QPushButton(newEntryWidget)
        self.quickTextButton9.setGeometry(QtCore.QRect(20, 360, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.quickTextButton9.setFont(font)
        self.quickTextButton9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.quickTextButton9.setObjectName("quickTextButton9")
        self.statusGroupBox = QtWidgets.QGroupBox(newEntryWidget)
        self.statusGroupBox.setEnabled(True)
        self.statusGroupBox.setGeometry(QtCore.QRect(610, 0, 311, 151))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.statusGroupBox.setFont(font)
        self.statusGroupBox.setCheckable(False)
        self.statusGroupBox.setObjectName("statusGroupBox")
        self.at_icField = QtWidgets.QRadioButton(self.statusGroupBox)
        self.at_icField.setEnabled(True)
        self.at_icField.setGeometry(QtCore.QRect(20, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.at_icField.setFont(font)
        self.at_icField.setFocusPolicy(QtCore.Qt.NoFocus)
        self.at_icField.setObjectName("at_icField")
        self.statusButtonGroup = QtWidgets.QButtonGroup(newEntryWidget)
        self.statusButtonGroup.setObjectName("statusButtonGroup")
        self.statusButtonGroup.addButton(self.at_icField)
        self.in_transitField = QtWidgets.QRadioButton(self.statusGroupBox)
        self.in_transitField.setEnabled(True)
        self.in_transitField.setGeometry(QtCore.QRect(20, 50, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.in_transitField.setFont(font)
        self.in_transitField.setFocusPolicy(QtCore.Qt.NoFocus)
        self.in_transitField.setObjectName("in_transitField")
        self.statusButtonGroup.addButton(self.in_transitField)
        self.workingField = QtWidgets.QRadioButton(self.statusGroupBox)
        self.workingField.setEnabled(True)
        self.workingField.setGeometry(QtCore.QRect(20, 80, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.workingField.setFont(font)
        self.workingField.setFocusPolicy(QtCore.Qt.NoFocus)
        self.workingField.setObjectName("workingField")
        self.statusButtonGroup.addButton(self.workingField)
        self.waitingForTransportField = QtWidgets.QRadioButton(self.statusGroupBox)
        self.waitingForTransportField.setEnabled(True)
        self.waitingForTransportField.setGeometry(QtCore.QRect(20, 110, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.waitingForTransportField.setFont(font)
        self.waitingForTransportField.setFocusPolicy(QtCore.Qt.NoFocus)
        self.waitingForTransportField.setIconSize(QtCore.QSize(20, 20))
        self.waitingForTransportField.setObjectName("waitingForTransportField")
        self.statusButtonGroup.addButton(self.waitingForTransportField)
        self.standbyField = QtWidgets.QRadioButton(self.statusGroupBox)
        self.standbyField.setGeometry(QtCore.QRect(170, 20, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.standbyField.sizePolicy().hasHeightForWidth())
        self.standbyField.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.standbyField.setFont(font)
        self.standbyField.setObjectName("standbyField")
        self.statusButtonGroup.addButton(self.standbyField)
        self.availableField = QtWidgets.QRadioButton(self.statusGroupBox)
        self.availableField.setGeometry(QtCore.QRect(170, 48, 121, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.availableField.sizePolicy().hasHeightForWidth())
        self.availableField.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.availableField.setFont(font)
        self.availableField.setObjectName("availableField")
        self.statusButtonGroup.addButton(self.availableField)
        self.availableField_2 = QtWidgets.QRadioButton(self.statusGroupBox)
        self.availableField_2.setGeometry(QtCore.QRect(170, 80, 150, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.availableField_2.sizePolicy().hasHeightForWidth())
        self.availableField_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.availableField_2.setFont(font)
        self.availableField_2.setObjectName("availableField_2")
        self.statusButtonGroup.addButton(self.availableField_2)
        self.label_5 = QtWidgets.QLabel(newEntryWidget)
        self.label_5.setGeometry(QtCore.QRect(176, 100, 172, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.to_fromField = QtWidgets.QComboBox(newEntryWidget)
        self.to_fromField.setGeometry(QtCore.QRect(13, 8, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.to_fromField.setFont(font)
        self.to_fromField.setObjectName("to_fromField")
        self.to_fromField.addItem("")
        self.to_fromField.addItem("")
        self.quickTextButton2 = QtWidgets.QPushButton(newEntryWidget)
        self.quickTextButton2.setGeometry(QtCore.QRect(350, 210, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.quickTextButton2.setFont(font)
        self.quickTextButton2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.quickTextButton2.setObjectName("quickTextButton2")
        self.quickTextButton1 = QtWidgets.QPushButton(newEntryWidget)
        self.quickTextButton1.setGeometry(QtCore.QRect(70, 210, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.quickTextButton1.setFont(font)
        self.quickTextButton1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.quickTextButton1.setIconSize(QtCore.QSize(32, 32))
        self.quickTextButton1.setObjectName("quickTextButton1")
        self.messageField = QtWidgets.QLineEdit(newEntryWidget)
        self.messageField.setGeometry(QtCore.QRect(110, 160, 821, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.messageField.setFont(font)
        self.messageField.setText("")
        self.messageField.setObjectName("messageField")
        self.quickTextButton5 = QtWidgets.QPushButton(newEntryWidget)
        self.quickTextButton5.setGeometry(QtCore.QRect(100, 310, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.quickTextButton5.setFont(font)
        self.quickTextButton5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.quickTextButton5.setObjectName("quickTextButton5")
        self.quickTextButton11 = QtWidgets.QPushButton(newEntryWidget)
        self.quickTextButton11.setGeometry(QtCore.QRect(640, 360, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.quickTextButton11.setFont(font)
        self.quickTextButton11.setFocusPolicy(QtCore.Qt.NoFocus)
        self.quickTextButton11.setObjectName("quickTextButton11")
        self.buttonBox = QtWidgets.QDialogButtonBox(newEntryWidget)
        self.buttonBox.setGeometry(QtCore.QRect(720, 430, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.quickTextButton4 = QtWidgets.QPushButton(newEntryWidget)
        self.quickTextButton4.setGeometry(QtCore.QRect(630, 260, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.quickTextButton4.setFont(font)
        self.quickTextButton4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.quickTextButton4.setObjectName("quickTextButton4")
        self.line_4 = QtWidgets.QFrame(newEntryWidget)
        self.line_4.setGeometry(QtCore.QRect(150, 340, 651, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_6 = QtWidgets.QLabel(newEntryWidget)
        self.label_6.setGeometry(QtCore.QRect(51, 88, 53, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.quickTextUndoButton = QtWidgets.QPushButton(newEntryWidget)
        self.quickTextUndoButton.setGeometry(QtCore.QRect(30, 430, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.quickTextUndoButton.setFont(font)
        self.quickTextUndoButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.quickTextUndoButton.setCheckable(False)
        self.quickTextUndoButton.setChecked(False)
        self.quickTextUndoButton.setObjectName("quickTextUndoButton")
        self.timeField = QtWidgets.QLineEdit(newEntryWidget)
        self.timeField.setEnabled(False)
        self.timeField.setGeometry(QtCore.QRect(111, 87, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.timeField.setFont(font)
        self.timeField.setFocusPolicy(QtCore.Qt.NoFocus)
        self.timeField.setReadOnly(False)
        self.timeField.setObjectName("timeField")
        self.teamField = QtWidgets.QLineEdit(newEntryWidget)
        self.teamField.setGeometry(QtCore.QRect(175, 8, 394, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.teamField.setFont(font)
        self.teamField.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.teamField.setObjectName("teamField")
        self.quickTextButton7 = QtWidgets.QPushButton(newEntryWidget)
        self.quickTextButton7.setGeometry(QtCore.QRect(350, 260, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.quickTextButton7.setFont(font)
        self.quickTextButton7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.quickTextButton7.setObjectName("quickTextButton7")
        self.quickTextButton8 = QtWidgets.QPushButton(newEntryWidget)
        self.quickTextButton8.setGeometry(QtCore.QRect(650, 310, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.quickTextButton8.setFont(font)
        self.quickTextButton8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.quickTextButton8.setCheckable(False)
        self.quickTextButton8.setChecked(False)
        self.quickTextButton8.setObjectName("quickTextButton8")
        self.label_2 = QtWidgets.QLabel(newEntryWidget)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(220, 70, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.quickTextButton10 = QtWidgets.QPushButton(newEntryWidget)
        self.quickTextButton10.setGeometry(QtCore.QRect(330, 360, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.quickTextButton10.setFont(font)
        self.quickTextButton10.setObjectName("quickTextButton10")
        self.line_5 = QtWidgets.QFrame(newEntryWidget)
        self.line_5.setGeometry(QtCore.QRect(90, 410, 771, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.quickTextButton1_2 = QtWidgets.QPushButton(newEntryWidget)
        self.quickTextButton1_2.setGeometry(QtCore.QRect(70, 260, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.quickTextButton1_2.setFont(font)
        self.quickTextButton1_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.quickTextButton1_2.setIconSize(QtCore.QSize(32, 32))
        self.quickTextButton1_2.setObjectName("quickTextButton1_2")
        self.line_6 = QtWidgets.QFrame(newEntryWidget)
        self.line_6.setGeometry(QtCore.QRect(110, 240, 731, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.attachedField = QtWidgets.QLineEdit(newEntryWidget)
        self.attachedField.setEnabled(False)
        self.attachedField.setGeometry(QtCore.QRect(340, 440, 361, 22))
        self.attachedField.setObjectName("attachedField")
        self.label_7 = QtWidgets.QLabel(newEntryWidget)
        self.label_7.setGeometry(QtCore.QRect(150, 430, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.radioLocField = QtWidgets.QTextEdit(newEntryWidget)
        self.radioLocField.setEnabled(False)
        self.radioLocField.setGeometry(QtCore.QRect(361, 96, 231, 56))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.radioLocField.setFont(font)
        self.radioLocField.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioLocField.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.radioLocField.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.radioLocField.setObjectName("radioLocField")
        self.teamComboBox = QtWidgets.QComboBox(newEntryWidget)
        self.teamComboBox.setEnabled(True)
        self.teamComboBox.setGeometry(QtCore.QRect(291, 8, 309, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.teamComboBox.setFont(font)
        self.teamComboBox.setFrame(True)
        self.teamComboBox.setObjectName("teamComboBox")
        self.teamComboBox.raise_()
        self.quickTextButton3.raise_()
        self.quickTextButton6.raise_()
        self.line_3.raise_()
        self.label.raise_()
        self.datumFormatLabel.raise_()
        self.quickTextButton9.raise_()
        self.statusGroupBox.raise_()
        self.label_5.raise_()
        self.to_fromField.raise_()
        self.quickTextButton2.raise_()
        self.quickTextButton1.raise_()
        self.messageField.raise_()
        self.quickTextButton5.raise_()
        self.quickTextButton11.raise_()
        self.buttonBox.raise_()
        self.quickTextButton4.raise_()
        self.line_4.raise_()
        self.label_6.raise_()
        self.quickTextUndoButton.raise_()
        self.timeField.raise_()
        self.teamField.raise_()
        self.quickTextButton7.raise_()
        self.quickTextButton8.raise_()
        self.label_2.raise_()
        self.quickTextButton10.raise_()
        self.line_5.raise_()
        self.quickTextButton1_2.raise_()
        self.line_6.raise_()
        self.attachedField.raise_()
        self.label_7.raise_()
        self.radioLocField.raise_()

        self.retranslateUi(newEntryWidget)
        self.buttonBox.accepted.connect(newEntryWidget.accept)
        self.buttonBox.rejected.connect(newEntryWidget.close)
        self.quickTextButton1.clicked.connect(newEntryWidget.quickTextAction)
        self.quickTextButton2.clicked.connect(newEntryWidget.quickTextAction)
        self.quickTextButton3.clicked.connect(newEntryWidget.quickTextAction)
        self.quickTextButton4.clicked['bool'].connect(newEntryWidget.quickTextAction)
        self.quickTextButton5.clicked.connect(newEntryWidget.quickTextAction)
        self.quickTextButton6.clicked.connect(newEntryWidget.quickTextAction)
        self.quickTextButton7.clicked['bool'].connect(newEntryWidget.quickTextAction)
        self.quickTextButton11.clicked.connect(newEntryWidget.quickTextAction)
        self.quickTextUndoButton.clicked.connect(newEntryWidget.quickTextUndo)
        self.quickTextButton9.clicked.connect(newEntryWidget.quickTextClueAction)
        self.teamField.customContextMenuRequested['QPoint'].connect(newEntryWidget.openChangeCallsignDialog)
        self.quickTextButton8.clicked.connect(newEntryWidget.quickTextAction)
        self.quickTextButton10.clicked.connect(newEntryWidget.quickTextSubjectLocatedAction)
        self.quickTextButton1_2.clicked.connect(newEntryWidget.quickTextAction)
        self.teamComboBox.activated['QString'].connect(newEntryWidget.setCallsignFromComboBox)
        self.teamField.textChanged['QString'].connect(newEntryWidget.teamFieldTextChanged)
        self.teamField.editingFinished.connect(newEntryWidget.teamFieldEditingFinished)
        QtCore.QMetaObject.connectSlotsByName(newEntryWidget)
        newEntryWidget.setTabOrder(self.teamField, self.messageField)
        newEntryWidget.setTabOrder(self.messageField, self.to_fromField)
        newEntryWidget.setTabOrder(self.to_fromField, self.quickTextButton10)
        newEntryWidget.setTabOrder(self.quickTextButton10, self.standbyField)

    def retranslateUi(self, newEntryWidget):
        _translate = QtCore.QCoreApplication.translate
        newEntryWidget.setWindowTitle(_translate("newEntryWidget", "Form"))
        newEntryWidget.setToolTip(_translate("newEntryWidget", "Type a callsign, or, choose from existing callsigns"))
        self.quickTextButton3.setText(_translate("newEntryWidget", "COMPLETED ASSIGNMENT  [F3]"))
        self.quickTextButton3.setShortcut(_translate("newEntryWidget", "F3"))
        self.quickTextButton6.setText(_translate("newEntryWidget", "WELFARE CHECK: OK  [F8]"))
        self.quickTextButton6.setShortcut(_translate("newEntryWidget", "F8"))
        self.label.setText(_translate("newEntryWidget", "Message:"))
        self.datumFormatLabel.setText(_translate("newEntryWidget", "DATUM / FORMAT"))
        self.quickTextButton9.setText(_translate("newEntryWidget", "LOCATED A CLUE  [F10]"))
        self.quickTextButton9.setShortcut(_translate("newEntryWidget", "F10"))
        self.statusGroupBox.setTitle(_translate("newEntryWidget", "Team Status"))
        self.at_icField.setText(_translate("newEntryWidget", "At IC"))
        self.in_transitField.setText(_translate("newEntryWidget", "In Transit"))
        self.workingField.setText(_translate("newEntryWidget", "Working"))
        self.waitingForTransportField.setText(_translate("newEntryWidget", "Waiting for Transport"))
        self.standbyField.setText(_translate("newEntryWidget", "STANDBY"))
        self.availableField.setText(_translate("newEntryWidget", "Available"))
        self.availableField_2.setText(_translate("newEntryWidget", "Off Duty"))
        self.label_5.setText(_translate("newEntryWidget", "Radio Location:"))
        self.to_fromField.setItemText(0, _translate("newEntryWidget", "FROM"))
        self.to_fromField.setItemText(1, _translate("newEntryWidget", "TO"))
        self.quickTextButton2.setText(_translate("newEntryWidget", "STARTING ASSIGNMENT  [F2]"))
        self.quickTextButton2.setShortcut(_translate("newEntryWidget", "F2"))
        self.quickTextButton1.setText(_translate("newEntryWidget", "DEPARTING IC  [F1]"))
        self.quickTextButton1.setShortcut(_translate("newEntryWidget", "F1"))
        self.quickTextButton5.setText(_translate("newEntryWidget", "RADIO CHECK: OK  [F7]"))
        self.quickTextButton5.setShortcut(_translate("newEntryWidget", "F7"))
        self.quickTextButton11.setText(_translate("newEntryWidget", "REQUESTING DEPUTY  [F12]"))
        self.quickTextButton11.setShortcut(_translate("newEntryWidget", "F12"))
        self.quickTextButton4.setText(_translate("newEntryWidget", "AT IC  [F6]"))
        self.quickTextButton4.setShortcut(_translate("newEntryWidget", "F6"))
        self.label_6.setText(_translate("newEntryWidget", "Time:"))
        self.quickTextUndoButton.setText(_translate("newEntryWidget", "UNDO  [Ctrl+Z]"))
        self.quickTextUndoButton.setShortcut(_translate("newEntryWidget", "Ctrl+Z"))
        self.quickTextButton7.setText(_translate("newEntryWidget", "REQUESTING TRANSPORT  [F5]"))
        self.quickTextButton7.setShortcut(_translate("newEntryWidget", "F5"))
        self.quickTextButton8.setText(_translate("newEntryWidget", "STANDBY  [F9]"))
        self.quickTextButton8.setShortcut(_translate("newEntryWidget", "F9"))
        self.label_2.setText(_translate("newEntryWidget", "Right-click to change and remember callsign"))
        self.quickTextButton10.setText(_translate("newEntryWidget", "SUBJECT LOCATED  [F11]"))
        self.quickTextButton10.setShortcut(_translate("newEntryWidget", "F11"))
        self.quickTextButton1_2.setText(_translate("newEntryWidget", "ENROUTE TO IC  [F4]"))
        self.quickTextButton1_2.setShortcut(_translate("newEntryWidget", "F1"))
        self.label_7.setText(_translate("newEntryWidget", "Attached callsign(s):"))

