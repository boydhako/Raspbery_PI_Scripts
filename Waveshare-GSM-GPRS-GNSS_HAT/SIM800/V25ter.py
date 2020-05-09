import serial
import time

class V25ter():
    def __init__(self, command):
        self.run = command

    def run(self):
        print(self.run)
