# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './F_FL_calculator/F_FL_calculator_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_weight_settings(object):
    def setupUi(self, weight_settings):
        weight_settings.setObjectName("weight_settings")
        weight_settings.resize(400, 482)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        weight_settings.setWindowIcon(icon)
        weight_settings.setSizeGripEnabled(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(weight_settings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(weight_settings)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(21)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(weight_settings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(weight_settings)
        self.buttonBox.accepted.connect(weight_settings.accept)
        self.buttonBox.rejected.connect(weight_settings.reject)
        QtCore.QMetaObject.connectSlotsByName(weight_settings)

    def retranslateUi(self, weight_settings):
        _translate = QtCore.QCoreApplication.translate
        weight_settings.setWindowTitle(_translate("weight_settings", "Энергия букв без удельных весов"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("weight_settings", "Б"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("weight_settings", "Е"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("weight_settings", "Ж"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("weight_settings", "I"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("weight_settings", "Ї"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("weight_settings", "ꙋ"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("weight_settings", "Ш"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("weight_settings", "Щ"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("weight_settings", "Ъ"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("weight_settings", "Ы"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("weight_settings", "Ь"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("weight_settings", "Ѣ"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("weight_settings", "Ю"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("weight_settings", "Я"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("weight_settings", "Ѥ"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("weight_settings", "ѡ"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("weight_settings", "Ѧ"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("weight_settings", "Ѫ"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("weight_settings", "Ѩ"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("weight_settings", "Ѭ"))
        item = self.tableWidget.verticalHeaderItem(20)
        item.setText(_translate("weight_settings", "Ѵ"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("weight_settings", "F"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("weight_settings", "FL"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
import res_rc
