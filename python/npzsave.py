import cv2
import numpy as np
from PIL import Image

# img = Image.open('./testfiles/Forever-Shady-S.jpg').convert('RGBA')
# arr = np.array(img)

# # record the original shape
# shape = arr.shape

# # make a 1-dimensional view of arr
# flat_arr = arr.ravel()

# # convert it to a matrix
# vector = np.matrix(flat_arr)

# # do something to the vector
# vector[:,::10] = 128

# # reform a numpy array of the original shape
# arr2 = np.asarray(vector).reshape(shape)

# # make a PIL image
# img2 = Image.fromarray(arr2, 'RGBA')
# img2.show()





# cv2.namedWindow("preview")
# im = cv2.imread('./testfiles/camsave3.bmp')
# print (type (im))
# #rim = np.array(im)
# #reim = np.vstack(rim)
# gray = cv2.cvtColor(np.asarray(im), cv2.COLOR_BGR2GRAY)
# #reeim = gray.reshape(1, 64*48)
# reeim = gray.ravel()
# cv2.imshow("preview", reeim)
# np.savetxt("./testfiles/img_pixels3.csv", reeim, delimiter=',')
# print('hi')
# np.savez('./testfiles/img_pixels1.csv', reeim)
# #np.savez(reim)
# npzfile = np.load('./testfiles/img_pixels1.csv.npz')
npzfile1 = np.load('order.npy')
# print (npzfile.files)
print (npzfile1)

# while True:
#     key = cv2.waitKey(20)
#     if key == 27:
#         cv2.destroyWindow("preview")
#         break
    