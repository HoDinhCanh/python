import socket
import struct
import sys

multicast_group = '224.0.0.1'
server_address = ('', 10000)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
listclient = []
# Bind to the server address
sock.bind(server_address)
# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


def send(data, client):
    try:
        s = data.decode('utf-8')
        message = s
        s = s.replace("{('", "")
        arr = []
        arr = s.split(")}")
        listaddres = []

        arr[0] = arr[0].replace("'", "")
        listaddres = arr[0].split(",")
        addre = listaddres[0], int(listaddres[1])
        message = "{" + str(client) + "}" + arr[1]
        for i in listclient:
            if i == addre:
                sock.sendto(message.encode('utf-8'), i)

    except:
        data = str(client) + " " + data.decode('utf-8')
        for i in listclient:
            if i != client:
                sock.sendto(data.encode('utf-8'), i)


def sendclient(client):
    sock.sendto(b"login_client_new", client)
    for i in listclient:
        if i != client:
            sock.sendto(b"login_client_new", i)
            sock.sendto(str(client).encode('utf-8'), i)
            sock.sendto(b"end_client_new", i)
            sock.sendto(str(i).encode('utf-8'), client)

    sock.sendto(b"end_client_new", client)


while True:
    data, address = sock.recvfrom(10240)

    if not (address in listclient):
        sendclient(address)
        listclient.append(address)


    else:
        send(data, address)


