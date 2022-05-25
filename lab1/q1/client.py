from socket import *

serverName = '10.59.100.199'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Enter message: ')
clientSocket.sendto(message.encode(),(serverName, serverPort))

reply, serverAddress = clientSocket.recvfrom(2048)
print('Server says: ', reply.decode())

clientSocket.close()