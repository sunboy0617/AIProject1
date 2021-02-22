import sys,os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from UIrelated import MainWidSetup

from PyQt5 import QtWidgets

app=QtWidgets.QApplication(sys.argv)
ui = MainWidSetup()    
ui.show()
sys.exit(app.exec_())
