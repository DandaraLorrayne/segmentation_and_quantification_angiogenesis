import cv2

def CalcBGRvalues(x,y):#calcular o valor BGR com base no x,y
    B=img[x,y,0] #posição e canal 0 = blue
    G=img[x,y,1] #posição e canal 1 = green
    R=img[x,y,2] #posição e canal 2 = red
    print("[x:",x,"y:",y,"]","[B:",B,"G:",G,"R:",R,"]")#exibir posição e valores BGR
    
def CallBackFunc(event, x, y, flags, param):#pega a posição do mouse e calcula BGR
    if event == cv2.EVENT_MOUSEMOVE:
        CalcBGRvalues(x,y)

img = cv2.imread('./images/input.png')#ler imagem
cv2.namedWindow('image')#nome da janela
cv2.setMouseCallback('image',CallBackFunc)#ligar a imagem à função callbackfunc
cv2.imshow('image', img)
cv2.waitKey()
