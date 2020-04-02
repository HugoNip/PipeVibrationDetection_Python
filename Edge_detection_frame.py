import cv2
import os

# path
video_dir = './Video_Source/'
video_path = os.path.join(video_dir,'C0002_Pipe.MP4')

def do_canny(frame):
    # Converts frame to grayscale because we only need the luminance channel for detecting edges - less computationally expensive
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # Applies a 5x5 gaussian blur with deviation of 0 to frame - not mandatory since Canny will do this for us
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Applies Canny edge detector with minVal of 50 and maxVal of 150
    canny = cv2.Canny(blur, 50, 150)
    return canny

cap = cv2.VideoCapture(video_path)
while (cap.isOpened()):
    ret, frame = cap.read()

    canny = do_canny(frame)

    cv2.imshow("canny", canny)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
