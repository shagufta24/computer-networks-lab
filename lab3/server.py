from socket import *
import binascii

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive!')

def bits_to_str(matrix):
    w = str()
    for row in matrix:
        s = str()
        for i in row:
            s=s+str(i)
        char = int(s, 2)
        w = w + chr(char)
    return w

def remove_parity(matrix):
    matrix = matrix[:-1]
    for i in range(len(matrix)):
        matrix[i] = matrix[i][:-1]
    return matrix

def even(n):
        if n%2==0: return True
        return False

while True:
    string, clientAddress = serverSocket.recvfrom(2048)
    matrix = eval(string.decode())
    N = len(matrix)
    M = len(matrix[0])

    stripped_matrix = remove_parity(matrix)
    message = bits_to_str(stripped_matrix)
    print('Received message: ', message)
    
    # Check for row error
    row_index = 0
    for row in matrix:
        if even(row.count(1)) == False:
            error_row = row_index
            break
        row_index +=1
    # Check for column parity
    for i in range(N+1):
        col = []
        for row in matrix:
            col.append(row[i])
        if even(col.count(1)) == False:
            error_col = i
            break

    # Correct error
    if matrix[error_row][error_col] == 0:
        matrix[error_row][error_col] = 1
    else:
        matrix[error_row][error_col] = 0
    
    print('Error detected at position: ', error_row, error_col)

    corrected_matrix = remove_parity(matrix)
    corrected_message = bits_to_str(corrected_matrix)
    print('Corrected message: ', corrected_message, '\n')

    reply = 'Error detected and corrected. Received: ' + corrected_message
    serverSocket.sendto(reply.encode(), clientAddress)

