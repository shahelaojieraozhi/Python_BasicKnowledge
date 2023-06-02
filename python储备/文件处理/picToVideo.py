import cv2

img = cv2.imread('F:\治\PURE/01-01/01-01/1.png')
imgInfo = img.shape
size = (imgInfo[1], imgInfo[0])
videoWrite = cv2.VideoWriter('5.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 25, size)

# 写入对象  1. file name   2. 编码器  3. 帧率   4 .size
for i in range(1, 128):
    fileName = str(i) + '.png'
    img = cv2.imread('./' + fileName)
    videoWrite.write(img)  # 写入方法 1 jpg dataprint('end!')
