from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive!')

def print_matrix(matrix):
    for row in matrix:
        print(row)

def even(n):
        if n%2==0: return True
        return False

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    matrix = eval(message.decode())
    print('Received message: ')
    print_matrix(matrix)
    
    N = len(matrix[0]) - 1
    
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
    print('Corrected message: ')
    print_matrix(matrix)

    reply = 'Error detected and corrected.'
    serverSocket.sendto(reply.encode(), clientAddress)

