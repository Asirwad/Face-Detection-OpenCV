import cv2

try:
    trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    trained_smile_data = cv2.CascadeClassifier('haarcascade_smile.xml')
    webcam = cv2.VideoCapture(0)

    while True:
        is_frame_read_success, frame = webcam.read()
        grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_coordinates = trained_face_data.detectMultiScale(grey_frame)

        print(f"face_coordinates : {face_coordinates}")

        for face_coordinate in face_coordinates:
            (x, y, w, h) = face_coordinate
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)

            the_face = frame[y:y+h, x:x+w]
            face_grey = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)
            smile_coordinates = trained_smile_data.detectMultiScale(face_grey,
                                                                    scaleFactor=1.7,
                                                                    minNeighbors=20)

            for (x_s, y_s, w_s, h_s) in smile_coordinates:
                cv2.rectangle(the_face, (x_s, y_s), (x_s+w_s, x_s+h_s), (0, 0, 255), 2)

        cv2.imshow("", frame)
        key = cv2.waitKey(1)

        # if q is pressed , exit
        if key in (81, 113):
            webcam.release()
            break

except Exception as e:
    print(e)