# import socket

# c = socket.socket()
# print('client is always right')

# c.connect(('localhost', 9999))

# name = input('what is your name?')
# c.send(bytes(name, 'utf-8'))


# Hf = c.recv(1024).decode()
# print(c.recv(1024).decode())

# print(Hf)

# import socket

# create socket
# c = socket.socket()

# print("Client started")

# # connect to server
# c.connect(('localhost', 9999))

# send name
# name = input("What is your name? : ")

# c.send(name.encode())

# # receive first message
# msg1 = c.recv(1024).decode()

# # receive second message
# msg2 = c.recv(1024).decode()

# # print messages
# print(msg1)
# print(msg2)

# # close connection
# c.close()


import socket

c = socket.socket()

c.connect(('localhost', 9999))

while True:
    msg = input("You: ")

    c.send(msg.encode())

    if msg.lower() == "quite":
        break

    reply = c.recv(1024).decode()

    print("Server:", reply)

c.close()