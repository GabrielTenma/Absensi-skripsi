#⡀⠀⢰⣙⢸⡇⠀⠨⣿⣿⣿⣿⣿⣿⣮⡁⠀⣆⣠⡁⠀⣻⣯⣀⠀⠀⠀⠀⠀⠀
#⣿⣦⡀⠈⠙⢇⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣝⣿⣮⡆⠀⠀⠀⠀
#⣿⣿⣿⣦⡀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣫⠿⠋⠁⠀⠀⠀⠀
#⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢻⣿⣿⣿⣿⣿⡇⠘⡄⠀⠀⠀⠀⠀
#⣻⠟⣽⣿⣿⣿⣿⣿⣿⣿⣿⢛⣩⣟⢷⣾⣿⣿⣿⣿⣿⣿⡇⠀⢹⣦⣄⣀⡁⣀
#⠃⣸⣿⣿⣿⣿⡏⠟⢛⠀⠨⠻⠛⠻⠿⢽⣦⣦⠾⢿⣿⡟⠀⠀⢸⣿⣿⣿⣿⢿
#⣾⣿⣿⣿⣿⠁⢸⣦⣤⢃⠢⠤⣭⣦⣄⠊⠏⠀⠁⢸⣿⣿⣷⣶⣼⣿⣿⣿⣿⣿
#⣿⣿⡇⢻⡇⢂⠘⡃⠈⢙⣿⣾⣤⣤⠀⠀⠀⠀⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#⠛⠉⢁⡎⢿⣝⣳⡇⡜⠻⠊⠁⠀⠀⠀⠀⠀⠀⠀⠊⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿
#⠀⠀⠘⣈⠄⢻⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢁⣸⣿⡿⡛⣿⣿⣿⣿⣿
#⠀⠀⠀⢘⣴⣦⡹⣿⠿⣶⣷⣄⡀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⢧⣿⣿⣿⣿⣿
#⣠⣠⣴⣿⠿⠋⣿⡷⠦⣿⣿⣿⣿⣿⣿⣿⣿⣡⣿⣿⣿⠧⣡⣥⣸⣿⣿⣿⣿⣿
#⠀⠀⠀⠀⠀⣼⡿⢃⡂⣿⣿⣿⣿⣸⣿⣿⣿⣿⣿⣿⢯⣼⣿⣿⣿⣿⣿⣿⣿⣿
#⠀⠀⠀⠠⠚⠋⠀⣬⡐⢸⢈⣿⣿⣿⣿⣿⣿⣿⡟⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#⠀⠀⠀⢀⣀⣤⣼⣿⣿⣧⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

# drawer ui lib
from random import randrange
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from qtpy import QtWidgets, QtCore
from QNotifications import QNotificationArea
import logging as log

# data lib
import cv2
import numpy as np
import array as arr
import sys

