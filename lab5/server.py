# First, install pyftpdlib using
# python3 -m pip install pyftpdlib

from pyftpdlib import servers
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler

from os.path import isdir
from os import makedirs

# IP address and port number to listen on
address = ("127.0.0.1", 2000)

# Root directory for the server
server_root = './server_files'

if __name__ == "__main__":

	# If server root directory does not exist, create it
	if not isdir(server_root):
		makedirs(server_root)
		
	authorizer = DummyAuthorizer()
	# Anonymous user
	authorizer.add_anonymous(server_root, perm='elradfmwMT')

	handler = FTPHandler
	handler.authorizer = authorizer

	# create server
	server = servers.FTPServer(address, handler)
	server.serve_forever()