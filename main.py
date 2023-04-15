address = "DE:CC:4C:D5:7A:99"

import asyncio
import struct
# import pickle
import logging
from pprint import pp
from datetime import datetime

from bleak import BleakScanner

timeout_seconds = 10
address_to_look_for = address

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def detection_callback(device, advertisement_data):
    if device.address == address_to_look_for:
        pp(advertisement_data.manufacturer_data[65527][1] / 4.0)
        logger.info(str(int(advertisement_data.manufacturer_data[65527][0] - 160)/ 4.0) + " " + str(int(advertisement_data.manufacturer_data[65527][1] - 160) / 4.0) + " " + str(int(advertisement_data.manufacturer_data[65527][2] - 160) / 4.0))
        

async def run():
    scanner = BleakScanner()
    scanner.register_detection_callback(detection_callback)
    await scanner.start()
    await asyncio.sleep(timeout_seconds)
    await scanner.stop()

if __name__=='__main__':    
    loop = asyncio.get_event_loop()
    while True:
        loop.run_until_complete(run())