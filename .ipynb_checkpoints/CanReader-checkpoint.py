import can 
import time
class CanReader:
    def __init__(self):
        self.bus=can.interface.Bus(channel="can0", bustype="socketcan")
        self.msg=self.bus.recv()
        self.timestamp=time.strftime("%H: %M: %S", time.localtime())
        self.arb_id=hex(msg.arbitration_id)
        self.data_hex=msg.data.hex()
    def getTime(self):
       return self.timestamp
    def get_id(self):
       return self.arb_id
    def get_hex(self):
       return self.data_hex
    def __str__(self):
        #print(f"[{timestamp}] ID={arb_id} Data={data_hex.upper()}")
        return f"[{self.timesamp}] ID={self.arb_id} Data={self.data_hex.upper()}"
