import RPi.GPIO as GPIO
import sys
import time
import serial

ser = serial.Serial(
   port='/dev/ttyS0',
   baudrate=115200
)

cmd = sys.argv[1]

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.IN)
GPIO.setup(7, GPIO.OUT)
pin7 = GPIO.input(7)
ser = bytes("AT+CGNSPWR=1\r\nAT+CGNSSEQ=\"RMC\"\r\nAT+CGINSF\r\nAT+CGNSURC=2\r\nAT+CGNSTST=1\r\n", "utf-8")

if cmd == "off":
	GPIO.output(7, GPIO.LOW)
	time.sleep(4)
elif cmd == "on":
	GPIO.output(7, GPIO.HIGH)
	time.sleep(4)
if pin7 == 1:
    pin7mode = "off"
#   GPIO.output(7, GPIO.LOW)
#   time.sleep(4)
elif pin7 == 0:
    pin7mode = "on"
#   GPIO.output(7, GPIO.HIGH)

print(pin7mode)
#ser.isOpen()
#ser.write()
time.sleep(4)


GPIO.cleanup()
