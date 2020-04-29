import serial
import time
ser = serial.Serial("/dev/ttyS0",115200)

W_buff = ["ATT+CGNSPWR=1\r\n", "AT+CGNSSEQ=\"RMC\"\r\n", "AT+CGNSINF\r\n"]

ser.write(W_buff)
time.sleep(0.5)
