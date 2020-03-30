import os
import sys 
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
 
def main(): 
    app = QApplication(sys.argv) 
    w = MyWindow() 
    w.show() 
    sys.exit(app.exec_()) 
 
class MyWindow(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args) 
 
  
        label = QLabel(self.tr("Enter the key to display boot options passed to the kernel with short description of each"))
        self.le = QLineEdit()
        self.te = QTextEdit()

 
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.le)
        layout.addWidget(self.te)
        self.setLayout(layout) 


        self.connect(self.le,SIGNAL("returnPressed(void)"),
                     self.run_command)

    def run_command(self):
        cmd = 'cat /proc/cmdline'
        stdouterr = os.popen4(cmd)[1].read()
        self.te.setText(stdouterr)
    #def home(self):
       # btn =QtGui.QPushButton("Quit", self)
       #	btn.clicked.connect(self.close_application)
       	#btn.resize(btn.minimumSizeHint())
       	#btn.move(0,0)
     	#self.show()
    #def close_application(self):   #if QWidget install in PyQt4 exit button from elearn reference
     #   print("thank you!!!")
      #  sys.exit()
  
if __name__ == "__main__": 
    main()

