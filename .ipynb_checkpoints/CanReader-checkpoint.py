import can 
import time
class CanReader:
    def __init__(self, msg):
        self.msg=msg
        #self.bus=can.interface.Bus(channel="can0", bustype="socketcan")
        #self.msg=self.bus.recv()
        #self.timestamp=time.strftime("%H: %M: %S", time.localtime())
        #self.arb_id=hex(msg.arbitration_id)
        #self.data_hex=msg.data.hex()
    def getTime(self):
        timestamp=time.strftime("%H: %M: %S", time.localtime())
        return timestamp
    def get_id(self):
        arb_id=hex(self.msg.arbitration_id)
        return arb_id
       
    def get_hex(self):
        data_hex=self.msg.data.hex()
        return data_hex
       
    def __str__(self):
        #print(f"[{timestamp}] ID={arb_id} Data={data_hex.upper()}")
        return f"[{self.getTime()}] ID={self.get_id()} Data={self.get_hex().upper()}"
