import cv2
import os

if __name__=="__main__":
    faceCascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
    video_capture = cv2.VideoCapture(0)

    user_id = input("Input user_id: ")
    NUM_IMGS = 400
    if not os.path.exists('data/{}'.format(user_id)):
        os.mkdir('data/{}'.format(user_id))

    cnt = 1
    while cnt <= NUM_IMGS:
        print(cnt, end=' ')
        ret, frame = video_capture.read()
        cv2.imshow('Video', frame)
        cv2.imwrite("data/{}/{}_{:03d}.jpg".format(user_id, user_id, cnt), frame)
        cnt += 1
        key = cv2.waitKey(100)

    video_capture.release()
    cv2.destroyAllWindows()
