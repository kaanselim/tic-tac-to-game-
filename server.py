import socket

s = socket.socket() # creating a socket object

port = 12345


s.bind(("",port))

s.listen(5)
print("socket is listening")


while True:
	c, addr = s.accept()
	print("got connection from", addr)
	a = input("please enter an input to send to client")
	c.sendall(b"thank you for connecting"+a)

	c.close()