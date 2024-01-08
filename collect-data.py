import cv2
import getch
import socket
import numpy as np
import os
import multiprocessing
''''''''''''''''''''''''''''''''''''

def order_function(char):
    global order
    if char == 'w':
        order = 3
        ord_Array[:] = [0, 0, 1, 0]
    elif char == 'a':
        order = 2
        ord_Array[:] = [0, 1, 0, 0]
    elif char == 'd':
        order = 1
        ord_Array[:] = [1, 0, 0, 0]
    else:
        order = 4
        ord_Array[:] = [0, 0, 0, 1]
    return order

def server_function():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.0.109"
    port = 9997
    serversocket.bind((host, port))
    serversocket.listen(5)
    while True:
        char = getch.getche()
        if char:
            Order = order_function(char)
        clientsocket, addr = serversocket.accept()
        print(" Got a connection from %s" % str(addr))
        clientsocket.send(str(Order).encode('utf-8'))
        clientsocket.close()

def save_picture():
    retval = os.getcwd()
    print ("Current working directory %s" % retval)
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture('http://192.168.0.111:4747/video')
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False
    i = 0
    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        gray = cv2.cvtColor(np.asarray(frame), cv2.COLOR_BGR2GRAY)   #change RGB to gray format
        reimage = cv2.resize(gray, (32, 24))   #resize image
        raveled = reimage.ravel()  #make a 1-dimensional view of image
        if cv2.imwrite('./testfiles/bmpfiles/camsave' + str(i) + '.bmp', reimage): #save the gray image in .bmp format
            np.savez('./testfiles/npzfiles/img_pixels' + str(i) + '.npz', img = raveled, order = ord_Array)  #save as a .npz file
            print ('camsave' , i, ord_Array[:])
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
        i += 1
    cv2.destroyWindow("preview")

def main():
    proc1 = multiprocessing.Process (target = save_picture)
    proc1.start()
    proc2 = multiprocessing.Process(target = server_function)
    proc2.start()

if __name__ == "__main__":
    ord_Array = multiprocessing.Array('i', (0, 0, 0, 0))
    order = 0
    proc1 = multiprocessing.Process (target = save_picture)
    proc1.start()
    proc2 = multiprocessing.Process(target = server_function)
    proc2.start()
    #main()
