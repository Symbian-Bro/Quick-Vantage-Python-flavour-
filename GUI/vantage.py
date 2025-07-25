# Form implementation generated from reading ui file 'quick-vantage.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(989, 827)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 130, 901, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(246, 245, 244)")
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setGeometry(QtCore.QRect(10, 220, 941, 501))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.widget_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 941, 501))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_3 = QtWidgets.QWidget(parent=self.verticalLayoutWidget_2)
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(parent=self.widget_3)
        self.widget_4.setGeometry(QtCore.QRect(9, 10, 921, 81))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(parent=self.widget_4)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(9, 0, 901, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_4)
        self.label_2.setStyleSheet("color: rgb(246, 245, 244)")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.CM_VAL = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_4)
        self.CM_VAL.setStyleSheet("color: rgb(246, 245, 244);")
        self.CM_VAL.setObjectName("CM_VAL")
        self.horizontalLayout_8.addWidget(self.CM_VAL)
        self.CM = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_4)
        self.CM.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.CM.setCheckable(True)
        self.CM.setObjectName("CM")
        self.horizontalLayout_8.addWidget(self.CM)
        self.widget_5 = QtWidgets.QWidget(parent=self.widget_3)
        self.widget_5.setGeometry(QtCore.QRect(9, 109, 921, 101))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=self.widget_5)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(9, 10, 901, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_3)
        self.label_3.setStyleSheet("color: rgb(246, 245, 244)")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.FL_VAL = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_3)
        self.FL_VAL.setStyleSheet("color: rgb(246, 245, 244);")
        self.FL_VAL.setObjectName("FL_VAL")
        self.horizontalLayout_7.addWidget(self.FL_VAL)
        self.FL = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_3)
        self.FL.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.FL.setCheckable(True)
        self.FL.setObjectName("FL")
        self.horizontalLayout_7.addWidget(self.FL)
        self.widget_6 = QtWidgets.QWidget(parent=self.widget_3)
        self.widget_6.setGeometry(QtCore.QRect(9, 229, 921, 131))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.widget_6)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 20, 901, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.label_6.setStyleSheet("color : rgb(246, 245, 244)")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.Level = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.Level.setStyleSheet("color: rgb(246, 245, 244);")
        self.Level.setObjectName("Level")
        self.horizontalLayout_6.addWidget(self.Level)
        self.Slider = QtWidgets.QSlider(parent=self.horizontalLayoutWidget_2)
        self.Slider.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.Slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.Slider.setObjectName("Slider")
        self.horizontalLayout_6.addWidget(self.Slider)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 989, 32))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Quick Vantage"))
        self.label_2.setText(_translate("MainWindow", "Conservation Mode"))
        self.CM_VAL.setText(_translate("MainWindow", "[1]"))
        self.CM.setText(_translate("MainWindow", "Toggle"))
        self.label_3.setText(_translate("MainWindow", "Function Lock"))
        self.FL_VAL.setText(_translate("MainWindow", "[0]"))
        self.FL.setText(_translate("MainWindow", "Toggle"))
        self.label_6.setText(_translate("MainWindow", "   Keyboard Back Light Level"))
        self.Level.setText(_translate("MainWindow", "  [Level]    "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
