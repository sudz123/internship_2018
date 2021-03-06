# The data is saved in a CSV fle. The first column of each row is the label while the next x columns are
# pixel values between 0-255, flattened out. This code helps read a csv and reform the image of appropriate size
# This file helps load images from a csv to check if they are being stored and labelled correctly

import cv2 as cv2
import numpy as np

#Load the data from csv file and store it in a numpy array
my_data = np.loadtxt('tesdata.csv', delimiter=',')

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,50)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2

# Iterate over the rows and display eachimage with their corresponding predictions
for i in range(0,my_data.shape[0]-1):
	
	arr = my_data[i , 1:]
	command = my_data[i,0]

	arr_new = arr.reshape(240,320,3)
	cv_img = arr_new.astype(np.uint8)
	cv2.putText(cv_img,'%d'%command, bottomLeftCornerOfText, font, fontScale,fontColor,lineType)
	cv2.imshow('image',cv_img)
	cv2.waitKey(0)
#	img = Image.fromarray(np.uint8(arr_new),'RGB')
#	img = img.resize((128, 128), PIL.Image.ANTIALIAS)
#	img.show()
#	time.sleep(2)
#	img.close()

