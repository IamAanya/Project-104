import cv2
img=cv2.imread("PRO-104-Project-Image-main/solar-system.jpg")
cv2.putText(img,"Sun",(100,80),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"Mercury",(125,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Jupiter",(500,80),cv2.FONT_HERSHEY_COMPLEX,1.7,(0,0,255))
cv2.imshow("displayimage",img)

cv2.waitKey(0)
