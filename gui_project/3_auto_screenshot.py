import time
from PIL import ImageGrab

time.sleep(5) # wait 5

for i in range(1,11):#every 2 sec, save 10 images
    img.ImageGrab.grab()#current screen 
    img.save("image{}.png".format(i)) #save as file
    time.sleep(2)