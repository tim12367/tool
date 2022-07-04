import cv2
import os

all_name = os.listdir()
file_type = '.mp4' #影片類型
video_files = []
for name in all_name:
    if name.endswith(file_type):
        video_files.append(name)
print(video_files)

# 從影片轉換出圖片

def get_images_from_video(video_name):
    video_images = []
    vc = cv2.VideoCapture(video_name)
    
    if vc.isOpened(): #判斷是否開啟影片
        rval, video_frame = vc.read()
    else:
        rval = False

    while rval:   #擷取視頻至結束
        rval, video_frame = vc.read()
        
        if rval==True:
            video_images.append(video_frame)     
        
    vc.release()
    
    return video_images

datadir_name = 'data' #資料夾名稱

all_frame = [] # 所有影格

for video_name in video_files:
    video_images = get_images_from_video(video_name) #讀取影片並轉成圖片
    all_frame = all_frame+video_images

if os.path.exists(datadir_name) == False:
    os.mkdir(datadir_name)
for i in range(0, len(all_frame)): #顯示出所有擷取之圖片
    cv2.imshow('windows', all_frame[i])
    path = '.\\'+datadir_name+'\\'+str(i)+'.jpg'
    cv2.imwrite(path, all_frame[i])
    cv2.waitKey(10)
print('total_frame = ',end='')
print(len(all_frame))
cv2.destroyAllWindows()