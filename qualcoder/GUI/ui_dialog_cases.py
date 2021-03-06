# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_cases.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_cases(object):
    def setupUi(self, Dialog_cases):
        Dialog_cases.setObjectName("Dialog_cases")
        Dialog_cases.resize(900, 677)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_cases)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog_cases)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.textBrowser = QtWidgets.QTextBrowser(self.splitter)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.splitter, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.label_cases = QtWidgets.QLabel(self.groupBox_2)
        self.label_cases.setMinimumSize(QtCore.QSize(0, 22))
        self.label_cases.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_cases.setObjectName("label_cases")
        self.gridLayout_2.addWidget(self.label_cases, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_add = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_add.setGeometry(QtCore.QRect(0, 0, 231, 28))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_delete = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_delete.setGeometry(QtCore.QRect(240, 30, 231, 28))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_import_cases = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_import_cases.setGeometry(QtCore.QRect(0, 30, 231, 28))
        self.pushButton_import_cases.setObjectName("pushButton_import_cases")
        self.pushButton_add_attribute = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_add_attribute.setGeometry(QtCore.QRect(240, 0, 231, 28))
        self.pushButton_add_attribute.setObjectName("pushButton_add_attribute")
        self.label_filename = QtWidgets.QLabel(self.groupBox)
        self.label_filename.setGeometry(QtCore.QRect(500, 80, 491, 30))
        self.label_filename.setMinimumSize(QtCore.QSize(0, 30))
        self.label_filename.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_filename.setWordWrap(True)
        self.label_filename.setObjectName("label_filename")
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.retranslateUi(Dialog_cases)
        QtCore.QMetaObject.connectSlotsByName(Dialog_cases)
        Dialog_cases.setTabOrder(self.pushButton_add, self.pushButton_import_cases)
        Dialog_cases.setTabOrder(self.pushButton_import_cases, self.pushButton_add_attribute)
        Dialog_cases.setTabOrder(self.pushButton_add_attribute, self.pushButton_delete)
        Dialog_cases.setTabOrder(self.pushButton_delete, self.tableWidget)
        Dialog_cases.setTabOrder(self.tableWidget, self.textBrowser)

    def retranslateUi(self, Dialog_cases):
        _translate = QtCore.QCoreApplication.translate
        Dialog_cases.setWindowTitle(_translate("Dialog_cases", "Cases"))
        self.label.setText(_translate("Dialog_cases", "Click on a case name to view the case. Double click the name to edit the case name. Click on Memo to edit a memo for the case. Click on Files to link files and file text to the case."))
        self.label_cases.setText(_translate("Dialog_cases", "Cases: "))
        self.pushButton_add.setText(_translate("Dialog_cases", "Add case"))
        self.pushButton_delete.setText(_translate("Dialog_cases", "Delete case"))
        self.pushButton_import_cases.setToolTip(_translate("Dialog_cases", "<html><head/><body><p>Import from a <span style=\" font-weight:600;\">comma delimited</span> csv file.</p><p>The file must have a header row and the first column must have the unique case names or identifiers. Subsequent columns are attributes for each case.</p></body></html>"))
        self.pushButton_import_cases.setText(_translate("Dialog_cases", "Import cases"))
        self.pushButton_add_attribute.setText(_translate("Dialog_cases", "Add attribute"))
        self.label_filename.setText(_translate("Dialog_cases", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_cases = QtWidgets.QDialog()
    ui = Ui_Dialog_cases()
    ui.setupUi(Dialog_cases)
    Dialog_cases.show()
    sys.exit(app.exec_())
