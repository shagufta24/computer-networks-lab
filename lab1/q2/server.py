from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive!')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    nums = eval(message.decode())
    print('Received numbers: ', nums)

    dedup_nums = []
    dups = []
    for n in nums:
        if n not in dedup_nums:
            dedup_nums.append(n)
        else:
            dups.append(n)

    serverSocket.sendto(str(dedup_nums).encode(), clientAddress)
    serverSocket.sendto(str(dups).encode(), clientAddress)

