# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sandra\Desktop\bfs.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.kvalue_lbl = QtWidgets.QLabel(self.centralwidget)
        self.kvalue_lbl.setGeometry(QtCore.QRect(120, 380, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.kvalue_lbl.setFont(font)
        self.kvalue_lbl.setObjectName("kvalue_lbl")
        self.edgeLbl = QtWidgets.QLabel(self.centralwidget)
        self.edgeLbl.setGeometry(QtCore.QRect(120, 50, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edgeLbl.setFont(font)
        self.edgeLbl.setObjectName("edgeLbl")
        self.hosLbl = QtWidgets.QLabel(self.centralwidget)
        self.hosLbl.setGeometry(QtCore.QRect(120, 210, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hosLbl.setFont(font)
        self.hosLbl.setObjectName("hosLbl")
        self.edgeTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.edgeTxt.setGeometry(QtCore.QRect(410, 50, 261, 61))
        self.edgeTxt.setObjectName("edgeTxt")
        self.hosTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.hosTxt.setGeometry(QtCore.QRect(410, 210, 261, 61))
        self.hosTxt.setObjectName("hosTxt")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(410, 380, 261, 61))
        self.textEdit.setObjectName("textEdit")
        self.uploadEdgeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.uploadEdgeBtn.setGeometry(QtCore.QRect(570, 120, 101, 51))
        self.uploadEdgeBtn.setObjectName("uploadEdgeBtn")
        self.uploadHospitalBtn = QtWidgets.QPushButton(self.centralwidget)
        self.uploadHospitalBtn.setGeometry(QtCore.QRect(570, 280, 101, 51))
        self.uploadHospitalBtn.setObjectName("uploadHospitalBtn")
        self.submitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.submitBtn.setGeometry(QtCore.QRect(570, 450, 101, 51))
        self.submitBtn.setObjectName("submitBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 18))
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
        self.kvalue_lbl.setText(_translate("MainWindow", "Enter k value:"))
        self.edgeLbl.setText(_translate("MainWindow", "Insert edge file:"))
        self.hosLbl.setText(_translate("MainWindow", "Insert hospital file:"))
        self.uploadEdgeBtn.setText(_translate("MainWindow", "Upload"))
        self.uploadHospitalBtn.setText(_translate("MainWindow", "Upload"))
        self.submitBtn.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
