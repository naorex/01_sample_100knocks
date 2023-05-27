# 数フレームから1フレームを抜き出して早送り風のタイムラプス動画を生成

import cv2

print('タイムラプス生成を開始')

# 映像取得
cap = cv2.VideoCapture('./mov/mov01.avi')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# hog宣言
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
hogParams = {'winStride':(8,8),'padding':(32,32),'scale':1.05,
            'hitThreshold':0}
            # 'finalThreshold':5} # エラーを吐くのでキャンセル

# タイムラプス生成
movie_name = 'timelapse.avi'
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
video = cv2.VideoWriter(movie_name,fourcc,30,(width,height))

num = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        if (num%10==0):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            human, r = hog.detectMultiScale(gray, **hogParams)
            if (len(human)>0):
                for (x,y,w,h) in human:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),3)
            video.write(frame)
    else:
        break
    num += 1
video.release()
cap.release()
cv2.destroyAllWindows()
print('タイムラプス生成を終了しました')
