import serial
import time
import logging

def write_file(path):
    logging.basicConfig(level=logging.NOTSET)  # Here
    logging.info("Sending file " + path)
    ser = serial.Serial('/dev/ttyUSB0', 250000)
    file = open(path, 'r')

    for line in file:
        ser.write(str.encode(line))
        logging.info("Sent line " + line)
        time.sleep(1)
        continue
        for i in range(0, 100000):
            line = ser.readline()
            logging.info("Got answer: " + str(line))

            if line == b'ok\n':
                break
    ser.close()
