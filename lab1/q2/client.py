from socket import *
import random

serverName = '10.59.100.199'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

N = random.randint(25, 100)
nums = []
for i in range(N):
    nums.append(random.randint(1, 100))

clientSocket.sendto(str(nums).encode(),(serverName, serverPort))

dedup_nums, serverAddress = clientSocket.recvfrom(2048)
dups, serverAddress = clientSocket.recvfrom(2048)

dedup_nums.decode()

print('De-duplicated numbers: ',eval(dedup_nums), '\n')
print('Duplicates removed: ', eval(dups))

clientSocket.close()