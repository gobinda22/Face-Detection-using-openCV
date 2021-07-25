import cv2

# create the haar cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
      _, imagePath = cap.read()# it returns two variable one is flag and other is image itself


    # convert the image into grayscale image

      gray = cv2.cvtColor(imagePath, cv2.COLOR_BGR2GRAY)# by deafult cv2 process images in BGR(blue, green, red)

    # Detect the faces in the image

      faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # scaleFactor 1.1 - Since some faces may be closer to the camera, they would appear bigger than the faces in the back. The scale factor compensates for this.
    # minNeighbors 4 defines how many objects are detected near the current one before it declares the face found.
    # minSize gives the size of each window.

      for (x, y, w, h) in faces:
            cv2.rectangle(imagePath, (x, y), (x+w, y+h), (255, 0, 0), 2) # the x and y location of the rectangle, and the rectangle’s width and height (w,h).


      cv2.imshow('img', imagePath)
      k = cv2.waitKey(30) & 0xff
      if k == 27:
          break

cap.release()