import can
import time
import pyqtgraph as pg
from PyQt6 import QtWidgets 
from pyqtgraph.Qt import QtGui

app = QtWidgets.QApplication([])
win = pg.GraphicsLayoutWidget(show=True, title="CAN Bus Live Data")
plot = win.addPlot(title="Speed over Time")
curve = plot.plot(pen='y')
data_points = []

bus = can.interface.Bus(channel="can0", interface="socketcan")

while True:
    msg = bus.recv()
    if msg:
        value = int.from_bytes(msg.data, byteorder='big')
        data_points.append(value)
        if len(data_points) > 100:
            data_points.pop(0)
        curve.setData(data_points)
        QtGui.QApplication.processEvents()
