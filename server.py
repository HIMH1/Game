import socket

server = socket.socket()
server.bind(('127.0.0.1', 3000))
print ('Server ready at 127.0.0.1')
server.listen(1)
client, address = server.accept()
print ('Got connection from', address)
while True:
	data = [3]
	data0_byte=client.recv(1024).decode()
	data.insert(0,data0_byte)
	print('arg0 captured', data0_byte)
	if data[0] == 'exit':
		print ('Exiting')
		server.close()
		client.close()
		break
	data1_byte = client.recv(1024).decode()
	data.insert(1,data1_byte)
	print('arg1 captured', data1_byte)

	data2_byte = client.recv(1024).decode()
	data.insert(2,data2_byte)
	print('arg2 captured', data2_byte)
	hasil=0
	if data[0] == '+':
		hasil = int(data[1]) + int(data[2])
	elif data[0] == '-':
		hasil = int(data[1]) - int(data[2])
	elif data[0] == '*':
		hasil = int(data[1]) * int(data[2])
	elif data[0] == '/':
		hasil = int(data[1]) / int(data[2])
	print (data[1], data[0], data[2], '=', hasil)
	hasil_byte=str.encode(str(hasil))
	client.send(hasil_byte)