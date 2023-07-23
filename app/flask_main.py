from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Load the trained face data classifier
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def detect_faces(frame):
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grey_frame)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame


def video_stream():
    webcam = cv2.VideoCapture(0)

    while True:
        is_frame_read_success, frame = webcam.read()
        if not is_frame_read_success:
            break
        frame_with_faces = detect_faces(frame)

        # Convert the frame to JPEG format
        ret, jpeg = cv2.imencode('.jpg', frame_with_faces)

        # Yield the JPEG data as bytes to stream the video
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

        key = cv2.waitKey(1)

        if key in (81, 113):
            webcam.release()
            break


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
