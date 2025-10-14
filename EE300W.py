import can 
import time

def main():
    bus = can.interface.Bus(channel="can0", bustype="socketcan")
    
    print( "CAN bus demo: Listening for messages...\n")

    try:
        while True:
            msg = bus.recv()
            if msg: 
                timestamp = time.strftime("%H: %M: %S", time.localtime())
                arb_id = hex(msg.arbitration_id)
                data_hex = msg.data.hex()

                print(f"[{timestamp}] ID={arb_id} Data={data_hex.upper()}")
    except KeyboardInterrupt:
        print("\nStopped CAN listener.")

if __name__ == "__main__":
    main()
