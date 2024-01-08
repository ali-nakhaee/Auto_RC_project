import getch
import cv2
import socket 

''''''''''''''''''''''''''''''''''''''
#camera connection
cv2.namedWindow("preview")
vc = cv2.VideoCapture('http://192.168.0.111:4747/video')
if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")


''''''''''''''''''''''''''''''''''''
#get order from user

def orderFunction (char):
    #char = getch.getche() 
    #char = getch.getch()
    if char == 'w':
        order = 3
    
    elif char == 'a':
        order = 2
    
    elif char == 'd':
        order = 1
        
    else:
        order = 4
        
    return order
    


''''''''''''''''''''''''''''''''''''
#make server
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 


# get local machine name
#host = socket.gethostname()                           
host = "192.168.0.109"
port = 9995                          

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    char = getch.getche()
    if char:
        order1 = orderFunction(char)
    
    clientsocket,addr = serversocket.accept()      
    print("Got a connection from %s" % str(addr))
    clientsocket.send(str(order1).encode('utf-8'))
    #clientsocket.send("Alioooo".encode())
    #clientsocket.send(10)
    clientsocket.close()
