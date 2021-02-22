from PyQt5 import QtCore, QtGui, QtWidgets
from random import shuffle


def HideButton(mainwindow,width,height):
    for i in range(25):
        if i < width * height :
            mainwindow.Buttonlist[i].setVisible(True) 
        else :
            mainwindow.Buttonlist[i].setVisible(False)

def ClearButtonText(mainwindow):
    for i in range(25):
        mainwindow.Buttonlist[i].setText("")
        mainwindow.Buttonlist[i].setStyleSheet("QPushButton{\n"
"    background:rgba(87,96,105,80);\n"
"    border: 5px groove rgba(111, 255, 212, 50);\n"
"    border-radius:20px;\n"
"    color: rgb(255,255, 255);\n"
"    selection-background-color: rgba(255,255,255,80);\n"
"    border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgba(140, 154, 168,80); \n"
"    border-style: inset;\n"
"}")


def ShiftButton(mainwindow,width,height):
    startpos = (360 - 60*width, 390 - 60 * height)
    for i in range(width * height):
        mainwindow.Buttonlist[i].setGeometry(QtCore.QRect(int(startpos[0]+int(120) * (i%width)), 
            int(startpos[1]+int(120) * int(i/width)),120,120))


def SetButtonText(buttonname, text):
    if text == '0':
        buttonname.setStyleSheet("QPushButton{\n"
"    background:rgba(255,255,255,80);\n"
"    border: 5px groove rgba(111, 255, 212, 50);\n"
"    border-radius:20px;\n"
"    color: rgb(255,255, 255);\n"
"    selection-background-color: rgba(255,255,255,80);\n"
"    border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgba(140, 154, 168,80); \n"
"    border-style: inset;\n"
"}")
        buttonname.setText("")
    else:
        buttonname.setStyleSheet("QPushButton{\n"
"    background:rgba(87,96,105,80);\n"
"    border: 5px groove rgba(111, 255, 212, 50);\n"
"    border-radius:20px;\n"
"    color: rgb(255,255, 255);\n"
"    selection-background-color: rgba(255,255,255,80);\n"
"    border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgba(140, 154, 168,80); \n"
"    border-style: inset;\n"
"}")
        buttonname.setText(text)


def RandomSetButton(mainwindow,width,height):
    temp_list = list(range(width*height))
    shuffle(temp_list)
    for i in range(width*height):
        SetButtonText(mainwindow.Buttonlist[i],str(temp_list[i]))
        mainwindow.numlist[i] = temp_list[i]


def exchange(mainwindow, idx_zero, idx_exchange):
    text1 = mainwindow.usefulnumlist[idx_exchange]
    SetButtonText(mainwindow.Buttonlist[idx_exchange],str(0))
    SetButtonText(mainwindow.Buttonlist[idx_zero],str(text1))
    mainwindow.Buttonlist[idx_exchange].setStyleSheet("QPushButton{\n"
"    background:rgba(255,255,255,80);\n"
"    border: 5px groove rgba(111, 255, 212, 50);\n"
"    border-radius:20px;\n"
"    color: rgb(255,255, 255);\n"
"    selection-background-color: rgba(255,255,255,80);\n"
"    border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgba(140, 154, 168,80); \n"
"    border-style: inset;\n"
"}")
    mainwindow.Buttonlist[idx_zero].setStyleSheet("QPushButton{\n"
"    background:rgba(87,96,105,80);\n"
"    border: 5px groove rgba(111, 255, 212, 50);\n"
"    border-radius:20px;\n"
"    color: rgb(255,255, 255);\n"
"    selection-background-color: rgba(255,255,255,80);\n"
"    border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgba(140, 154, 168,80); \n"
"    border-style: inset;\n"
"}")
    

