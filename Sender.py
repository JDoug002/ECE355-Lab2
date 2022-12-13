import socket
import time

port = 5050
host = socket.gethostbyname(socket.gethostname())  # gets IP address of whatever machine runs the program
address = (host, port)
FORMAT = 'UTF-8'  # Unicode Transformation Format needed to convert message into bytes

sendSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creates socket for streaming internet connection
sendSocket.connect(address)  # create connection between Receiver socket and Sender socket


def wait():  # Includes 1 second delay to simulate delay
    time.sleep(1)


def udt_send(packet):  # Send message over UDP to receiver
    sendSocket.send(packet)
    sendSocket.close()
    wait()


def make_pkt(message):  # Creates packet to be sent from message
    packet = message.encode(FORMAT)
    udt_send(packet)


def rdt_send(message):  # Sends message to receiver
    make_pkt(message)


rdt_send("Testing rdt1.0 protocol")
