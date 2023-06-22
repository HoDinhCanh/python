'Chat Room Connection - Client-To-Client'
import threading
import socket
import sys
import time

import yfinance as yf
host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []

msft = yf.Ticker("BBJP")
print(msft.info)
# def info():
#     broadcast(f'{msft.info}'.encode('utf-8'))
#     time.sleep(5)
def broadcast(message):
    for client in clients:
        client.send(message)


# Function to handle clients'connections


def handle_client(client):
    while True:
        try:
            # message = client.recv(1024)
            message = msft.info
            broadcast(message)
            print(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)
            break


# Main function to receive the clients connection
def receive():
    while True:
        print('Server is running and listening ...')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected to the server'.encode('utf-8'))
        client.send('you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()



if __name__ == "__main__":
    receive()