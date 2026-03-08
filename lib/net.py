import network
from time import sleep
from wifi_settings import *
from network import *
import usocket

class Wifi:
    def __init__(self):
        pass
    
    def connect(self):
        #Connect to WLAN
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        while wlan.isconnected() == False:
            print(f'Waiting for connection to {WIFI_SSID}...')
            sleep(1)
            
        self.host = wlan.ifconfig()[0]
        print("IP Address", self.host)
        
        mac = wlan.config('mac')
        print("MAC Address:", [hex(i) for i in mac])
        
        return self.host
    
    def startWifiAccessPoint(self, ap_ssid, ap_password):
        
        ap = network.WLAN(network.AP_IF)
        ap.config(essid=ap_ssid, password=ap_password)
        ap.active(True)
        while ap.active() == False:
            pass
        
        self.host = ap.ifconfig()[0]

        # Show access point settings
        print("Access point created with SSID: {}, password: {}".format(ap_ssid, ap_password))

        self.host = ap.ifconfig()[0]
        print("IP Address", self.host)
        
        mac = ap.config('mac')
        print("MAC Address:", [hex(i) for i in mac])
        
        return self.host
    
    def createReceiver(self, port):
        # Create socket bound to a port
        print("\nCreate UDP Server socket")
        self.socket = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
        self.socket.settimeout(None)
        self.socket.bind((str(self.host), port))       
    

    def receiveMessage(self):
        MAXBUF = 256
        data, addr = self.socket.recvfrom(MAXBUF)
        message = data.decode()
        return message
    
    def createSender(self, host, port):
        # Create socket bound to a port
        print("\nCreate UDP Server socket")
        self.socket = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
        self.socket.settimeout(None)

        self.host = host
        self.port = port
        
        
    def sendMessage(self, message):
        size = self.socket.sendto(str.encode(message), (self.host, self.port))
        return size
    
    
    def closeSocket(self):
        self.socket.close()