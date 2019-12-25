import socket

client = socket.socket()
ipaddr = input('Connect to IP: ')
client.connect((ipaddr, 3000))
print ('Connected to server')
while True:
	operator = input('Operator: ')
	operator_byte = str.encode(operator)
	client.send(operator_byte)


	operandA = input('Operand 1: ')
	operandA_byte = str.encode(operandA)
	client.send(operandA_byte)


	operandB = input('Operand 2: ')
	operandB_byte = str.encode(operandB)
	client.send(operandB_byte)

	hasil_byte=client.recv(1024).decode()
	print ('Hasil:', hasil_byte)
	if 'exit' == input('Type "exit" to exit, no input to continue '):
		client.send('exit')
		client.close()
		exit()