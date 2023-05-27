import cv2

# HOG（輝度勾配）特徴量を求める
# 準備
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
hogParams = {'winStride':(8,8), 'padding':(32,32),
            'scale':1.05, 'hitThreshold':0}
            # 'finalThreshold':5} #エラーを吐くので除外

# 検出
img = cv2.imread('./img/img01.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
human, r = hog.detectMultiScale(gray, **hogParams)
if(len(human)>0):
    for (x,y,w,h) in human:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),3)
cv2.imshow('img',img)
cv2.imwrite('temp01.jpg',img)
cv2.waitKey(0)



# 画像内の人の顔を検出
# 準備
cascade_file = 'haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_file)

# 検出
img = cv2.imread('./img/img02.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_list = cascade.detectMultiScale(gray, minSize=(50,50))

# 検出した顔に印を付ける
for (x,y,w,h) in face_list:
    color = (0,0,225)
    pen_w = 3
    cv2.rectangle(img,(x,y),(x+w,y+h),color,thickness=pen_w)
cv2.imshow('img',img)
cv2.imwrite('temp02.jpg',img)
cv2.waitKey(0)
