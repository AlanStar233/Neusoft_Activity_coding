import cv2
import numpy as np
import torchvision.transforms as transforms

def cv2_BGR2Gray():
    image_path = "./likangju.jpg"
    image = cv2.imread(image_path)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('li', image)