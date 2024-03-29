# -*- coding: utf-8 -*-
#!/usr/bin/python
#Box布局
import sys
from PyQt4 import QtGui
class Boxlayout(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle('box layout')
        ok = QtGui.QPushButton('OK')
        cancel = QtGui.QPushButton('Cancel')
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(ok)
        hbox.addWidget(cancel)
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.resize(300, 150)
app = QtGui.QApplication(sys.argv)
qb = Boxlayout()
qb.show()
sys.exit(app.exec_())