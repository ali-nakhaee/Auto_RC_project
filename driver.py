import cv2
import socket
import numpy as np
import multiprocessing

def order_function():
    print('Model is loading...')
    loaded_model = cv2.ml.ANN_MLP_load('./testfiles/nn_model_02.xml')
    
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture('http://192.168.0.111:4747/video')
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False
    while rval:
        #cv2.imshow("preview", frame)
        rval, frame = vc.read()
        lhf = frame[0:320, :] #lower half of image
        cv2.imshow("preview", lhf)
        gray = cv2.cvtColor(np.asarray(lhf), cv2.COLOR_BGR2GRAY)   #change RGB to gray format
        reimage = cv2.resize(gray, (32, 12))   #resize image
        raveled = reimage.ravel()  #make a 1-dimensional view of image
        x = np.empty((1, 32*12), np.float32)
        x[:] = raveled[:]
        Order, resp = loaded_model.predict(x)
        order.value = int(Order)
        print(order.value)
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
    cv2.destroyWindow("preview")
    
def server_function():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.0.109"
    port = 9998
    serversocket.bind((host, port))
    serversocket.listen(5)
    while True:
        clientsocket, addr = serversocket.accept()      
        print(" Got a connection from %s" % str(addr), order.value, 'as order has send!')
        clientsocket.send(str(order.value).encode('utf-8'))
        clientsocket.close()
    
    
    
if __name__ == '__main__':
    order = multiprocessing.Value('i', 0)
    proc1 = multiprocessing.Process (target = order_function)
    proc1.start()
    proc2 = multiprocessing.Process (target = server_function)
    proc2.start()