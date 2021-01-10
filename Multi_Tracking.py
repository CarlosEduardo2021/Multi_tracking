import cv2
import sys
from random import randint

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']

def createTrackerByName(trackerType):
    if trackerType == tracker_types[0]:
        tracker = cv2.TrackerBoosting_create()
    elif trackerType == tracker_types[1]:
        tracker = cv2.TrackerMIL_create()
    elif trackerType == tracker_types[2]:
        tracker = cv2.TrackerKCF_create()
    elif trackerType == tracker_types[3]:
        tracker = cv2.TrackerTLD_create()
    elif trackerType == tracker_types[4]:
        tracker = cv2.TrackerMedianFlow()
    elif trackerType == tracker_types[5]:
        tracker = cv2.TrackerMOSSE_create()
    elif trackerType == tracker_types[6]:
        tracker = cv2.TrackerCSRT_create()
    else:
        tracker = None
        print('Nome incorreto')
        print('Os rastreados disponeveis são: ')
        for t in tracker_types:
            print(t)

    return tracker

#print(createTrackerByName('MIL8'))
#print(createTrackerByName('MIL'))

cap = cv2.VideoCapture('videos/race.mp4')

ok, frame = cap.read()
if not ok:
    print('Não é possivel ler o arquivo de video')
    sys.exit(1)

bboxex = []
colors = []

while True:
    bboxex = cv2.selectROI('MultiTracker', frame)
    bboxex.append(bboxex)
    colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))

    print('Pressione Q para sair das caixas de seleção e começar a rastrear ')
    print('Pressione qualquer outra tecla para selecionar o  próximo objeto')

    k = cv2.waitKey(0) & 0XFF
    if (k == 133):
        break

print('Caixas delimitadoras selecionadas {}'.format(bboxex))
print('Cores {}'.format(colors))