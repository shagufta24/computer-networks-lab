Lab Assignment 3 - Error Detection and Correction

To run:
python server.py
python client.py

Note: Please use python 3 to run the codes.

Input:
client.py - Enter the value of N to generate the NxN matrix.

Output:
server.py - Prints the original received message, the error location and the corrected message.

Logic:
On the client's side, an NxN matrix of 0s and 1s is randomly generated. The row-wise and column-wise parity bits are computed and added to the matrix. Then, an error is introduced by randomly flipping one of the bits. The matrix is encoded as a message and sent to the server.

The server, on receiving the message, decodes it and checks if each row and column has an even parity. Based on this, it detects the exact position of the bit error and corrects it by reversing the bit.