# common
import util.CommonUtil as util
import config.variable.ApplicationConstant as appConfig
import config.variable.GlobalVariable as globalVariable
import delivery.Api as delivery

                
class Ui_MainWindow(QtWidgets.QWidget):

    # func :: load all component ui
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.display_width = 607
        self.display_height = 488
        MainWindow.resize(self.display_width, self.display_height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pbScan = QtWidgets.QPushButton(self.centralwidget)
        self.pbScan.setGeometry(QtCore.QRect(100, 350, 401, 51))
        self.pbScan.setFlat(False)
        self.pbScan.setObjectName("pbScan")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 607, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # call retranslate ui
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # func :: add component to mainwindow ui
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Attendance Scan"))

        # button :: pbscan
        self.pbScan.setText(_translate("MainWindow", "Scan"))
        self.pbScan.clicked.connect(self.scanImage)

        # load webcam
        self.initializeWebcam()

        # load notify
        self.initializeNotify()


    # func :: load webcam
    def initializeWebcam(self):

        # create imagelabel display
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(100, 70, 401, 261))
        self.image_label.resize(401,261)
        self.image_label.setObjectName("image_label")

        # create the video capture thread
        self.thread = VideoThread()
        
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        
        # start the thread
        self.thread.start()


    # func :: load notify
    def initializeNotify(self):
        # Create a widget to render the notifications on.
        self.targetWidget = QtWidgets.QWidget(self.centralwidget)
        self.targetWidget.setGeometry(100,100,800,600)
        self.targetWidget.setObjectName("targetWidget")

        # Create a new notification area, and pass it the target widget.
        self.qna = QNotificationArea(self.targetWidget)
        
        # Show the target widget.
        self.targetWidget.show()


    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)

    # func :: convert from cv2 image to QPixmap    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
        p = convert_to_Qt_format.scaled(401, 261, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        return QtGui.QPixmap.fromImage(p)

    # func :: read cap & save img as file
    def take_picture(self):
        ret, img = cap.read()
        cv2.imwrite(appConfig.TAKE_PICTURE_FILENAME, img)
        log.info('[TAKEPICTURE] Image exported: '+ appConfig.TAKE_PICTURE_FILENAME)

    # func :: scan image
    def scanImage(self):
        self.pbScan.setText("Please Wait..")
        self.pbScan.isEnabled = False
        self.take_picture()
        self.pbScan.setText("Scan")
        self.pbScan.isEnabled = True
        self.sendNotify('saved picture!',0)

    # func :: Send notification
    def sendNotify(self, msg, style):
        index = ['primary','info','danger']
        self.qna.display(msg,index[style],2000)

    # func :: send request & recv user name
    def deliveryImage(self, imagePath):
        delivery.matchImagePerson(globalVariable.thermalMaxTemp, imagePath)

    

# Thread Class (videoThread)
class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    def run(self):
        # cv face detect with default haarcascade
        faceDetect = cv2.CascadeClassifier(appConfig.FILE_CASCADE);

        # capture from web cam
        while True:
            # separate ret and frame
            ret, cv_img = cap.read()
            # load thermaldetect temp

            # set image(cv) to grayscale bw
            gray = cv2.cvtColor(cv_img,cv2.COLOR_BGR2GRAY)
            faces = faceDetect.detectMultiScale(gray,1.3,5)
            
            self.thermalDetectValue()

            # set variable if detect face
            globalVariable.isDetectFace = True if faces == True else False

            # create rectangle in face
            for (x,y,w,h) in faces:
                cv2.rectangle(cv_img,(x,y), (x+w,y+h),(0,255,0),2)

            if ret:
                self.change_pixmap_signal.emit(cv_img)

            log.info("Thermal Max Temperature: "+ globalVariable.thermalMaxTemp)
    
    # func :: get value from thermal
    def thermalDetectValue(self):
        # pixel stack data thermal (8x8)
        pixels = globalVariable.sensorTc.pixels                              # alias pixel as sensorTc pixels 
        for x in range(len(pixels)):
            for y in range(len(pixels[0])):
                # save higher value thermal temp
                if(pixels[x][y] > globalVariable.thermalMaxTemp):
                    globalVariable.thermalMaxTemp = pixels[x][y]


# Main app first load
if __name__ == "__main__":

    # Initializer
    util.checkAdafruitBoard()                               # load util check adafruit board

    log.basicConfig(filename=appConfig.LOG_FILENAME,level=log.INFO)

    app = QtWidgets.QApplication(sys.argv)                  # alias QtWidget
    MainWindow = QtWidgets.QMainWindow()                    # set mainwindow as QtWidget
    ui = Ui_MainWindow()                                    # alias ui_Mainwindow
    cap = cv2.VideoCapture(appConfig.CAMERA_INDEX)          # set cap as cv2 videocapture

    ui.setupUi(MainWindow)                                  # load ui
    MainWindow.show()                                       # call mainwindow to show
    sys.exit(app.exec())                                    # exit when mainwindow closed
