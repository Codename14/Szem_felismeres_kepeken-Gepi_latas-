import cv2

#loaded the image, you need to have an image in your working directory
image = cv2.imread("face_dataset/real_00044.jpg.")
blurImg = cv2.blur(image,(30,30))
#gausBlur = cv2.GaussianBlur(image, (5,5),0)


#loading our Haar Cascade Classifier
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Teszt rész
#face_cascade = cv2.CascadeClassifier("OwnFaceCascade_size24x24_stages_15.xml") #trained by 128 positive image, 270 negative image
#face_cascade = cv2.CascadeClassifier("OwnFaceCascade_size24x24_stages_16.xml") #trained by 128 positive image, 270 negative image
#face_cascade = cv2.CascadeClassifier("OwnFaceCascade_size24x24_stages_17.xml") #trained by 128 positive image, 270 negative image
#face_cascade = cv2.CascadeClassifier("OwnFaceCascade_size24x24_stages_18.xml") #trained by 128 positive image, 270 negative image
#face_cascade = cv2.CascadeClassifier("OwnFaceCascade_size24x24_stages_19.xml") #trained by 128 positive image, 270 negative image
#face_cascade = cv2.CascadeClassifier("OwnFaceCascade_size24x24_stages_20.xml") #trained by 128 positive image, 270 negative image
#face_cascade = cv2.CascadeClassifier("OwnFaceCascade_size32x32_stages_14.xml") #trained by 128 positive image, 270 negative image

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
    if len(faces) == 0:
        quit = True
    i+=1

#DEBUG
    # print(f"arc {faces}")
    # print(f"szem {eyes}")
    # print(f"Bal szem arcx{faces[0,0]} < szemx{eyes[1,0]} VAGY arcy{faces[0,1]} > szemy{eyes[1,1]}")
    # print(f"Jobb szem  arcx{faces[0,0]} < szemx{eyes[0,0]} VAGY arcy{faces[0,1]} > szemy{eyes[0,1]}")
    # print(f"arcx{[faces[0,0] + faces[0,2]]} < szemx{[eyes[0,0] + eyes[0,2]]} VAGY arcy{[faces[0,1] + faces[0,3]]} < szemy{[eyes[0,0] + eyes[0,3]]}")
    # print(f"arcx{[faces[0,0] + faces[0,2]]} < szemx{[eyes[1,0] + eyes[1,2]]} VAGY arcy{[faces[0,1] + faces[0,3]]} < szemy{[eyes[1,0] + eyes[1,3]]}")

notreal = False

if  len(eyes) > 0 and len(faces) > 0 :
    # Jobb szem
     # Starting point
     # x kordináta x kordináta  vagy  y kordináta y kordináta
    if faces[0,0] > eyes[0,0] or faces[0,1] > eyes[0,1]:
        notreal = True
        print("Hibás pozíció 1")
    # End point
    if [faces[0,0] + faces[0,2]] < [eyes[0,0] + eyes[0,2]] or [faces[0,1] + faces[0,3]] < [eyes[0,0] + eyes[0,3]]:
        notreal = True
        print("Hibás pozíció 2")
    # Bal szem
    # Starting point
    if faces[0, 0] > eyes[1, 0] or faces[0, 1] > eyes[1, 1]:
        notreal = True
        print("Hibás pozíció 3")

    # End point
    if [faces[0, 0] + faces[0, 2]] < [eyes[1, 0] + eyes[1, 2]] or [faces[0, 1] + faces[0, 3]] < [eyes[1, 0] + eyes[1, 3]]:
        notreal = True
        print("Hibás pozíció 4")

 
if len(eyes) != 2 or len(faces) != 1 or notreal:
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    # org
    org = (40, 320)
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