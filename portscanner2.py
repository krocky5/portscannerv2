
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = input("Put a website ---> ")

def pscan(port):
	try:
		s.connect((server,port))
		return True
	except:
		return False

for x in range(1,26):
	if pscan(x):
		print("port",x,"is open my dude")
	else:
		print("port",x,"is closed")