import cv2

# 画像データの読み込み
img = cv2.imread('./img/img01.jpg')
height, width = img.shape[:2]
print('画像幅：'+str(width))
print('画像高さ：'+str(height))
cv2.imshow('img',img)
cv2.waitKey(0)

# 動画データの読み込み
# 情報取得 #
cap = cv2.VideoCapture('.//mov/mov01.avi')
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)
print('画像幅：'+str(width))
print('画像高さ：'+str(height))
print('総フレーム数：'+str(count))
print('FPS:' + str(fps))

# # 出力(再生のみ)
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret:
#         cv2.imshow('frame',frame)
#     if cv2.waitKey(1)&0xFF==ord('q'): #'q'キーで終了
#         break
# cap.release()
# cv2.destroyAllWindows()



# 映像を画像に分割して保存
# snapshotフォルダに保存する
num=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow('frame',frame)
        filepath = './snapshot/snapshot_'+str(num)+'.jpg'
        cv2.imwrite(filepath,frame)
        if cv2.waitKey(1)&0xFF==ord('q'): #'q'キーで終了
            break
    num = num + 1
cap.release()
cv2.destroyAllWindows()
