import cv2 
from PIL import Image
from google.colab.patches import cv2_imshow
from datetime import datetime 
import time




img_background = cv2.imread("/content/drive/MyDrive/Opencv/katelyn-greer.jpg")
img = cv2.imread("/content/drive/MyDrive/Opencv/background.png")
ksize = (30, 30)
img_blur  = cv2.blur(img_background , ksize, cv2.BORDER_DEFAULT)
print(type(img_background)) 
#cv2.imwrite("output1.jpg", img_background)
img1 = cv2.addWeighted(img_blur[0:1920 , 0: 1668],1.2,img,1,0)
#cv2_imshow(img1)

img2 = cv2.addWeighted(img_background[0:1920 , 0: 1668],1,img,1,0)

img2 = img2[150:1600, 200:1400]

x_offset = 200
y_offset = 150
img1[y_offset:y_offset+img2.shape[0], x_offset:x_offset+img2.shape[1]] = cv2.addWeighted(img1[y_offset:y_offset+img2.shape[0], x_offset:x_offset+img2.shape[1]], 0.2, img2, 0.8, 0)
time_now = '#' + datetime.now().isoformat().split('T')[0]
cv2.putText(img1, time_now, (935, 1500), cv2.FONT_HERSHEY_COMPLEX, 1.8, (37,32,32), 2)
cv2_imshow(img1)
cv2.imwrite(time_now[1:]+'.jpg', img1)

# background = Image.open("/content/drive/MyDrive/Opencv/lachlan.jpg")
# foreground = Image.open("/content/drive/MyDrive/Opencv/pngegg.png")
# background.paste(foreground, (0, 0), foreground)
# print(type(background))
# background.save("output.jpg", "JPEG")
# label = "best teacher ever"
# thêm chữ lên ảnh
#cv2.putText(img, label, (300, 1600), cv2.FONT_HERSHEY_SCRIPT_COMPLEX , 3, (37,32,32), 2)
#cv2_imshow(img)  
# Using cv2.blur() method 
