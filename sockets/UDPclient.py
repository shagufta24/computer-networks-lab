# The socket module is used for network communications
from socket import *

# servername - Either the IP address or the hostname of the server. DNS lookup will get IP address from hostname.
serverName = '10.59.100.199' #'10.0.0.5'
serverPort = 12000

# Creating the client’s socket
# AF_INET - Address family. INET means the network is using IPv4.
# SOCK_DGRAM - The socket type (UDP socket). 
# We don't specify the port number of the client socket, the OS does that.
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Enter message:')

# Send the message through the socket to the destination host
# encode() converts the message from string type to byte type
# sendto() attaches the destination address (serverName, serverPort) to the message and 
# sends the resulting packet into the clientSocket.
# the source address is also automatically attached to the packet 
clientSocket.sendto(message.encode(),(serverName, serverPort))

# the client waits to receive data from the server
# the packet data is put in modifiedMessage 
# the packet’s source address is put in serverAddress
reply, serverAddress = clientSocket.recvfrom(2048)

# decode() converts the message from bytes to string
# The text should now be capitalized
print('Received: ', reply.decode())
clientSocket.close()