import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

while True:
        socket.listen(5)
        client, address = socket.accept()
        print ("{} connected".format(address[0]))

        response = client.recv(255)
        if response != "":
                print (response)
        if response==b'stop':
                break

print ("Close")
client.close()
stock.close()