import numpy as np
import cv2

def load_data():
    global number_of_data
    global X
    global Y
    global x
    for i in range(1, number_of_data):
        data = np.load('./testfiles/npzfiles/img_pixels' + str(i+390) + '.npz')
        X[i, :] = data['img']
        Y[i, :] = data['order']
    
    X = X / 255     #Normalize Data
    for i in range(1, number_of_data):
        x[i, :] = X[i, :32*12]          #upper half of the image
    print('Load data compeleted...')
    #print('X.shape = ', X.shape)
    print('x.shape = ', x.shape)
    print('Y.shape = ', Y.shape)
    #print('for example X[130] = %a and Y[130] = %a' %(X[130, :], Y[130, :]))
    #print('X[i, :].shape = ', X[130, :].shape)
    print('for example x[130] = %a and Y[130] = %a' %(x[130, :], Y[130, :]))
    print('x[i, :].shape = ', x[130, :].shape)
    
def model():
    #creat model
    ann = cv2.ml.ANN_MLP_create()
    ann.setTrainMethod(cv2.ml.ANN_MLP_BACKPROP | cv2.ml.ANN_MLP_UPDATE_WEIGHTS)
    #ann.setLayerSizes(np.array([64*48, 500, 4]))
    ann.setLayerSizes(np.array([32*24/2, 32, 4]))
    ann.setActivationFunction(cv2.ml.ANN_MLP_SIGMOID_SYM)
    ann.setTermCriteria(( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 100, 0.01 ))
    print ('Model created.')
    
    #train model
    print('Training started...')
    #ann.train(X[:], cv2.ml.ROW_SAMPLE, Y[:])
    ann.train(x[:], cv2.ml.ROW_SAMPLE, Y[:])
    print('Training Compeleted.')
    
    #test a sample input
    #test = X[300, :].reshape(1, 3072)
    test = x[300, :].reshape(1, 384)
    print('sample predict output is: ', ann.predict(test))
    
    #save model
    #ann.save('./testfiles/nn_model_01.xml')
    ann.save('./testfiles/nn_model_02.xml')
    print('Model saved.')
    
def load_evaluate_model():
    print('model is loading...')
    #loaded_model = cv2.ml.ANN_MLP_load('./testfiles/nn_model_01.xml')
    loaded_model = cv2.ml.ANN_MLP_load('./testfiles/nn_model_02.xml')
    #ret, resp = loaded_model.predict(X)
    ret, resp = loaded_model.predict(x)
    prediction = resp.argmax(-1)
    true_labels = Y.argmax(-1)
    accuracy = np.mean(prediction == true_labels)
    print('model accuracy = ', accuracy)
    
    
    
if __name__ == '__main__':
    number_of_data = 1120
    X = np.empty((number_of_data, 32*24), np.float32)
    x = np.empty((number_of_data, 32*12), np.float32)     #half of image
    Y = np.empty((number_of_data, 4), np.float32)
    load_data()
    model()
    load_evaluate_model()
    
        