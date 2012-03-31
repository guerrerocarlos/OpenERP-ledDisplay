import serial
import eventlet
from eventlet import wsgi
import httplib
import ftplib
import urllib
import SocketServer
import BaseHTTPServer


class PosDisplay(object):
    def __init__(self):
        self.ser = serial.Serial(0)
    
    def bridge(self, env, start_response):
        self.ser.write(" "*42)
        linea1,linea2 = env['PATH_INFO'][1:].split("___")
        self.ser.write("\r"+linea1[:19]+"\n\r"+" "*(20-len(linea2))+linea2)
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return ['OK\r\n']

    def run(self):
        wsgi.server(eventlet.listen(('', 8100)), self.bridge)
        self.ser.close()

if __name__ == "__main__":
    pos_display = PosDisplay()
    pos_display.run()
