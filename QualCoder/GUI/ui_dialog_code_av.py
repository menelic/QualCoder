# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_code_av.ui'
#
# Created: Wed Mar  6 23:29:29 2019
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_code_av(object):
    def setupUi(self, Dialog_code_av):
        Dialog_code_av.setObjectName("Dialog_code_av")
        Dialog_code_av.resize(1021, 596)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_code_av)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog_code_av)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 90))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 90))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_play = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_play.setGeometry(QtCore.QRect(10, 40, 85, 27))
        self.pushButton_play.setObjectName("pushButton_play")
        self.pushButton_stop = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_stop.setGeometry(QtCore.QRect(110, 40, 85, 27))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalSlider_vol = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider_vol.setGeometry(QtCore.QRect(795, 50, 160, 18))
        self.horizontalSlider_vol.setMaximum(100)
        self.horizontalSlider_vol.setProperty("value", 100)
        self.horizontalSlider_vol.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_vol.setObjectName("horizontalSlider_vol")
        self.label_volume = QtWidgets.QLabel(self.groupBox_2)
        self.label_volume.setGeometry(QtCore.QRect(700, 46, 81, 20))
        self.label_volume.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_volume.setObjectName("label_volume")
        self.label_time = QtWidgets.QLabel(self.groupBox_2)
        self.label_time.setGeometry(QtCore.QRect(410, 43, 231, 21))
        self.label_time.setObjectName("label_time")
        self.label_time_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_time_2.setGeometry(QtCore.QRect(730, 70, 231, 21))
        self.label_time_2.setObjectName("label_time_2")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 10, 1003, 23))
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(10)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.pushButton_coding = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_coding.setGeometry(QtCore.QRect(210, 40, 181, 27))
        self.pushButton_coding.setObjectName("pushButton_coding")
        self.label_code = QtWidgets.QLabel(self.groupBox_2)
        self.label_code.setGeometry(QtCore.QRect(210, 70, 431, 17))
        self.label_code.setObjectName("label_code")
        self.label_coder = QtWidgets.QLabel(self.groupBox_2)
        self.label_coder.setGeometry(QtCore.QRect(4, 72, 201, 17))
        self.label_coder.setObjectName("label_coder")
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(Dialog_code_av)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.gridLayout_2.addWidget(self.treeWidget, 1, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Dialog_code_av)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 1, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Dialog_code_av)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog_code_av)
        QtCore.QMetaObject.connectSlotsByName(Dialog_code_av)
        Dialog_code_av.setTabOrder(self.pushButton_play, self.pushButton_stop)
        Dialog_code_av.setTabOrder(self.pushButton_stop, self.horizontalSlider_vol)

    def retranslateUi(self, Dialog_code_av):
        _translate = QtCore.QCoreApplication.translate
        Dialog_code_av.setWindowTitle(_translate("Dialog_code_av", "Code Audio Video"))
        self.pushButton_play.setText(_translate("Dialog_code_av", "Play"))
        self.pushButton_stop.setText(_translate("Dialog_code_av", "Stop"))
        self.label_volume.setText(_translate("Dialog_code_av", "Volume"))
        self.label_time.setText(_translate("Dialog_code_av", "Time:"))
        self.label_time_2.setText(_translate("Dialog_code_av", "Duration: "))
        self.horizontalSlider.setToolTip(_translate("Dialog_code_av", "<html><head/><body><p>Left click on the slider button and drag left or right to change video position.</p></body></html>"))
        self.pushButton_coding.setToolTip(_translate("Dialog_code_av", "<html><head/><body><p>Select a code. Play video from start or another position. Press the Start coding button to begin coding the audio/video segement. Press the Stop coding button to end the coded segment.</p></body></html>"))
        self.pushButton_coding.setText(_translate("Dialog_code_av", "Start coding"))
        self.label_code.setText(_translate("Dialog_code_av", "Code:"))
        self.label_coder.setText(_translate("Dialog_code_av", "Coder:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_code_av = QtWidgets.QDialog()
    ui = Ui_Dialog_code_av()
    ui.setupUi(Dialog_code_av)
    Dialog_code_av.show()
    sys.exit(app.exec_())
