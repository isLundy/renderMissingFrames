import os
from PySide2.QtWidgets import (QWidget, QLineEdit, QPushButton, QApplication,
                QLabel, QHBoxLayout, QVBoxLayout, QDesktopWidget)
from PySide2.QtGui import QCursor
from PySide2.QtCore import Qt

class MissingFrames(QWidget):
    def __init__(self, start, end):
        super(MissingFrames, self).__init__()

        self.node = nuke.selectedNode()
        self.node.selectOnly()

        self.start = start
        self.end = end

        if self.node.Class() == 'Write':
            self.setUI()
            self.setPZ()
            self.show()

    def setUI(self):
        nodeLabel = QLabel(self.node.name())
        mfLabel = QLabel('Missing Frames')

        mfText = QLineEdit()
        mfText.setText(self.missingFrames())
        mfText.setReadOnly(True)

        renderButton = QPushButton('Render the Missing Frames')
        renderButton.clicked.connect(self.close)

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(mfLabel)
        hbox.addWidget(mfText)
        hbox.addStretch()

        vbox = QVBoxLayout()
        vbox.addWidget(nodeLabel)
        vbox.addStretch()
        vbox.addLayout(hbox)
        vbox.addStretch()
        vbox.addWidget(renderButton)


        self.setLayout(vbox)

    def missingFrames(self):
        frameNum = self.node['file'].getValue().split('.')[-2]
        evalStr = self.node['file'].evaluate().rsplit('.', 2)
        seq = '%s.%s.%s'%(evalStr[0], frameNum, evalStr[-1])
        print(frameNum)
        print(evalStr)
        print(seq)

        frames = []
        for frame in range(self.start, self.end+1):
            file = seq%frame
            if not os.path.exists(file):
                frames.append(frame)

        nums = ""
        if frames:
            for frame in frames:
                if frame-1 in frames:
                    if frame-2 in frames:
                        nums = nums.replace(str(frame-1), str(frame))
                    else:
                        nums += '-%s'%frame
                else:
                    nums += ' %s'%frame
        print(nums)

        return nums.strip()

    def setPZ(self):
        self.setWindowTitle('Missing Frames')
        self.resize(600, 200)

        qr = self.frameGeometry()
        screenCenter = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(screenCenter)
        self.move(qr.topLeft())
        
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

mf = MissingFrames(1001, 1179)
