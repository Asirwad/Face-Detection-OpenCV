import cv2

try:
    trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    webcam = cv2.VideoCapture(0)

    while True:
        is_frame_read_success, frame = webcam.read()
        grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_coordinates = trained_face_data.detectMultiScale(grey_frame)
        print(face_coordinates)
        for coordinate in face_coordinates:
            (x, y, w, h) = coordinate
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("", frame)
        key = cv2.waitKey(1)

        # if q is pressed , exit
        if key in (81, 113):
            webcam.release()
            break

except Exception as e:
    print(e)