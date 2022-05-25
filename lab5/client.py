from ftplib import FTP
from os import system, remove
from os.path import basename

HOST = "localhost"
PORT = 2000

def show_files(ftp):
	files = []
	ftp.dir(files.append)
	print("Server file directory: ")
	for file in files:
		print(file)

def upload(ftp, path):
	try:
		with open(path, "rb") as inFPtr:
			ftp.storbinary(f"STOR {basename(path)}", inFPtr)
		print(f"Uploaded {basename(path)} successfully.")

	except Exception as e:
		print(f"Failed to perform operation: {e}. Try again.")

def download(ftp, path):
	try:
		with open(basename(path), "wb") as outFPtr:
			ftp.retrbinary(f"RETR {path}", outFPtr.write)
		print(f"Downloaded {basename(path)} successfully.")

	except Exception as e:
		print(f"Failed to perform operation: {e}. Try again.")
		remove(basename(path))

if __name__ == "__main__":
	
	ftp = FTP()
	try:
		# Connect and login to the server
		ftp.connect(HOST, PORT)
		ftp.login()

	except ConnectionRefusedError:
		print("Failed to establish connection with the server.")
		exit()
	
	except Exception as e:
		print(f"Failed to perform operation: {e}. Try again.")
		exit()

	while(True):
		option = input("\nOptions:\n1 - Get a list of files on the server\n2 - Upload a file to the server\n3 - Download a file from the server\n4 - Exit program\n\nEnter option: ")
		
		try:
			option = int(option)
		except ValueError:
			print("Enter a number between 1 and 4.")
			continue

		# List server files
		if option == 1:
			show_files(ftp)
		
		# Upload a file to the server
		elif option == 2:
			local_path = input("Enter absolute file path: ")
			upload(ftp, local_path)

		# Download a file from the server
		elif option == 3:
			remote_path = input("Enter absolute file path: ")
			download(ftp, remote_path)

		# Exit program
		elif option == 4:
			exit()
		
		# Any other number
		else:
			print("Invalid entry, try again.")
			continue

	ftp.quit()