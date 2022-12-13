import socket

port = 5050
host = socket.gethostbyname(socket.gethostname())  # gets IP address of whatever machine runs the program
address = (host, port)
FORMAT = 'utf-8'  # Unicode Transformation Format needed to convert message into bytes

recSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creates socket for streaming internet connection
recSocket.bind(address)  # create connection between socket and machine's IP address


def deliver_data(message):  # Prints message to terminal
    print(message)


def extract(conn):  # extracts information from connection
    while True:
        message = conn.recv(1024).decode(FORMAT)  # receives message no larger than 1024 bytes
        deliver_data(message)
        break

    recSocket.close()
    exit()

def rdt_recv():
    recSocket.listen(1)  # allows exactly 1 connection
    while True:
        conn, addr = recSocket.accept()  # forms new connection between sender and receiver
        print("New connection from: ", str(addr))
        extract(conn)


print("Receiver is listening to", str(host))
rdt_recv()
