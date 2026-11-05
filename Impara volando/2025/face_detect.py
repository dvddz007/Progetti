import cv2
 
def getArea(face, img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.1, 8)
    if len(faces) > 0:
        x, y, w, h = faces[0]
        cv2.putText(img, f"{w*h}", (10, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)
        return w * h
    return None
# se l'area è minore 30_000 si avvicina
# se l'earea è maggiore di 110_000 si allontana


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
    
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray, 1.1, 8)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
        getArea(face, frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
