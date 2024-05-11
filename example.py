import cv2
import mediapipe as mp
import itertools
import math
import numpy as np
import cvzone
import csv
from threading import Thread
from cvzone.FaceMeshModule import FaceMeshDetector
import time


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
co=0


LEFT_EYE_INDEXES = list(set(itertools.chain(*mp_face_mesh.FACEMESH_LEFT_EYE)))

RIGHT_EYE_INDEXES = list(set(itertools.chain(*mp_face_mesh.FACEMESH_RIGHT_EYE)))
# print(RIGHT_EYE_INDEXES)

FACEMESH_FACE_OVAL_INDEXES = list(set(itertools.chain(*mp_face_mesh.FACEMESH_FACE_OVAL)))
# print((FACEMESH_FACE_OVAL_INDEXES))

FACEMESH_TESSELATION_INDEXES = list(set(itertools.chain(*mp_face_mesh.FACEMESH_TESSELATION)))
# print(FACEMESH_TESSELATION_INDEXES)

def cam_distance():
    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        # Drawing
        cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.3