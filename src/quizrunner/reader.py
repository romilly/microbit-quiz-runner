from abc import ABCMeta, abstractmethod

import serial
import microfs
import io


class Reader(metaclass=ABCMeta):
    @abstractmethod
    def readline(self):
        pass


class SerialReader(Reader):
    def __init__(self):
        port = microfs.find_microbit()[0]
        baud = 115200
        s = serial.Serial(port, timeout=0)
        s.baudrate = baud
        self._reader =  io.BufferedReader(s)

    def readline(self):
        return self._reader.readline()


class MockReader(Reader):
    def __init__(self):
        self.lines = []

    def add(self, *lines):
        for line in lines:
            self.lines.append(line)

    def readline(self):
        if len(self.lines) > 0:
            return self.lines.pop(0)
        return ''

