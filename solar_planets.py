import cv2

img=cv2.imread("Project-104/PRO-104-Project-Image-main/solar-system.jpg")
cv2.putText(img,"Sun",(20,275),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Mercury",(125,175),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.3,color=(255,255,255))
cv2.putText(img,"Venus",(200,275),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.3,color=(255,255,255))
cv2.putText(img,"Earth",(300,275),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.3,color=(255,255,255))
cv2.putText(img,"Mars",(400,275),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.3,color=(255,255,255))
cv2.putText(img,"Jupiter",(525,55),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.3,color=(255,255,255))
cv2.putText(img,"Saturn",(755,100),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.3,color=(255,255,255))
cv2.putText(img,"Uranus",(975,115),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.3,color=(255,255,255))
cv2.putText(img,"Neptune",(1125,115),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.3,color=(255,255,255))


cv2.imshow("poster with cv2 by parth",img)
cv2.imwrite("Solar_systemwithname.jpg",img)
cv2.waitKey(0)