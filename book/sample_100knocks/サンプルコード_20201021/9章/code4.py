# 全体像をグラフにして可視化

import cv2
import pandas as pd
import matplotlib.pyplot as plt

import warnings
warnings.simplefilter('ignore', FutureWarning)

print('分析を開始します')

# 映像取得
cap = cv2.VideoCapture('./mov/mov02.avi')
fps = cap.get(cv2.CAP_PROP_FPS)

# hog宣言
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
hogParams = {'winStride':(8,8),'padding':(32,32),'scale':1.05,
            'hitThreshold':0}
            # 'finalThreshold':5} # エラーを吐くのでキャンセル

num = 0
list_df = pd.DataFrame(columns=['time','people'])
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        if (num%10==0):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            human, r = hog.detectMultiScale(gray, **hogParams)
            if (len(human)>0):
                for (x,y,w,h) in human:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),3)
            tmp_se = pd.Series([num/fps,len(human)],index=list_df.columns)
            list_df = list_df.append(tmp_se, ignore_index=True)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    else:
        break
    num += 1
cap.release()
cv2.destroyAllWindows()
print('分析を終了しました')


# データフレームの可視化
plt.plot(list_df['time'],list_df['people'])
plt.xlabel('time(sec)')
plt.ylabel('population')
# plt.ylim(0,15)
plt.show()




# 移動平均を計算してノイズの影響を除去
import numpy as np

def moving_average(x,y):
    y_conv = np.convolve(y,np.ones(5)/float(5),mode='valid')
    x_dat = np.linspace(np.min(x),np.max(x),np.size(y_conv))
    return x_dat, y_conv

plt.plot(list_df['time'],list_df['people'],label='raw')
ma_x,ma_y = moving_average(list_df['time'],list_df['people'])
plt.plot(ma_x,ma_y,label='average')
plt.xlabel('time(sec)')
plt.ylabel('population')
# plt.ylim(0,15)
plt.legend()
plt.show()
