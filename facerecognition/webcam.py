"""Webcam utilities."""

import cv2

import gfx


KEY_ENTER = 13#13 is the Enter Key


def capture():
    vc = cv2.VideoCapture(0, cv2.CAP_DSHOW) #captureDevice = camera
    # vc = cv2.VideoCapture(0)
    if vc.isOpened():
        _, frame = vc.read()
        return gfx.Image(frame)


def display():
    vc = cv2.VideoCapture(0)
    key = 0
    success = True

    face_detector = gfx.FaceDetector()

    while success and key != KEY_ENTER:
        success, frame = vc.read()
        face_detector.show(gfx.Image(frame), wait=False)
        key = cv2.waitKey(1)