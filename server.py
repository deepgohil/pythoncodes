# import socket

# def mpm():
#     host  = "127.0.0.1"
#     port = 6001

#     s = socket.socket()
#     s.bind((host,port))
#     s.listen(1)
#     print("Waiting for connection")
#     c, addr = s.accept()
#     print("Connection Established")
#     print("Client Address : ",addr)
     
#     while True:
#         print()
#         data = c.recv(1024)
#         d = data.decode("ascii")
#         print("Client : ",d)
        
#         print()
        
#         x = input("Server : ")
#         y = x.encode("ascii")
#         c.send(y)
        
# mpm()

import socket

def mpm():
    host = '127.0.0.1'
    port = 6011
    
    s = socket.socket()
    s.bind((host,port))
    s.listen(1)
    
    print('Connection Waiting.....')
    c, addr = s.accept()
    print('Connection Established!')

    while True:
        data = c.recv(1024)
        d = data.decode('ascii')
        print("Client: ",d)
        
        print()
        
        x = input('Server: ')
        x = x.encode('ascii')
        c.send(x)


mpm()































