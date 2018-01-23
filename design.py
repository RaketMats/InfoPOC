# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1108, 927)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 410, 111, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.treeProcesses = QtGui.QTreeWidget(self.centralwidget)
        self.treeProcesses.setGeometry(QtCore.QRect(10, 430, 321, 431))
        self.treeProcesses.setColumnCount(1)
        self.treeProcesses.setObjectName(_fromUtf8("treeProcesses"))
        self.treeProcesses.headerItem().setText(0, _fromUtf8("1"))
        self.treeProcesses.header().setVisible(False)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(340, 430, 761, 431))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(340, 410, 131, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.cmdOkTableView = QtGui.QPushButton(self.centralwidget)
        self.cmdOkTableView.setGeometry(QtCore.QRect(340, 880, 71, 21))
        self.cmdOkTableView.setObjectName(_fromUtf8("cmdOkTableView"))
        self.cmdSaveState = QtGui.QPushButton(self.centralwidget)
        self.cmdSaveState.setGeometry(QtCore.QRect(90, 880, 75, 23))
        self.cmdSaveState.setObjectName(_fromUtf8("cmdSaveState"))
        self.cmdLoadState = QtGui.QPushButton(self.centralwidget)
        self.cmdLoadState.setGeometry(QtCore.QRect(10, 880, 75, 23))
        self.cmdLoadState.setObjectName(_fromUtf8("cmdLoadState"))
        self.cmdTestUnicode = QtGui.QPushButton(self.centralwidget)
        self.cmdTestUnicode.setGeometry(QtCore.QRect(440, 870, 93, 28))
        self.cmdTestUnicode.setObjectName(_fromUtf8("cmdTestUnicode"))
        self.txtUnicodeTest = QtGui.QLineEdit(self.centralwidget)
        self.txtUnicodeTest.setGeometry(QtCore.QRect(550, 870, 113, 22))
        self.txtUnicodeTest.setObjectName(_fromUtf8("txtUnicodeTest"))
        self.cmdDocPlan = QtGui.QPushButton(self.centralwidget)
        self.cmdDocPlan.setGeometry(QtCore.QRect(1020, 800, 81, 23))
        self.cmdDocPlan.setObjectName(_fromUtf8("cmdDocPlan"))
        self.imageLabel = QtGui.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(20, 20, 850, 400))
        self.imageLabel.setFrameShape(QtGui.QFrame.Box)
        self.imageLabel.setObjectName(_fromUtf8("imageLabel"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_4.setText(_translate("MainWindow", "Processer", None))
        self.label_11.setText(_translate("MainWindow", "Beskrivning", None))
        self.cmdOkTableView.setText(_translate("MainWindow", "Accept", None))
        self.cmdSaveState.setText(_translate("MainWindow", "Save File", None))
        self.cmdLoadState.setText(_translate("MainWindow", "Open File", None))
        self.cmdTestUnicode.setText(_translate("MainWindow", "Test Unicode", None))
        self.cmdDocPlan.setText(_translate("MainWindow", "Dokumentplan", None))
        self.imageLabel.setText(_translate("MainWindow", "Image Label", None))

