import socket
# names = ["monday","friday","john"]
# ages = [23,45,67]

# result = zip(names, ages)
# print(list(result))

# socket

# server = socket.socket()
# print('socket created wooooo')

# server.bind(('localhost', 9999))

# server.listen(3)
# print('waiting for connections')

# while True:
#     c, addr = server.accept()
#     name = c.recv(1024).decode()
#     print("connected with", addr, name)

#     c.send(bytes("Welcome client!", 'utf-8'))

#     Hf = input('how are you')
#     c.send(bytes(Hf, 'utf-8'))

#     c.close()

# import socket

# # create socket
# server = socket.socket()

# print("Socket created successfully")

# # bind ip and port
# server.bind(('localhost', 9999))

# # listen for connections
# server.listen(3)

# print("Waiting for connections...")

# while True:
#     # accept connection
#     c, addr = server.accept()

#     print("Connected with:", addr)

#     # receive client name
#     name = c.recv(1024).decode()

    # print("Client name is:", name)

    # # send welcome message
    # c.send("Welcome client!".encode())

    # # send another message
    # message = input("How are you? : ")

    # c.send(message.encode())

    # # close connection
    # c.close()

import socket

server = socket.socket()
server.bind(('localhost', 9999))
server.listen()

print("Waiting for connection...")

c, addr = server.accept()

print("Connected with", addr)

while True:
    message = c.recv(1024).decode()

    if message.lower() == "bye":
        break

    print("Client:", message)

    reply = input("You: ")

    c.send(reply.encode())

c.close()