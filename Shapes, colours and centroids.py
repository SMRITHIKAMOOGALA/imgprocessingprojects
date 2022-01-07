import cv2
import numpy as np
import os
def detectShape(c):         
	   shape = 'unknown' 
	   peri=cv2.arcLength(c,True) 
	   vertices = cv2.approxPolyDP(c, 0.02 * peri, True)
	   sides = len(vertices) 
	   if (sides == 3): 
			shape='Triangle' 
	   elif(sides==4): 
			 x,y,w,h=cv2.boundingRect(c)
			 aspectratio=float(w)/h 
			 if (aspectratio==1):
				   shape='Square'
			 else:
				   shape="Rectangle" 
	   elif(sides==5):
			shape='Pentagon' 
	   else:
		   shape='Circle' 
	   return shape 
def detectColor(ins):
	color='unidentified'
	if ins[0]==0 and ins[1]==0 and ins[2]==255:
		color='Red'
	elif ins[0]==255 and ins[1]==0 and ins[2]==0:
		color='Blue'
	elif ins[0]==0 and ins[1]==255 and ins[2]==0:
		color='Green'
	else:
		color='Orange'			 
	return color
def detect_shapes(img):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a nested list
	containing details of colored (non-white) shapes in that image
	""" 
	detected_shapes = []
	dum=img
	imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret, binary = cv2.threshold(imgray, 100, 255,cv2.THRESH_OTSU)
	inverted_binary = ~binary
	contours, hierarchy = cv2.findContours(inverted_binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for c in contours:
		sublist=[]
		M = cv2.moments(c)
		cX = int((M["m10"] / M["m00"]))
		cY = int((M["m01"] / M["m00"]))
		shape = detectShape(c)
		ins=dum[cY,cX]
		color=detectColor(ins)
		sublist.append(color)
		sublist.append(shape)
		sublist.append((cX,cY))
		detected_shapes.append(sublist)
	return detected_shapes  
def get_labeled_image(img, detected_shapes):
	"""
	Purpose:
	---
	This function takes the image and the detected shapes list as an argument
	and returns a labelled image
	"""
	for detected in detected_shapes:
		colour = detected[0]
		shape = detected[1]
		coordinates = detected[2]
		cv2.putText(img, str((colour, shape)),coordinates, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
	return img

if __name__ == '__main__':
	
	# path directory of images in 'test_images' folder
	img_dir_path = 'test_images/'

	# path to 'test_image_1.png' image file
	file_num = 1
	img_file_path = img_dir_path + 'test_image_' + str(file_num) + '.png'
	
	# read image using opencv
	img = cv2.imread(img_file_path)
	
	print('\n============================================')
	print('\nFor test_image_' + str(file_num) + '.png')
	
	# detect shape properties from image
	detected_shapes = detect_shapes(img)
	print(detected_shapes)
	
	# display image with labeled shapes
	img = get_labeled_image(img, detected_shapes)
	cv2.imshow("labeled_image", img)
	cv2.waitKey(2000)
	cv2.destroyAllWindows()
	
	choice = input('\nDo you want to run your script on all test images ? => "y" or "n": ')
	
	if choice == 'y':

		for file_num in range(1, 16):
			
			# path to test image file
			img_file_path = img_dir_path + 'test_image_' + str(file_num) + '.png'
			
			# read image using opencv
			img = cv2.imread(img_file_path)
	
			print('\n============================================')
			print('\nFor test_image_' + str(file_num) + '.png')
			
			# detect shape properties from image
			detected_shapes = detect_shapes(img)
			print(detected_shapes)
			
			# display image with labeled shapes
			img = get_labeled_image(img, detected_shapes)
			cv2.imshow("labeled_image", img)
			cv2.waitKey(2000)
			cv2.destroyAllWindows()


