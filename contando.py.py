import cv2
import numpy as np
import os
import csv

def getArea(img):
	area = 0
	for x in range(img.shape[0]):
		for y in range (img.shape[1]):
			if(img[x][y].all()==0):
				area += 1
	return area


areas  = []
pathFolder = "saida2/"
file = open('report2.txt', 'w')
filesArray = [x for x in os.listdir(pathFolder) if os.path.isfile(os.path.join(pathFolder,x))]
for file_name in filesArray:
    file_name_no_extension = os.path.splitext(file_name)[0]
    fundus = cv2.imread(pathFolder+'/'+file_name)
    area = getArea(fundus)
    areas.append(area)
    print (file_name, "AREA: ",area)
    file.write("%s - AREA: %d\n" % (file_name, area))
