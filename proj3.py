import cv2
import numpy as np
import signal
import sys
import operator


# how many different classes of images we have
numberOfClass = range(1, 6)
# counter of each classes to calculate how many simiar number if image we have in each class
x=0
y = 0
z = 0
a = 0
b = 0
#we also can set test image path in here
#template = cv2.imread('Data/04/01.jpg')
#template = cv2.imread('Data/04/81.jpg',0)
template = cv2.imread(sys.argv[1],0)


for eachNum in numberOfClass:
    # all training set and training set range
    #in class 1 the image range is 1-86
    if eachNum == 1:
        numberOfVersion = range(1,86)
    if eachNum == 2:
        numberOfVersion = range(1,73)
    if eachNum == 3:
        numberOfVersion = range(1,89)
    if eachNum == 4:
        numberOfVersion = range(1,82)
    if eachNum == 5:
        numberOfVersion = range(1,87)
    for eachVer in numberOfVersion:
        if eachVer == 1 and eachNum == 1:
            img_bgr = cv2.imread('Data/01/01.png')
        else:
            if eachVer < 10:
                img_bgr = cv2.imread('Data/0'+str(eachNum)+'/0'+str(eachVer)+'.jpg')

            else:
                img_bgr = cv2.imread('Data/0'+str(eachNum)+'/'+str(eachVer)+'.jpg')

        img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.7

        if np.all(res > threshold):
            if eachNum == 1:

                x += 1

            if eachNum == 2:

                y += 1

            if eachNum == 3:
                z += 1

            if eachNum == 4:
                a += 1

            if eachNum == 5:
                b += 1


    CounterList = [x, y, z, a, b]

    index, value = max(enumerate(CounterList), key=operator.itemgetter(1))


if index == 0:
    print('Smile')
if index == 1:
    print('Hat')
if index == 2:
    print('Hash')
if index == 3:
    print('Heart')
if index == 4:
    print('Dollar')














