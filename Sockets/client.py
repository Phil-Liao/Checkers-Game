import socket
import threading

class network:
    def __init__(self):
        self.HEADER = 64
        self.PORT = 5050
        self.FORMAT = "utf-8"
        self.DISCONNECT_MESSAGE = "!Disconnected!"
        self.SERVER = "192.168.0.104"
        self.ADDR = (self.SERVER, self.PORT)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
        self.receive_message = ""

    def send(self, msg):
        thread = threading.Thread(target = network.receive, args = (self.receive_message))       
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
    
    def receive(self, receive_message):
        pass

