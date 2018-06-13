#! encoding: UTF-8
import os
import random
import cv2

videos_src_path = '***'
videos_save_path = '***'

videos = os.listdir(videos_src_path)

#videos = filter(lambda x: x.endswith('avi'), videos)
params = []
params.append(int(cv2.IMWRITE_PNG_COMPRESSION))
params.append(3)
for each_video in videos:
    print each_video

    # get the name of each video, and make the directory to save frames
    each_video_name, _ = each_video.split('.')
    save_path = videos_save_path + '/' + each_video_name
    if not os.path.exists(save_path):
        os.mkdir(save_path)               

    each_video_save_full_path = save_path + '/'

    # get the full path of each video, which will open the video tp extract frames
    each_video_full_path = os.path.join(videos_src_path, each_video)

    cap  = cv2.VideoCapture(each_video_full_path)
    frameRate = cap.get(5)
    # frameRate 25
    print frameRate
    frame_count = 1
    success = True
    frameRate1 = frameRate // 2
    frameRate2 = frameRate // 3
    frate = [frameRate,frameRate1,frameRate2]
    
    #print cap.get(3), cap.get(4)
    #cap.set(3, 1024)
    #cap.set(4, 512)
    while(success):
        
        frameId = cap.get(1) #current frame number
        success, frame = cap.read()
        #print 'Read a new frame: ', success
        #print cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        #index = random.randint(0,2)
        #if frameId % frate[index] == 0:
        if frameId % 13 == 0:
            print frameId
            frame = cv2.resize(frame, (1024,512), interpolation=cv2.INTER_AREA)
            #缩小建议用 INTER_AREA， 放大用 cv2.INTER_CUBIC（慢）和cv2.INTER_LINEAR
            cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.png" % frame_count, frame, params)
            frame_count = frame_count + 1
        """
        函数名：cv2.imwrite( P1 , P2 , P3 )
        功  能：图像保存函数
        参数一：图像保存的路径、名称
        参数二：保存的图像
        参数三：可不填写，设置图像压缩，即图像的保存精度
              如果保存为 JPG 格式，则为 CV_IMWRITE_JPEG_QUALITY ，本身为 LONG 型，使用时应转化为 int 类型
              如果保存为 PNG 格式，则为 CV_IMWRITE_PNG_COMPRESSION ，本身为 LONG 型，使用时应转化为 int 类型
              如果保存为 PPM、PGM、PBM，则为 CV_IMWRITE_PXM_BINARY ，
    
              若参数三为 CV_IMWRITE_JPEG_QUALITY ，则范围为 0-100 ，默认值为 95
              若参数三为 CV_IMWRITE_PNG_COMPRESSION ， 则范围为 0-9 ， 默认值为 3
              若参数三为 CV_IMWRITE_PXM_BINARY ，则取值为 0 或 1 ，默认值为 1
        """
        #break

cap.release()
