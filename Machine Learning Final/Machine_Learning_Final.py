# Distance, Direction
import cv2 as cv
import numpy as np
import time
import imutils
from imutils import paths


class Location ():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.focalLength = 0.69
        self.knownWidth = 24.0

    def getCenterX(self):
        return self.x

    def getCenterY(self):
        return self.y

    def getWidth(self):
        return self.w

    def getHeight(self):
        return self.h

    def distance_to_camera(self):
        # compute and return the distance from the maker to the camera
        return (self.knownWidth * self.focalLength) / self.w

    def getPos(self):
        return [self.x, self.y, round((self.knownWidth * self.focalLength) / self.w, 2)]


def YOLO(img):
    cv.imshow('window',  img)
    cv.waitKey(1)

    # Load names of classes and get random colors
    classes = open('obj.names').read().strip().split('\n')
    np.random.seed(42)
    colors = np.random.randint(0, 255, size=(len(classes), 3), dtype='uint8')

    # Give the configuration and weight files for the model and load the network.
    net = cv.dnn.readNetFromDarknet(
        'yolov3_custom_16_1000.cfg', 'yolov3_custom_16_1000.weights')
    net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
    # net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

    # determine the output layer
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # construct a blob from the image
    blob = cv.dnn.blobFromImage(
        img, 1/255.0, (416, 416), swapRB=True, crop=False)
    r = blob[0, 0, :, :]

    cv.imshow('blob', r)
    text = f'Blob shape={blob.shape}'
    # cv.displayOverlay('blob', text)
    print(text)
    cv.waitKey(1)

    net.setInput(blob)
    t0 = time.time()
    outputs = net.forward(ln)
    t = time.time()
    print('time=', t-t0)

    print(len(outputs))
    for out in outputs:
        print(out.shape)

    def trackbar2(x):
        confidence = x/100
        r = r0.copy()
        for output in np.vstack(outputs):
            if output[4] > confidence:
                x, y, w, h = output[:4]
                p0 = int((x-w/2)*416), int((y-h/2)*416)
                p1 = int((x+w/2)*416), int((y+h/2)*416)
                print('Blob: ', p0, p1)
                cv.rectangle(r, p0, p1, 1, 1)
        cv.imshow('blob', r)
        text = f'Bbox confidence={confidence}'
        print(text)

    r0 = blob[0, 0, :, :]
    r = r0.copy()
    cv.imshow('blob', r)
    cv.createTrackbar('confidence', 'blob', 50, 101, trackbar2)
    trackbar2(50)

    boxes = []
    confidences = []
    classIDs = []
    h, w = img.shape[:2]

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > 0.5:
                box = detection[:4] * np.array([w, h, w, h])
                (centerX, centerY, width, height) = box.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                box = [x, y, int(width), int(height)]
                boxes.append(box)
                confidences.append(float(confidence))
                classIDs.append(classID)
    centerList = []
    dimensionList = []
    indices = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    if len(indices) > 0:
        for i in indices.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            color = [int(c) for c in colors[classIDs[i]]]
            cv.rectangle(img, (x, y), (x + w, y + h), color, 2)
            text = "{}: {:.4f}".format(
                classes[classIDs[i]], confidences[i])
            print(text)
            X_center = x + (w / 2)
            Y_center = y + (h / 2)
            Ball = Location(X_center, Y_center, w, h)
            myList.append(Ball)
            cv.putText(img, text, (x, y - 5),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    cv.imshow('window', img)
    cv.waitKey(1)
    # cv.destroyAllWindows()


# def distance_to_camera(knownWidth, focalLength, perWidth):
    # compute and return the distance from the maker to the camera
    # return (knownWidth * focalLength) / perWidth


def check_pos(prev, curr):
    tolerance = 5

    if(curr[0] > prev[0] + 5):
        xMovement = 'Rightwards'
    elif(curr[0] < prev[0] - 5):
        xMovement = 'Leftwards'
    else:
        xMovement = 'Neither'

    if(curr[1] > prev[1] + 5):
        yMovement = 'Downwards'
    elif(curr[1] < prev[1] - 5):
        yMovement = 'Upwards'
    else:
        yMovement = 'Neither'

    if(curr[2] > prev[2] + 5):
        zMovement = 'Leaving'
    elif(curr[2] < prev[2] - 5):
        zMovement = 'Approaching'
    else:
        zMovement = 'Neither'

    text = "{}, {}, and {}".format(xMovement, yMovement, zMovement)
    cv.putText(img, text, (0, 50),
               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), thickness=2)


myList = []

# cap = cv.VideoCapture('Image/Video2.mp4')

cap = cv.VideoCapture(0)

count = 0

while(True):
    ret, img = cap.read()
    YOLO(img)
    if len(myList) >= 1:
        tempList = [[myList[-1].getCenterX(), myList[-1].getCenterY()],
                    [myList[-1].getWidth(), myList[-1].getHeight()], 0]
        if len(tempList) == 3:
            cm = myList[-1].distance_to_camera()
            cm *= 1000
            box = cv.cv.BoxPoints(
                tempList) if imutils.is_cv2() else cv.boxPoints(tempList)
            box = np.int0(box)
            cv.drawContours(img, [box], -1, (0, 255, 0), 2)
            cv.putText(img, "%.2fcm" % (cm),
                       (img.shape[1] - 300, img.shape[0] -
                        20), cv.FONT_HERSHEY_SIMPLEX,
                       2.0, (0, 255, 0), 3)

            print('Current Position: ', myList[-1].getPos())

        if len(myList) >= 2:
            check_pos(myList[-2].getPos(), myList[-1].getPos())
        cv.imshow("image", img)
        print('\n\n')

    count += 30
    cap.set(1, count)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
