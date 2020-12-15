from PySide2 import QtWidgets
from numpy import floor

class QPushButton_Widget(QtWidgets.QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.audiobuffer = None

        self.setObjectName("QPushButton_Widget")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.button = QtWidgets.QPushButton("Click me!")

        self.gridLayout.addWidget(self.button, 0, 0, 1, 1)

    def set_buffer(self, buffer):
        self.audiobuffer = buffer
        self.old_index = self.audiobuffer.ringbuffer.offset

    def handle_new_data(self, floatdata):
        # we need to maintain an index of where we are in the buffer
        index = self.audiobuffer.ringbuffer.offset

        available = index - self.old_index

        if available < 0:
            # ringbuffer must have grown or something...
            available = 0
            self.old_index = index

        # if we have enough data to add a frequency column in the time-frequency plane, compute it
        needed = self.fft_size * (1. - self.overlap)
        realizable = int(floor(available / needed))

        if realizable > 0:
            pass