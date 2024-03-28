import socket


def port_scan(host, port):
    try:
        s = socket.socket()
        s.connect((host, port))
        return True
    except:
        return False


host = input("Enter IP : ")
start_port = int(input("Enter First Port : "))
end_port = int(input("Enter Last Port : "))

for port in range(start_port, end_port+1):
    if port_scan(host, port):
        print("Port", port, "Open")
    else:
        print("Port", port, "Closed")
