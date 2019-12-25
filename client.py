import socket

client = socket.socket()
ipaddr = input('Connect to IP: ')
client.connect((ipaddr, 3000))
print('Connected to server')

print('you in the range from 0-5')
while True:
    guessed = str.encode(input('guess what number i have: '))
    client.send(guessed)
    receivedMsg = client.recv(1024).decode()
    print(receivedMsg)
    if receivedMsg == 'you lost':
        client.send(str.encode('exit'))
        client.close()
        exit()

