import face_recognition
import cv2
import numpy as np
import urllib.request
import json
import argparse
import time
import os, sys
from PIL import Image









def DownloadSingleFile(fileURL, cnt):
    print('Downloading image...')


    face_locations = []
    face_encodings = []
    folder='output/'
    fileName = 'insta' + str("%06d" % cnt) + '.jpg'

    try:
        req = urllib.request.urlopen(fileURL)
        arr=np.asarray(bytearray(req.read()),dtype="uint8")
        frame=cv2.imdecode(arr,-1)

        ## 받아오고 cv 변환
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

    # 얼굴검출
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)



        if(face_locations):
            # for (top, right, bottom, left), name in zip(face_locations, fileName):
            #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            #     top *= 4
            #     right *= 4
            #     bottom *= 4
            #     left *= 4
            #
            #     # Draw a box around the face
            #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            #
            #     # Draw a label with a name below the face
            #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            #     font = cv2.FONT_HERSHEY_DUPLEX
            #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imwrite(folder+'face/'+fileName, frame)
            print('Done. ' + fileName)
        else:
            cv2.imwrite(folder+'noface/'+fileName,frame)

    except Exception as e:
            print(str(e))
            print(fileURL)
            print("예외패스")
# import examples.crawler as crawler
if __name__ == '__main__':
    # os.system('python crawler.py hashtag -t 얼굴 -o ./output.json -n 3000')
    with open('output.json', encoding='UTF8') as data_file:
        data = json.load(data_file)
    for i in range(0, len(data)):
        instagramURL = data[i]['img_url']
        DownloadSingleFile(instagramURL, i)
