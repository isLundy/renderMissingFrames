import os
from PySide2.QtWidgets import (QWidget, QLineEdit, QPushButton, QApplication,
                QLabel, QHBoxLayout, QVBoxLayout, QDesktopWidget)
from PySide2.QtGui import QCursor
from PySide2.QtCore import Qt

class MissingFrames(QWidget):
    def __init__(self):
        super(MissingFrames, self).__init__()

        self.node = nuke.selectedNode()
        self.node.selectOnly()

        if self.node.Class() == 'Write':
            self.setUI()
            self.setPZ()
            self.show()

    def setUI(self):
            self.nodeLabel = QLabel(self.node.name())

            self.rangeLabel = QLabel('Frame range')
            self.startText = QLineEdit()
            self.startText.setText(str(int(nuke.root()['first_frame'].getValue())))
            self.toLabel = QLabel('-')
            self.endText = QLineEdit()
            self.endText.setText(str(int(nuke.root()['last_frame'].getValue())))
            self.checkButton = QPushButton('Checking')

            self.mfLabel = QLabel('Missing Frames')
            self.mfText = QLineEdit()
            self.mfText.setReadOnly(True)
            self.checkButton.clicked.connect(self.checking)

            self.renderButton = QPushButton('Render the Missing Frames')
            self.renderButton.clicked.connect(self.close)

            hbox = QHBoxLayout()
            hbox.addWidget(self.nodeLabel)
            hbox.addWidget(self.rangeLabel)
            hbox.addWidget(self.startText)
            hbox.addWidget(self.toLabel)
            hbox.addWidget(self.endText)
            hbox.addWidget(self.checkButton)
            hbox.addWidget(self.mfLabel)
            hbox.addWidget(self.mfText)
            hbox.addStretch()

            vbox = QVBoxLayout()
            vbox.addStretch()
            vbox.addLayout(hbox)
            vbox.addStretch()
            vbox.addWidget(self.renderButton)

            self.setLayout(vbox)

    def setPZ(self):
        self.setWindowTitle('Missing Frames')
        self.resize(1200, 200)

        qr = self.frameGeometry()
        screenCenter = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(screenCenter)
        self.move(qr.topLeft())
        
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def missingFrames(self):
        frameNum = self.node['file'].getValue().split('.')[-2]
        evalStr = self.node['file'].evaluate().rsplit('.', 2)
        seq = '%s.%s.%s'%(evalStr[0], frameNum, evalStr[-1])
        print(frameNum)
        print(evalStr)
        print(seq)

        self.frames = []
        for frame in range(self.start, self.end+1):
            file = seq%frame
            if not os.path.exists(file):
                self.frames.append(frame)

        self.missingNums = ''
        if self.frames:
            for frame in self.frames:
                if frame-1 in self.frames:
                    if frame-2 in self.frames:
                        self.missingNums = self.missingNums.replace(str(frame-1), str(frame))
                    else:
                        self.missingNums += '-%s'%frame
                else:
                    self.missingNums += ' %s'%frame

    def checking(self):
        self.start = int(self.startText.text())
        self.end = int(self.endText.text())
        self.missingFrames()
        self.mfText.setText(self.missingNums)

mf = MissingFrames()
