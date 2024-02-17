import cv2
import os

video = cv2.VideoCapture(0)

facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

photoCount = 0

name = input("Enter your name: ")
PATH = 'images/' + name

if os.path.exists(PATH):
    print("Your name already exist in the database.")
    quit
else:
    os.makedirs(PATH)
    print("path created")
