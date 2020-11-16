import cv2

# So in this line of code we have loaded the image, you need to have an image in your working directory
image = cv2.imread("real_00034.jpg")
blurImg = cv2.blur(image,(30,30))
#gausBlur = cv2.GaussianBlur(image, (5,5),0)


# This is for loading our Haar Cascade Classifier that we have already copied in our directory
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#face_cascade = cv2.CascadeClassifier("own_cascade.xml") #trained by 128 positive image, 270 negative image


# detectMultiScale() function is for detecting objects if it finds a face in the image it will return
# in the form of x,y,w,h. and it needs some parameters.
# This is parameter is for specifying  how much the image size is reduced at each image scale.
# minNeighbors: Parameter specifying how many neighbors each candidate rectangle should have to retain it,
# this parameter will affect the quality of the detected faces.

quit = False
i = 1

while  quit == False and i < 200:
    eyes = eye_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=i)
    print(f"I értéke: {i}")
    print(f"Szem mennyisége: {len(eyes)}")
    if len(eyes) == 2:
        quit = True
    if len(eyes) == 0:
        quit = True
    i+=1

i = 1
quit = False

while  quit == False and i < 200 and len(eyes) == 2:
    faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=i)
    print(f"I értéke: {i}")
    print(f"Arc mennyisége: {len(faces)}")
    if len(faces) == 1:
        quit = True
    if len(eyes) == 0:
            quit = True
    i+=1

#DEBUG
    # print(f"arc {faces}")
    # print(f"szem {eyes}")
    # print(f"szem2 arcx{faces[0,0]} < szemx{eyes[1,0]} VAGY arcy{faces[0,1]} > szemy{eyes[1,1]}")
    # print(f"szem  arcx{faces[0,0]} < szemx{eyes[0,0]} VAGY arcy{faces[0,1]} > szemy{eyes[0,1]}")
    # print(f"arcx{[faces[0,0] + faces[0,2]]} < szemx{[eyes[0,0] + eyes[0,2]]} VAGY arcy{[faces[0,1] + faces[0,3]]} < szemy{[eyes[0,0] + eyes[0,3]]}")
    # print(f"arcx{[faces[0,0] + faces[0,2]]} < szemx{[eyes[1,0] + eyes[1,2]]} VAGY arcy{[faces[0,1] + faces[0,3]]} < szemy{[eyes[1,0] + eyes[1,3]]}")

blurry = False

if  len(eyes) > 0 and len(faces) > 0 :
    #SZEM 1
        #  x        x           és  y               y
        #KEZDŐ
    if faces[0,0] > eyes[0,0] or faces[0,1] > eyes[0,1]:
        blurry = True
        print("belep1")
        #VÉG
    if [faces[0,0] + faces[0,2]] < [eyes[0,0] + eyes[0,2]] or [faces[0,1] + faces[0,3]] < [eyes[0,0] + eyes[0,3]]:
        blurry = True
        print("belep2")
    #SZEM 2
    # KEZDŐ
    if faces[0, 0] > eyes[1, 0] or faces[0, 1] > eyes[1, 1]:
        blurry = True
        print("belep3")

        # VÉG
    if [faces[0, 0] + faces[0, 2]] < [eyes[1, 0] + eyes[1, 2]] or [faces[0, 1] + faces[0, 3]] < [eyes[1, 0] + eyes[1, 3]]:
        blurry = True
        print("belep4")

if len(eyes) != 2 or len(faces) != 1 or blurry:
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    # org
    org = (30, 350)
    # fontScale
    fontScale = 1.2
    # Blue color in BGR
    color = (255, 255, 255)
    # Line thickness of 2 px
    thickness = 4
    image = cv2.putText(blurImg, 'Nem sikerult a felismeres!', org, font,
                       fontScale, color, thickness, cv2.LINE_AA)
else:
    # So in this code we want to draw rectangle in the eyes in image
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(image, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2) #line color and thickness
    # So in this code we want to draw rectangle in the face in image
    for x, y, w, h in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2) #




# In this line of code we want to show our image
cv2.imshow("Eye, Face Detected", image)


cv2.waitKey(0)
cv2.destroyAllWindows()