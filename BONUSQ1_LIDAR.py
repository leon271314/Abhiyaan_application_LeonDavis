import cv2
import numpy as np
import matplotlib.pyplot as plt

def lidar(img , name):
  height = img.shape[0]
  width = img.shape[1]

  max_length = width/2


  for x in range(360):
      theta = x*2*np.pi/360
      for r in range(int(width/2)):
          if(int(height/2 + r*np.sin(theta)) < height):


              if(img[int(height/2 + r*np.sin(theta)), int(width/2 + r*np.cos(theta))] < 200):
                  plt.plot(x,r/(max_length),'.b')
                  break

  plt.ylim(0,1)
  plt.xlim(0,360)

  plt.xlabel('Serial number of beam')
  plt.ylabel('Normalised length')
  plt.title(name)


  plt.show()
  cv2.imshow(name,img)
  cv2.waitKey(0)


image = cv2.imread("4Junc.png", cv2.IMREAD_GRAYSCALE)
lidar(image,"4Junc")
image = cv2.imread("Curve.png", cv2.IMREAD_GRAYSCALE)
lidar(image,"Curve")
image = cv2.imread("scenario.png", cv2.IMREAD_GRAYSCALE)
lidar(image,"scenario")
image = cv2.imread("Straight.png", cv2.IMREAD_GRAYSCALE)
lidar(image,"Straight")
image = cv2.imread("TJunc.png", cv2.IMREAD_GRAYSCALE)
lidar(image,"TJunc")

cv2.destroyAllWindows()
