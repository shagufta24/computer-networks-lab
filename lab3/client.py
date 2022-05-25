from socket import *
import random
import binascii

serverName = '10.59.107.188' #'10.0.0.13'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

def str_to_bits(word):
    return [[int(i) for i in bin(ord(c))[2:]] for c in word]

def even(n):
        if n%2==0: return True
        return False

words = "Find your passion and success will find you"
words = words.split()
for message in words:
    matrix = str_to_bits(message)

    N = len(matrix)
    M = len(matrix[0])

    # Adding row parities
    for row in matrix:
        if even(row.count(1)) == False:
            row.append(1)
        else: row.append(0)

    # Adding column parities
    col_par = []
    for i in range(M+1):
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

    clientSocket.sendto(str(matrix).encode(),(serverName, serverPort))

    reply, serverAddress = clientSocket.recvfrom(2048)
    print('Server says: ', reply.decode())

clientSocket.close()