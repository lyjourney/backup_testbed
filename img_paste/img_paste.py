from PIL import Image
import numpy as np
import cv2

car_origin = Image.open("car.png")

opencvImage = cv2.cvtColor(np.array(car_origin), cv2.COLOR_RGB2BGR)
opencvImage = cv2.cvtColor(opencvImage, cv2.COLOR_RGB2RGBA)
opencvImage[opencvImage[:,:,3]<=150] = 0

# cv2.imwrite("here.jpg",opencvImage)

blank_img = Image.new("RGB",size=(1920,1080),color = (153, 153, 255))
blank_img.convert('RGBA')

#Image.alpha_composite(Image.new("RGBA",car_origin.size),car_origin).save("test.jpg")

blank_img.paste(car_origin,(1000,100),car_origin)

conv = blank_img.convert('RGB')
conv.save("test.jpg")

#car_np = np.asarray(car_origin).copy()
# car_np[car_np[:,:,3]<=150] = 0

#im22 = Image.fromarray(im2)
#im222 = im22.convert('RGB')
#im222.save("testtest.jpg")
