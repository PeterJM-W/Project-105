import os
import cv2

path = "Images"
images = []

for i in os.listdir(path):
    name, ext = os.path.splitext(i)
    if ext in ['.jpg', '.png', '.gif']:
        fileName = path + "/" + i
        print(fileName)
        images.append(fileName)

count = len(images)
frame = cv2.imread(images[1])

height, width, channel = frame.shape
size = (width, height)
output = cv2.VideoWriter("memories.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 5, size)

for i in range(0, count - 1, 1):
    frame = cv2.imread(images[i])
    output.write(frame)

output.release()
print('Done!')
        
