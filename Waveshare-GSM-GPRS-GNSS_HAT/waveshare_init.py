import RPi.GPIO as GPIO
import serial
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
ser = serial.Serial("/dev/ttyS0", 115200)

#W_buff = ["AT+CGNSPWR=1\r\n", "AT+CSTT=\"RESELLER\"\r\n", "AT+CSGS=2\r\n", "AT+CGATT=1\r\n", "AT+CGNSSEQ=\"RMC\"\r\n", "AT+SAPBR=3,1,\"CONTYPE\",\"GPRS\"\r\n", "AT+SAPBR=3,1,\"APN\",\"3GNET\"\r\n", "AT+SAPBR=1,1\r\n", "AT+SAPBR=2,1\r\n", "AT+CNTPCID=1\r\n", "AT+CNTP\r\n", "AT+CCLK?\r\n", "AT+CLBS=1,1\r\n", "AT+FTPSERV=\"116.247.119.165\"\r\n", "AT+FTPUN=\"customer\"\r\n", "AT+FTPPW=\"111111\"\r\n", "AT+FTPGETNAME=\"MTK3.EPO\"\r\n", "AT+FTPGETPATH=\"/\"\r\n", "AT+FTPEXTGET=1\r\n", "AT+FTPEXTGET=4,\"epo\"\r\n", "AT+FSLS=C:\\User\\\r\n", "AT+CGNSCHK=3,1\r\n", "AT+CGNSPWR=1\r\n", "AT+CGNSAID=31,1,1\r\n", "AT+CGNSINF\r\n", "AT+CGNSURC=2\r\n", "AT+CGNSTST=1\r\n"]
W_buff = ["AT+CGNSPWR=1\r\n", "AT+CSTT=\"RESELLER\"\r\n", "AT+CSGS=2\r\n", "AT+CGATT=1\r\n", "AT+CGNSSEQ=\"RMC\"\r\n", "AT+SAPBR=3,1,\"CONTYPE\",\"GPRS\"\r\n", "AT+SAPBR=3,1,\"APN\",\"3GNET\"\r\n", "AT+SAPBR=1,1\r\n", "AT+SAPBR=2,1\r\n", "AT+CNTPCID=1\r\n", "AT+CNTP\r\n", "AT+CCLK?\r\n", "AT+CLBS=1,1\r\n", "AT+FTPSERV=\"116.247.119.165\"\r\n", "AT+FTPUN=\"customer\"\r\n", "AT+FTPPW=\"111111\"\r\n", "AT+FTPGETNAME=\"MTK3.EPO\"\r\n", "AT+FTPGETPATH=\"/\"\r\n", "AT+FTPEXTGET=1\r\n", "AT+FTPEXTGET=4,\"epo\"\r\n", "AT+FSLS=C:\\User\\\r\n", "AT+CGNSCHK=3,1\r\n", "AT+CGNSPWR=1\r\n", "AT+CGNSAID=31,1,1\r\n", "AT+CGNSINF\r\n", "AT+CGNSURC=2\r\n", "AT+CGNSTST=2\r\n"]




ser.write(W_buff[0])
ser.flushInput()
data = ""
num = 0

try:
    while True:
        GPIO.output(7, GPIO.LOW)
        time.sleep(0.75)
        break
    while True:
        while ser.inWaiting() > 0:
            data += ser.read(ser.inWaiting())
        if data != "":
            print data
            time.sleep(0.5)
            ser.write(W_buff[num+1])
            num = num+1
            if num == 4:
                time.sleep(0.5)
                ser.Write(W_buff[4])
            data = ""
except keyboardInterrupt:
    if ser != None:
        ser.close()

GPIO.cleanup()
