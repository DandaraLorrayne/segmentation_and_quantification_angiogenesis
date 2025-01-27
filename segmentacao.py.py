import cv2
import numpy as np
import os
import csv


def extract_bv(image):		#foi extraido o canal verde da imagem pois possui maior contraste
	b,green_fundus,r = cv2.split(image)
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))# foi aplicada a equalização do histograma adaptativo com contrate limitado, para aumentar ainda mais o contrate
	contrast_enhanced_green_fundus = clahe.apply(green_fundus)

	# aplicando filtragem sequencial alternativa= 3 vezes fechando e 3 vezes abrindo
	r1 = cv2.morphologyEx(contrast_enhanced_green_fundus, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)), iterations = 1)
	R1 = cv2.morphologyEx(r1, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)), iterations = 1)
	r2 = cv2.morphologyEx(R1, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11)), iterations = 1)
	R2 = cv2.morphologyEx(r2, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11)), iterations = 1)
	r3 = cv2.morphologyEx(R2, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(23,23)), iterations = 1)
	R3 = cv2.morphologyEx(r3, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(23,23)), iterations = 1)	
	f4 = cv2.subtract(R3,contrast_enhanced_green_fundus)#subtraindo a imagem de saida de clahe
	f5 = clahe.apply(f4)		

	# removendo contornos pequenos tomando a area como parametro e removendo ruidos
	ret,f6 = cv2.threshold(f5,15,255,cv2.THRESH_BINARY)	#limiarizacao
	mask = np.ones(f5.shape[:2], dtype="uint8") * 255	
	contours, hierarchy = cv2.findContours(f6.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)#encontrando os contornos
	for cnt in contours:
		if cv2.contourArea(cnt) <= 200:
			cv2.drawContours(mask, [cnt], -1, 0, -1)			
	im = cv2.bitwise_and(f5, f5, mask=mask)
	ret,fin = cv2.threshold(im,15,255,cv2.THRESH_BINARY_INV)			
	newfin = cv2.erode(fin, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)), iterations=1)	#erosao dos ruidos

	# remover partes maiores e manchas, levando em consideracao que nao possuem formas lineares como as dos vasos sanguineos
	fundus_eroded = cv2.bitwise_not(newfin)	
	xmask = np.ones(fundus.shape[:2], dtype="uint8") * 255
	xcontours, xhierarchy = cv2.findContours(fundus_eroded.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)	
	for cnt in xcontours:
		shape = "unidentified"
		peri = cv2.arcLength(cnt, True)
		approx = cv2.approxPolyDP(cnt, 0.04 * peri, False)   				
		if len(approx) > 4 and cv2.contourArea(cnt) <= 3000 and cv2.contourArea(cnt) >= 100:
			shape = "circle"	
		else:
			shape = "veins"
		if(shape=="circle"):
			cv2.drawContours(xmask, [cnt], -1, 0, -1)	
	
	finimage = cv2.bitwise_and(fundus_eroded,fundus_eroded,mask=xmask)	
	blood_vessels = cv2.bitwise_not(finimage)
	return blood_vessels	

if __name__ == "__main__":	
	pathFolder = "retinas_apos_angiogenese/" #pasta de imagens de entrada
	filesArray = [x for x in os.listdir(pathFolder) if os.path.isfile(os.path.join(pathFolder,x))]
	destinationFolder = "saida_apos_angiogenese/" # salvando as imagens de saida na pasta
	if not os.path.exists(destinationFolder):
		os.mkdir(destinationFolder)
	for file_name in filesArray:
		file_name_no_extension = os.path.splitext(file_name)[0]
		fundus = cv2.imread(pathFolder+'/'+file_name)		
		bloodvessel = extract_bv(fundus)
		cv2.imwrite(destinationFolder+file_name_no_extension+"_bloodvessel.png",bloodvessel)
    
