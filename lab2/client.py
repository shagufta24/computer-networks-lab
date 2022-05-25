from socket import *
import random

serverName = '10.59.107.188'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

def even(n):
    if n%2==0: return True
    return False

N = int(input('Enter the value of N: '))
if (N <= 0):
    print("Invalid value of N")
    exit()
    
matrix=[]
for i in range(N):
    row = []
    for j in range(N):
        row.append(random.randint(0,1))
    matrix.append(row)



# Adding row parities
for row in matrix:
    if even(row.count(1)) == False:
        row.append(1)
    else: row.append(0)

# Adding column parities
col_par = []
for i in range(N+1):
    col = []
    for row in matrix:
        col.append(row[i])
    if even(col.count(1)) == False:
        col_par.append(1)
    else: col_par.append(0)
matrix.append(col_par)

# Introduce error bit
error_row = random.randint(0,N)
error_col = random.randint(0,N)

if matrix[error_row][error_col] == 0:
    matrix[error_row][error_col] = 1
else:
     matrix[error_row][error_col] = 0

matrix = str(matrix)
clientSocket.sendto(matrix.encode(),(serverName, serverPort))

reply, serverAddress = clientSocket.recvfrom(2048)
print('Message Received: ', reply.decode())

clientSocket.close()