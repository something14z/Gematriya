# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tree_generator_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PosForm(object):
    def setupUi(self, PosForm):
        PosForm.setObjectName("PosForm")
        PosForm.resize(872, 517)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PosForm.sizePolicy().hasHeightForWidth())
        PosForm.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        PosForm.setPalette(palette)
        PosForm.setAutoFillBackground(False)
        self.trees_generate_btn = QtWidgets.QPushButton(PosForm)
        self.trees_generate_btn.setGeometry(QtCore.QRect(330, 440, 241, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.trees_generate_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.trees_generate_btn.setFont(font)
        self.trees_generate_btn.setObjectName("trees_generate_btn")
        self.gridLayoutWidget = QtWidgets.QWidget(PosForm)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 20, 660, 411))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.let2_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.let2_checkBox.setFont(font)
        self.let2_checkBox.setObjectName("let2_checkBox")
        self.gridLayout.addWidget(self.let2_checkBox, 2, 0, 1, 1)
        self.let9_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.let9_checkBox.setFont(font)
        self.let9_checkBox.setObjectName("let9_checkBox")
        self.gridLayout.addWidget(self.let9_checkBox, 9, 0, 1, 1)
        self.let8_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.let8_checkBox.setFont(font)
        self.let8_checkBox.setObjectName("let8_checkBox")
        self.gridLayout.addWidget(self.let8_checkBox, 8, 0, 1, 1)
        self.let3_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.let3_checkBox.setFont(font)
        self.let3_checkBox.setObjectName("let3_checkBox")
        self.gridLayout.addWidget(self.let3_checkBox, 3, 0, 1, 1)
        self.let1_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.let1_checkBox.setFont(font)
        self.let1_checkBox.setObjectName("let1_checkBox")
        self.gridLayout.addWidget(self.let1_checkBox, 1, 0, 1, 1)
        self.let6_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.let6_checkBox.setFont(font)
        self.let6_checkBox.setObjectName("let6_checkBox")
        self.gridLayout.addWidget(self.let6_checkBox, 6, 0, 1, 1)
        self.let4_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.let4_checkBox.setFont(font)
        self.let4_checkBox.setObjectName("let4_checkBox")
        self.gridLayout.addWidget(self.let4_checkBox, 4, 0, 1, 1)
        self.let7_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.let7_checkBox.setFont(font)
        self.let7_checkBox.setObjectName("let7_checkBox")
        self.gridLayout.addWidget(self.let7_checkBox, 7, 0, 1, 1)
        self.let5_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.let5_checkBox.setFont(font)
        self.let5_checkBox.setObjectName("let5_checkBox")
        self.gridLayout.addWidget(self.let5_checkBox, 5, 0, 1, 1)
        self.gen_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.gen_checkBox.setFont(font)
        self.gen_checkBox.setObjectName("gen_checkBox")
        self.gridLayout.addWidget(self.gen_checkBox, 0, 0, 1, 1)
        self.last_letter_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.last_letter_checkBox.setFont(font)
        self.last_letter_checkBox.setObjectName("last_letter_checkBox")
        self.gridLayout.addWidget(self.last_letter_checkBox, 10, 0, 1, 1)
        self.axial_letter_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.axial_letter_checkBox.setFont(font)
        self.axial_letter_checkBox.setObjectName("axial_letter_checkBox")
        self.gridLayout.addWidget(self.axial_letter_checkBox, 11, 0, 1, 1)
        self.shock_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.shock_checkBox.setFont(font)
        self.shock_checkBox.setObjectName("shock_checkBox")
        self.gridLayout.addWidget(self.shock_checkBox, 0, 1, 1, 1)
        self.spec_weight_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.spec_weight_checkBox.setFont(font)
        self.spec_weight_checkBox.setObjectName("spec_weight_checkBox")
        self.gridLayout.addWidget(self.spec_weight_checkBox, 1, 1, 1, 1)
        self.mirrored_img_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.mirrored_img_checkBox.setFont(font)
        self.mirrored_img_checkBox.setObjectName("mirrored_img_checkBox")
        self.gridLayout.addWidget(self.mirrored_img_checkBox, 2, 1, 1, 1)
        self.complementary_img_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.complementary_img_checkBox.setFont(font)
        self.complementary_img_checkBox.setObjectName("complementary_img_checkBox")
        self.gridLayout.addWidget(self.complementary_img_checkBox, 3, 1, 1, 1)
        self.hermetic_root_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.hermetic_root_checkBox.setFont(font)
        self.hermetic_root_checkBox.setObjectName("hermetic_root_checkBox")
        self.gridLayout.addWidget(self.hermetic_root_checkBox, 4, 1, 1, 1)
        self.heavenly_face_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.heavenly_face_checkBox.setFont(font)
        self.heavenly_face_checkBox.setObjectName("heavenly_face_checkBox")
        self.gridLayout.addWidget(self.heavenly_face_checkBox, 9, 1, 1, 1)
        self.average_weight_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.average_weight_checkBox.setFont(font)
        self.average_weight_checkBox.setObjectName("average_weight_checkBox")
        self.gridLayout.addWidget(self.average_weight_checkBox, 5, 1, 1, 1)
        self.middle_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.middle_checkBox.setFont(font)
        self.middle_checkBox.setObjectName("middle_checkBox")
        self.gridLayout.addWidget(self.middle_checkBox, 6, 1, 1, 1)
        self.god_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.god_checkBox.setFont(font)
        self.god_checkBox.setObjectName("god_checkBox")
        self.gridLayout.addWidget(self.god_checkBox, 7, 1, 1, 1)
        self.energy_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.energy_checkBox.setFont(font)
        self.energy_checkBox.setObjectName("energy_checkBox")
        self.gridLayout.addWidget(self.energy_checkBox, 10, 1, 1, 1)
        self.base_letter_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.base_letter_checkBox.setFont(font)
        self.base_letter_checkBox.setObjectName("base_letter_checkBox")
        self.gridLayout.addWidget(self.base_letter_checkBox, 8, 1, 1, 1)

        self.retranslateUi(PosForm)
        QtCore.QMetaObject.connectSlotsByName(PosForm)

    def retranslateUi(self, PosForm):
        _translate = QtCore.QCoreApplication.translate
        PosForm.setWindowTitle(_translate("PosForm", "Генератор деревьев"))
        self.trees_generate_btn.setText(_translate("PosForm", "Сгенерировать деревья"))
        self.let2_checkBox.setText(_translate("PosForm", "2-я буква"))
        self.let9_checkBox.setText(_translate("PosForm", "9-я буква"))
        self.let8_checkBox.setText(_translate("PosForm", "8-я буква"))
        self.let3_checkBox.setText(_translate("PosForm", "3-я буква"))
        self.let1_checkBox.setText(_translate("PosForm", "1-я буква"))
        self.let6_checkBox.setText(_translate("PosForm", "6-я буква"))
        self.let4_checkBox.setText(_translate("PosForm", "4-я буква"))
        self.let7_checkBox.setText(_translate("PosForm", "7-я буква"))
        self.let5_checkBox.setText(_translate("PosForm", "5-я буква"))
        self.gen_checkBox.setText(_translate("PosForm", "Генограмма"))
        self.last_letter_checkBox.setText(_translate("PosForm", "Буква на последней позиции"))
        self.axial_letter_checkBox.setText(_translate("PosForm", "Осевая буква"))
        self.shock_checkBox.setText(_translate("PosForm", "Ударная буква с номером позиции"))
        self.spec_weight_checkBox.setText(_translate("PosForm", "УВ и ТО"))
        self.mirrored_img_checkBox.setText(_translate("PosForm", "ЗЧО и его ТО"))
        self.complementary_img_checkBox.setText(_translate("PosForm", "КЧО и его ТО"))
        self.hermetic_root_checkBox.setText(_translate("PosForm", "ГК и его ТО"))
        self.heavenly_face_checkBox.setText(_translate("PosForm", "Небесный и земной лики"))
        self.average_weight_checkBox.setText(_translate("PosForm", "СУВ буквы"))
        self.middle_checkBox.setText(_translate("PosForm", "СТО"))
        self.god_checkBox.setText(_translate("PosForm", "Боги имён"))
        self.energy_checkBox.setText(_translate("PosForm", "Энергетическая направленность"))
        self.base_letter_checkBox.setText(_translate("PosForm", "Опорные буквы"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PosForm = QtWidgets.QWidget()
    ui = Ui_PosForm()
    ui.setupUi(PosForm)
    PosForm.show()
    sys.exit(app.exec_())
