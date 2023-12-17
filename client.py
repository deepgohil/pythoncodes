# import socket 

# def mpm():
#     host = "127.0.0.1"
#     port = 6001

#     s = socket.socket()
#     s.connect((host,port))
#     print("Connection established")

#     while True: 
#         print()
#         x = input("Client : ")
#         y = x.encode("ascii")
#         s.send(y)

#         print()

#         data = s.recv(1024)
#         d = data.decode("ascii")
#         print("Server : ",d)
        

# mpm()

import socket

def mpm():
    host = '127.0.0.1'
    port = 6011
    
    s = socket.socket()
    
    s.connect((host,port))
    print('Connection Established!')
    
    while True:
        x = input('Client: ')
        x = x.encode('ascii')
        s.send(x)
        
        print()
        
        data = s.recv(1024)
        d = data.decode('ascii')
        print('Server: ',d)
        
mpm()






































