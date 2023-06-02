# -*- coding: UTF-8 -*-
import os
import cv2
import time

# 图片合成视频
def picvideo(path, size):
    '''
    fps:
    帧率：1秒钟有n张图片写进去[控制一张图片停留5秒钟，那就是帧率为1，重复播放这张图片5次]
    如果文件夹下有50张 534*300的图片，这里设置1秒钟播放5张，那么这个视频的时长就是10秒
    '''
    fps = 30
    size = (640, 480)  # 图片的分辨率片
    # file_path = "./" + str(int(time.time())) + ".mp4"  # 导出路径
    file_path1 = "./" + '100201' + ".mp4"  # 导出路径
    file_path2 = "./" + '100202' + ".mp4"  # 导出路径
    fourcc = cv2.VideoWriter_fourcc('d', 'i', 'v', 'x')  # 不同视频编码对应不同视频格式（例：'I','4','2','0' 对应avi格式）
    video1 = cv2.VideoWriter(file_path1, fourcc, fps, size)
    video2 = cv2.VideoWriter(file_path2, fourcc, fps, size)
    # video = cv2.VideoWriter(file_path, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    # (1, 901) (901, 1801)
    for i in range(1, 901):
        fileName = str(i) + '.png'
        img = cv2.imread(
            r".\10-02/" + fileName)  # 使用opencv读取图像，直接返回numpy.ndarray 对象，通道顺序为BGR ，注意是BGR，通道值默认范围0-255。
        video1.write(img)  # 把图片写进视频

    video1.release()  # 释放

    for i in range(901, 1801):
        fileName = str(i) + '.png'
        img = cv2.imread(
            r".\10-02/" + fileName)  # 使用opencv读取图像，直接返回numpy.ndarray 对象，通道顺序为BGR ，注意是BGR，通道值默认范围0-255。
        video2.write(img)  # 把图片写进视频

    video2.release()  # 释放


picvideo('./', (640, 480))

