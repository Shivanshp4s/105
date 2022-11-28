import os
import cv2


path = "C:/Users/DELL/Documents/python/Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height,width,channel = frame.shape
size=(width,height)
print(size)

out=cv2.VideoWriter("sunset.mp4",cv2.VideoWriter_fourcc(*'mp4v'),5,size)

#for sun rise
for i in range(count-1,0,-1):
    frame=cv2.imread(images[i])
    out.write(frame)
    if cv2.waitKey(1) == 32 :
        break

out.release()
print("done")