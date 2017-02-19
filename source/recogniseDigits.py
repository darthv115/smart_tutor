#!/usr/bin/python

# Import the modules
from array import *
import mnist_loader
import cPickle as pickle
import cv2
from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np
from sklearn import preprocessing

def recog(image):
    # Load the trained model
    with open('../assets/model/trained_model.pkl', 'rb') as input:
        net = pickle.load(input)

    # Load the classifier
    clf, pp = joblib.load("../assets/model/digits_cls.pkl")

    # Read the input image 
    im = cv2.imread(image)

    # Convert to grayscale and apply Gaussian filtering
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)

    # Threshold the image
    ret, im_th = cv2.threshold(im_gray, 90, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the image
    ctrs, hier = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get rectangles contains each contour
    rects = [cv2.boundingRect(ctr) for ctr in ctrs]

    # Added by Ashish
    # Digits is a ndarray to store the digits
    digits = np.zeros((1,), dtype=int)

    # For each rectangular region, calculate HOG features and predict
    # the digit using Linear SVM.
    for rect in rects:
        # Draw the rectangles
        cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3) 
        # Make the rectangular region around the digit
        leng = int(rect[3] * 1.6)
        pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
        pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
        roi = im_th[pt1:pt1+leng, pt2:pt2+leng]
        # Resize the image
        roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
        roi = cv2.dilate(roi, (3, 3))

        # data_image = array('B')
        data_image = []

        width, height = roi.shape

        for x in range(0,width):
            for y in range(0,height):
                data_image.append(roi[y,x])

        x = np.array(data_image, dtype=float)

        # Calculate the HOG features
        roi_hog_fd = hog(roi, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualise=False)
        roi_hog_fd = pp.transform(np.array([roi_hog_fd], 'float64'))

        # Expand a dimension of the ndarray
        x = np.expand_dims(x, axis=1)

        # Added 30-01-2017 <Ashish>
        # Feedforward the clean data (number) into the trained NN model
        try:
            nbr = np.argmax(net.feedforward(x))
            # print "Recognised digit: ", nbr
        except Exception, e:
            raise e
        finally:
            pass

        cv2.putText(im, str(int(nbr)), (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)

        # Append individual digits to the ndarray
        digits = np.append(digits,nbr)

    cv2.namedWindow("Resulting Image with Rectangular ROIs", cv2.WINDOW_NORMAL)
    cv2.imshow("Resulting Image with Rectangular ROIs", im)
    print "Press any key on the keyboard."
    cv2.waitKey(0)
    return digits

# !end