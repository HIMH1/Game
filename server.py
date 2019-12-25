import socket
from random import randrange
import math



server = socket.socket()
server.bind(('127.0.0.1', 3000))
print ('Server ready at 127.0.0.1')
server.listen(1)
client, address = server.accept()
print('Got connection from', address)

level = 5
attempts = 1;
num = randrange(level)

while True:
	data = []
	data.append(client.recv(1024).decode())
	if data[0] == 'exit':
		print('Exiting')
		server.close()
		client.close()
		break

	if attempts <= math.ceil(math.log2(level)):
		if int(data[0]) == num:
			level = level + 5
			client.send(str.encode('you won , it will get harder ,'+' you in the range from 0-'+str(level)))
			num = randrange(level)
			attempts = 1
		elif int(data[0]) < num:
			client.send(str.encode('greater ,  you tried '+ str(attempts)+' out of '+str(math.ceil(math.log2(level)))))
			attempts = attempts+1
		elif int(data[0]) > num:
			client.send(str.encode('smaller , you tried '+str(attempts)+' out of '+str(math.ceil(math.log2(level)))))
			attempts = attempts + 1
	else:
		client.send(str.encode('you lost'))
		server.close()
		client.close()
		break
