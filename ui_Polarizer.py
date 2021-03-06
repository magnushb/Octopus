# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Polarizer.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import numpy as np

zero_pos = 201240
horizontal_pos = 45
vertical_pos = 90 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 439)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 210, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 210, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(136, 70, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 60, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lcdNumber = QtWidgets.QLCDNumber(8,self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(470, 90, 250, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 301, 41))
        font = QtGui.QFont()
        font.setFamily("aakar")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(180, 240, 61, 111))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(250, 240, 51, 111))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(121, 240, 51, 111))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(460, 250, 213, 25))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.widget4 = QtWidgets.QWidget(self.centralwidget)
        self.widget4.setGeometry(QtCore.QRect(150, 100, 82, 71))
        self.widget4.setObjectName("widget4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.widget4)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
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
        self.label.setText(_translate("MainWindow", "Relative motion"))
        self.label_2.setText(_translate("MainWindow", "Absolute position"))
        self.label_3.setText(_translate("MainWindow", "Preset polarization states"))
        self.label_4.setText(_translate("MainWindow", "Current position"))
        self.label_5.setText(_translate("MainWindow", "Polarizer controller"))
        self.pushButton_3.setText(_translate("MainWindow", "+"))
        self.pushButton_3.clicked.connect(self.move_relative_1)
        self.pushButton_7.setText(_translate("MainWindow", "+"))
        self.pushButton_7.clicked.connect(self.move_relative_2)
        self.pushButton_5.setText(_translate("MainWindow", "+"))
        self.pushButton_5.clicked.connect(self.move_relative_3)
        self.pushButton_4.setText(_translate("MainWindow", "-"))
        self.pushButton_4.clicked.connect(self.move_relative_1_neg)
        self.pushButton_8.setText(_translate("MainWindow", "-"))
        self.pushButton_8.clicked.connect(self.move_relative_2_neg)
        self.pushButton_6.setText(_translate("MainWindow", "-"))
        self.pushButton_6.clicked.connect(self.move_relative_3_neg)
        self.pushButton_9.setText(_translate("MainWindow", "Move"))
        self.pushButton.setText(_translate("MainWindow", "Vertical"))
        self.pushButton.clicked.connect(self.move_to_vertical)
        self.pushButton_2.setText(_translate("MainWindow", "Horizontal"))
        self.pushButton_2.clicked.connect(self.move_to_horizontal)
        self.pushButton_9.clicked.connect(self.move_to)

    def do_at_startup(self, MainWindow):
        """
        Query current position when program is started, 
        and add preset relative step sizes.
        """
        # Initiate connection
        with serial.Serial('COM5') as ser:
            ser.baudrate = 19200
            ser.bytesize = 8
            ser.parity = 'N'
            ser.xonxoff = 1
            ser.rtscts = 1
            ser.timeout = 5
            
            # Ask for current position
            ser.write(b'0PA?'+b'\r\n')
            answ = ser.readline()
            curr_pos = answ.decode('utf-8').split()
            print('Current position: ',curr_pos)
            # Update LDC display with current position
            self.lcdNumber.display(int(curr_pos[1])+zero_pos)
            # Set values for relative movements
            self.lineEdit.setText("10")
            self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
            self.lineEdit_2.setText("100")
            self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
            self.lineEdit_3.setText("1000")
            self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)



    def move_relative_1(self, MainWindow):
        """
        Move with the number of steps given in input box 1 relative the current position.
        """
        with serial.Serial('COM5') as ser:
            ser.baudrate = 19200
            ser.bytesize = 8
            ser.parity = 'N'
            ser.xonxoff = 1
            ser.rtscts = 1
            ser.timeout = 5
        
            # Get step size
            to_move = self.lineEdit.text()
            # Construnct command
            move_string = bytes('0PR{}'.format(to_move),'utf-8')
            # Move
            ser.write(move_string+b'\r\n')
            answ = ser.readline()
            # Ask for current position
            ser.write(b'0PA?'+b'\r\n')
            answ = ser.readline()
            curr_pos = answ.decode('utf-8').split()[1]
            # Update LCD display
            self.lcdNumber.display(int(curr_pos)+zero_pos)

    def move_relative_1_neg(self, MainWindow):
        """
        Move with the number of steps given in input box 1 relative the current position.
        """
        with serial.Serial('COM5') as ser:
            ser.baudrate = 19200
            ser.bytesize = 8
            ser.parity = 'N'
            ser.xonxoff = 1
            ser.rtscts = 1
            ser.timeout = 5
        
            # Get step size
            to_move = self.lineEdit.text()
            # Construnct command
            move_string = bytes('0PR-{}'.format(to_move),'utf-8')
            # Move
            ser.write(move_string+b'\r\n')
            answ = ser.readline()
            # Ask for current position
            ser.write(b'0PA?'+b'\r\n')
            answ = ser.readline()
            curr_pos = answ.decode('utf-8').split()[1]
            # Update LCD display
            self.lcdNumber.display(int(curr_pos)+zero_pos)

    def move_relative_2(self, MainWindow):
        """
        Move with the number of steps given in input box 1 relative the current position.
        """
        with serial.Serial('COM5') as ser:
            ser.baudrate = 19200
            ser.bytesize = 8
            ser.parity = 'N'
            ser.xonxoff = 1
            ser.rtscts = 1
            ser.timeout = 5
        
            # Get step size
            to_move = self.lineEdit_2.text()
            # Construnct command
            move_string = bytes('0PR{}'.format(to_move),'utf-8')
            # Move
            ser.write(move_string+b'\r\n')
            answ = ser.readline()
            # Ask for current position
            ser.write(b'0PA?'+b'\r\n')
            answ = ser.readline()
            curr_pos = answ.decode('utf-8').split()[1]
            # Update LCD display
            self.lcdNumber.display(int(curr_pos)+zero_pos)

    def move_relative_2_neg(self, MainWindow):
        """
        Move with the number of steps given in input box 1 relative the current position.
        """
        with serial.Serial('COM5') as ser:
            ser.baudrate = 19200
            ser.bytesize = 8
            ser.parity = 'N'
            ser.xonxoff = 1
            ser.rtscts = 1
            ser.timeout = 5
        
            # Get step size
            to_move = self.lineEdit_2.text()
            # Construnct command
            move_string = bytes('0PR-{}'.format(to_move),'utf-8')
            # Move
            ser.write(move_string+b'\r\n')
            answ = ser.readline()
            # Ask for current position
            ser.write(b'0PA?'+b'\r\n')
            answ = ser.readline()
            curr_pos = answ.decode('utf-8').split()[1]
            # Update LCD display
            self.lcdNumber.display(int(curr_pos)+zero_pos)

    def move_relative_3(self, MainWindow):
        """
        Move with the number of steps given in input box 1 relative the current position.
        """
        with serial.Serial('COM5') as ser:
            ser.baudrate = 19200
            ser.bytesize = 8
            ser.parity = 'N'
            ser.xonxoff = 1
            ser.rtscts = 1
            ser.timeout = 5
        
            # Get step size
            to_move = self.lineEdit_3.text()
            # Construnct command
            move_string = bytes('0PR{}'.format(to_move),'utf-8')
            # Move
            ser.write(move_string+b'\r\n')
            answ = ser.readline()
            # Ask for current position
            ser.write(b'0PA?'+b'\r\n')
            answ = ser.readline()
            curr_pos = answ.decode('utf-8').split()[1]
            # Update LCD display
            self.lcdNumber.display(int(curr_pos)+zero_pos)

    def move_relative_3_neg(self, MainWindow):
        """
        Move with the number of steps given in input box 1 relative the current position.
        """
        with serial.Serial('COM5') as ser:
            ser.baudrate = 19200
            ser.bytesize = 8
            ser.parity = 'N'
            ser.xonxoff = 1
            ser.rtscts = 1
            ser.timeout = 5
        
            # Get step size
            to_move = self.lineEdit_3.text()
            # Construnct command
            move_string = bytes('0PR-{}'.format(to_move),'utf-8')
            # Move
            ser.write(move_string+b'\r\n')
            answ = ser.readline()
            # Ask for current position
            ser.write(b'0PA?'+b'\r\n')
            answ = ser.readline()
            curr_pos = answ.decode('utf-8').split()[1]
            # Update LCD display
            self.lcdNumber.display(int(curr_pos)+zero_pos)

    def move_to(self, MainWindow):
        """
        Send command to move to absolute position
        """
        # Initiate connection
        with serial.Serial('COM5') as ser:
            ser.baudrate = 19200
            ser.bytesize = 8
            ser.parity = 'N'
            ser.xonxoff = 1
            ser.rtscts = 1
            ser.timeout = 5
            
            # Get how much to move
            to_move = self.lineEdit_4.text()
            if not to_move:
                to_move = '0'
            #to_move = to_move.astype(np.int)
            # Move
            pos_string = bytes('0PA{}'.format(to_move),'utf-8')
            ser.write(pos_string+b'\r\n')
            answ = ser.readline()
            #print('pos:',answ)
            # Ask for current position
            ser.write(b'0PA?'+b'\r\n')
            answ = ser.readline()
            curr_pos = answ.decode('utf-8').split()
            print('Current position: ',curr_pos)
            # Ask for home position
            ser.write(b'0OR?'+b'\r\n')
            answ = ser.readline()
            home_pos = answ.decode('utf-8').split()[1]
            print(home_pos)
            # Update LDC display with current position
            self.lcdNumber.display(int(curr_pos[1])+zero_pos)
        
    def move_to_vertical(self, MainWindow):
        """
        Send command to move to position of vertical polarization
        """
        # Initiate connection
        with serial.Serial('COM5') as ser:
            ser.baudrate = 19200
            ser.bytesize = 8
            ser.parity = 'N'
            ser.xonxoff = 1
            ser.rtscts = 1
            ser.timeout = 5
            
            # Move
            pos_string = bytes('0PA{}'.format(vertical_pos),'utf-8')
            ser.write(pos_string+b'\r\n')
            answ = ser.readline()
            # Ask for current position
            ser.write(b'0PA?'+b'\r\n')
            answ = ser.readline()
            curr_pos = answ.decode('utf-8').split()
            # Update LDC display with current position
            self.lcdNumber.display(int(curr_pos[1])+zero_pos)

    def move_to_horizontal(self, MainWindow):
        """
        Send command to move to position of horizontal polarization
        """
        # Initiate connection
        with serial.Serial('COM5') as ser:
            ser.baudrate = 19200
            ser.bytesize = 8
            ser.parity = 'N'
            ser.xonxoff = 1
            ser.rtscts = 1
            ser.timeout = 5
            
            # Move
            pos_string = bytes('0PA{}'.format(horizontal_pos),'utf-8')
            ser.write(pos_string+b'\r\n')
            answ = ser.readline()
            # Ask for current position
            ser.write(b'0PA?'+b'\r\n')
            answ = ser.readline()
            curr_pos = answ.decode('utf-8').split()
            # Update LDC display with current position
            self.lcdNumber.display(int(curr_pos[1])+zero_pos)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.do_at_startup(MainWindow)
    sys.exit(app.exec_())