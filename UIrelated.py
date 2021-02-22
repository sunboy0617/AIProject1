from mainwid import Ui_MainWindow
import ButtonAdjust
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox 
from functools import partial
from Algorithm import Astar, Faster_Astar, is_trans_successful
from Algorithm_DC import Astar_algo_DC
from PyQt5.QtCore import QTimer
import time


def isSameNumInList(listname, length):
    set_list = set(listname[0:length])
    if len(set_list) == length:
        return False
    else:
        return True

class MainWidSetup(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWidSetup, self).__init__()
        # basic setup
        self.setupUi(self)
        self.Buttonlist = []
        self.Buttonlist.append(self.Button_cubic_1)
        self.Buttonlist.append(self.Button_cubic_2)
        self.Buttonlist.append(self.Button_cubic_3)
        self.Buttonlist.append(self.Button_cubic_4)
        self.Buttonlist.append(self.Button_cubic_5)
        self.Buttonlist.append(self.Button_cubic_6)
        self.Buttonlist.append(self.Button_cubic_7)
        self.Buttonlist.append(self.Button_cubic_8)
        self.Buttonlist.append(self.Button_cubic_9)
        self.Buttonlist.append(self.Button_cubic_10)
        self.Buttonlist.append(self.Button_cubic_11)
        self.Buttonlist.append(self.Button_cubic_12)
        self.Buttonlist.append(self.Button_cubic_13)
        self.Buttonlist.append(self.Button_cubic_14)
        self.Buttonlist.append(self.Button_cubic_15)
        self.Buttonlist.append(self.Button_cubic_16)
        self.Buttonlist.append(self.Button_cubic_17)
        self.Buttonlist.append(self.Button_cubic_18)
        self.Buttonlist.append(self.Button_cubic_19)
        self.Buttonlist.append(self.Button_cubic_20)
        self.Buttonlist.append(self.Button_cubic_21)
        self.Buttonlist.append(self.Button_cubic_22)
        self.Buttonlist.append(self.Button_cubic_23)
        self.Buttonlist.append(self.Button_cubic_24)
        self.Buttonlist.append(self.Button_cubic_25)


        self.width = 3
        self.height = 3
        self.isAdjustable = True
        self.isAbleToDisp = False
        self.numlist = [0 for i in range(25)]
        self.usefulnumlist = []
        self.iteration = 0
        self.speed = 500
        self.result = None
        self.timer = QTimer()
        self.algo_type = 0

        ButtonAdjust.HideButton(self,3,3)
        ButtonAdjust.ClearButtonText(self)
        ButtonAdjust.ShiftButton(self,3,3)

        # slots
        # self.Button_init.clicked.connect(self.slot_layer_init)
        self.Button_rand.clicked.connect(self.slot_rand)
        self.Button_calc.clicked.connect(self.slot_calc)
        self.Button_showmove.clicked.connect(self.slot_disp)
        self.spinBox_height.valueChanged.connect(self.slot_spinBox)
        self.spinBox_width.valueChanged.connect(self.slot_spinBox)
        self.timer.timeout.connect(self.slot_timer)
        self.horizontalSlider.valueChanged.connect(self.slot_slider)
        self.comboBox.currentIndexChanged.connect(self.slot_combobox)
        for i in range(25):
            self.Buttonlist[i].clicked.connect(partial(self.slot_click_adjust, i))
            self.Buttonlist[i].rightClicked.connect(partial(self.slot_right_click_adjust, i))



    def slot_spinBox(self):
        self.timer.stop()
        self.Lab_Time.setText('0.0s')
        self.Lab_Step.setText('0')
        self.isAdjustable = True
        self.isAbleToDisp = False
        self.numlist = [0 for i in range(25)]
        self.iteration = 0
        self.usefulnumlist = []
        self.result = None
        width = int(self.spinBox_width.value())
        height = int(self.spinBox_height.value())
        ButtonAdjust.HideButton(self,width,height)
        ButtonAdjust.ClearButtonText(self)
        ButtonAdjust.ShiftButton(self,width,height)

        self.width = width
        self.height = height

    def slot_combobox(self):
        self.algo_type = self.comboBox.currentIndex()

    def slot_slider(self):
        value = self.horizontalSlider.value()
        self.speed = 500/value


    def slot_rand(self):

        if self.isAdjustable:
            ButtonAdjust.RandomSetButton(self, self.width, self.height)
            return


        elif self.isAdjustable == False:
            QMessageBox.warning(self,"警告","不在可调节阶段！", QMessageBox.Ok)
            return


    def slot_click_adjust(self,idx):
        if self.isAdjustable == False:
            return
        self.numlist[idx] = (self.numlist[idx] + 1) % (self.width * self.height)
        ButtonAdjust.SetButtonText(self.Buttonlist[idx], str(self.numlist[idx]))
    
    def slot_right_click_adjust(self,idx):
        if self.isAdjustable == False:
            return
        self.numlist[idx] = (self.numlist[idx] - 1 + self.width * self.height) % (self.width * self.height)
        ButtonAdjust.SetButtonText(self.Buttonlist[idx], str(self.numlist[idx]))
    

    def slot_calc(self):
        width = int(self.spinBox_width.value())
        height = int(self.spinBox_height.value())
        
        if width != self.width or height != self.height:
            QMessageBox.warning(self,"警告","尺寸不匹配，请先点击生成初始界面按钮！", QMessageBox.Ok)
            return
        elif isSameNumInList(self.numlist,self.width*self.height):
            QMessageBox.warning(self,"警告","图中有重复数字或重复空白！", QMessageBox.Ok)
            return
        elif self.isAbleToDisp == True:
            QMessageBox.warning(self,"警告","请点击演示动画按钮观看演示！", QMessageBox.Ok)
            return
        else:
            self.isAdjustable = False
            k = 6*self.height*self.width
            goal = [i for i in range(1, self.width*self.height)]
            goal.append(0)
            if is_trans_successful(self.numlist,goal,self.height,self.width) == False:
                self.isAdjustable = True
                QMessageBox.warning(self,"错误","无法达到目标，请修改！", QMessageBox.Ok)
            else:
                self.usefulnumlist = self.numlist[0:self.height*self.width]
                time1=time.time()
                if self.algo_type == 0:
                    self.result = Astar(self.usefulnumlist,goal,self.height,self.width,k)
                elif self.algo_type == 1:
                    self.result = Faster_Astar(self.usefulnumlist,goal,self.height,self.width,k)
                else:
                    self.result = Astar_algo_DC(self.usefulnumlist,goal,self.height,self.width)
                time2=time.time()
                self.iteration = len(self.result) - 1
                self.Lab_Time.setText('%.2fs' % (time2 - time1))
                self.Lab_Step.setText(str(self.iteration))
                self.isAbleToDisp = True
                QMessageBox.warning(self,"提示","已找到路径！", QMessageBox.Ok)

    def slot_disp(self):
        if self.isAbleToDisp == False:
            QMessageBox.warning(self,"错误","不在显示阶段！", QMessageBox.Ok)
            return
        if self.result == None:
            QMessageBox.warning(self,"错误","不在显示阶段！", QMessageBox.Ok)
            return

        self.timer.start(self.speed)


    def slot_timer(self):
        print(self.iteration)
        if self.iteration == 0:
            self.Lab_Step.setText(str(self.iteration))
            self.Lab_Time.setText('0.0s')
            self.numlist[0:self.height*self.width] = self.usefulnumlist
            self.result = None
            self.isAbleToDisp = False
            self.isAdjustable = True
            self.timer.stop()
            return
        else:
            self.Lab_Step.setText(str(self.iteration))
            next_state = self.result[self.iteration-1]
            zero_pos = 0
            exchange_pos = 0
            for j in range(len(self.usefulnumlist)):
                if self.usefulnumlist[j] != self.result[self.iteration-1][j]:
                    if self.usefulnumlist[j] == 0:
                        zero_pos = j
                    else:
                        exchange_pos = j

            ButtonAdjust.exchange(self, zero_pos, exchange_pos)
            self.usefulnumlist = self.result[self.iteration-1]
            self.iteration = self.iteration - 1
            self.Lab_Step.setText(str(self.iteration))
            self.timer.start(self.speed)



        