import cv2                          #emotion cascade se hora ha
import numpy as np                  
from keras.models import load_model #loading model
import time                         #calling sys time
import sys

def web_cam(face_detector,model,src=0,vid_rec = False):
    cap = cv2.VideoCapture(src)
    if not cap.isOpened():
        print("Can't start camera")
        sys.exit(0)
    faceCascade = face_detector
    font = cv2.FONT_HERSHEY_SIMPLEX
    emotions = {0:'Angry',1:'Fear',2:'Happy',3:'Sad',4:'Surprised',5:'Neutral'}

    emoji = []
    for index in range(6):
        emotion = emotions[index]
        emoji.append(cv2.imread('./emojis/' + emotion + '.png', -1)) #reading emojis


    frame_count = 0
    
    while 1:
        ret, frame = cap.read()    #read gui frame

        if not ret:
            print("No image from source")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    #color kaam to accuracy zada islye grey

        start_time = time.time() #sys time araha

        faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=7,minSize=(100, 100),)   

        y0 = 15
        for index in range(6):
            cv2.putText(frame, emotions[index] + ': ', (5, y0), font,
                        0.4, (0, 255, 255), 1, cv2.LINE_AA)
            y0 += 15

        try:
            FIRSTFACE = True
            if len(faces) > 0:
                for x, y, width, height in faces:
                    cropped_face = gray[y:y + height,x:x + width]
                    test_image = cv2.resize(cropped_face, (48, 48))
                    test_image = test_image.reshape([-1,48,48,1])

                    test_image = np.multiply(test_image, 1.0 / 255.0)
                    start_time = time.time()
                    if frame_count % 5 == 0:
                        probab = model.predict(test_image)[0] * 100
                        label = np.argmax(probab)
                        probab_predicted = int(probab[label])
                        predicted_emotion = emotions[label]
                        frame_count = 0

                    frame_count += 1
                    if FIRSTFACE:
                        y0 = 8
                        for score in probab.astype('int'):
                            cv2.putText(frame, str(score) + '% ', (80 + score, y0 + 8),
                                        font, 0.3, (0, 0, 255),1, cv2.LINE_AA)
                            cv2.rectangle(frame, (75, y0), (75 + score, y0 + 8),
                                          (0, 255, 0), cv2.FILLED)
                            y0 += 15
                            FIRSTFACE =False

                    font_size = width / 400
                    filled_rect_ht = int(height / 5)

                    emoji_face = emoji[(label)]
                    emoji_face = cv2.resize(emoji_face, (filled_rect_ht, filled_rect_ht))

                    emoji_x1 = x + width - filled_rect_ht
                    emoji_x2 = emoji_x1 + filled_rect_ht
                    emoji_y1 = y + height
                    emoji_y2 = emoji_y1 + filled_rect_ht

                    cv2.rectangle(frame, (x, y), (x + width, y + height),(255,0, 0),2)
                    cv2.rectangle(frame, (x-1, y+height), (x+1 + width, y + height+filled_rect_ht),
                                  (255, 0, 0),cv2.FILLED)
                    cv2.putText(frame, predicted_emotion+' '+ str(probab_predicted)+'%',
                                (x, y + height+ filled_rect_ht-10), font,font_size,(0,255,0), 1, cv2.LINE_AA)

                    for c in range(0, 3):
                        frame[emoji_y1:emoji_y2, emoji_x1:emoji_x2, c] = emoji_face[:, :, c] * \
                            (emoji_face[:, :, 3] / 255.0) + frame[emoji_y1:emoji_y2, emoji_x1:emoji_x2, c] * \
                            (1.0 - emoji_face[:, :, 3] / 255.0)

        except Exception as error:
            
            pass
        
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def main():
    
    face_detector = cv2.CascadeClassifier('./Xml_File/haarcascade_frontalface_default.xml') # cascade 
    emotion_model = load_model('./Xml_File/emotion_recognition.h5')   #model ha
    web_cam(face_detector,emotion_model)

if __name__ == '__main__':
    main()

