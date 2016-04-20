import cv2
import numpy as np
import time

window_size = 400
cap = cv2.VideoCapture(0)
cap.set(3, window_size)
cap.set(4, window_size)

cv2.namedWindow("window")
cv2.namedWindow("mask")
cv2.namedWindow("res")

cv2.moveWindow("window", 0, 0)
cv2.moveWindow("mask", window_size, 0)
cv2.moveWindow("res", window_size * 2, 0)

lower_bound = np.array([0,0,0])
upper_bound = np.array([0,0,0])
mouse_x = window_size / 2
mouse_y = window_size / 2
font = cv2.FONT_HERSHEY_SIMPLEX

def detect_hsv(event, x, y, flags, param):
    global mouse_x, mouse_y
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_x = x
        mouse_y = y
        
cv2.setMouseCallback("window", detect_hsv)

def print_hsv(frame, lower_bound, upper_bound):
    cv2.putText(frame, "lower_bound: " + str(lower_bound), (5,window_size - 20), font, 0.4, (0,255,255), 1)
    cv2.putText(frame, "upper_bound: " + str(upper_bound), (5,window_size - 40), font, 0.4, (0,255,255), 1)

def update(x):
    lower_bound[0] = cv2.getTrackbarPos("lower_hue", "window")
    lower_bound[1] = cv2.getTrackbarPos("lower_sat", "window")
    lower_bound[2] = cv2.getTrackbarPos("lower_val", "window")

    upper_bound[0] = cv2.getTrackbarPos("upper_hue", "window")
    upper_bound[1] = cv2.getTrackbarPos("upper_sat", "window")
    upper_bound[2] = cv2.getTrackbarPos("upper_val", "window")



cv2.createTrackbar("lower_hue", "window", 15, 180, update)
cv2.createTrackbar("lower_sat", "window", 0, 255, update)
cv2.createTrackbar("lower_val", "window", 91, 255, update)

cv2.createTrackbar("upper_hue", "window", 52, 180, update)
cv2.createTrackbar("upper_sat", "window", 255, 255, update)
cv2.createTrackbar("upper_val", "window", 255, 255, update)


update(-1)


sum_x_err  = 0
x_err = 0
last_x_err = 0
count = 0
sample_number = 20
while True:

    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    mask = cv2.erode(mask, None, iterations = 5)
    mask = cv2.dilate(mask, None, iterations = 5)
    res = cv2.bitwise_and(frame, frame, mask= mask)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    print "cnts = ", len(cnts)
    if len(cnts) > 0:
        c = max(cnts, key = cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if h > 3 * w:
            last_x_err = x_err
            x_err = window_size / 2 - x
            if abs(x_err - last_x_err) > 5:
                sum_x_err = 0
                count = 0
            elif count > sample_number:
                mean_x_err = sum_x_err / count
                sum_x_err = 0
                count = 0
                print "mean x err = ", mean_x_err
            else:
                print "x_err = ", x_err
                sum_x_err += x_err
                count += 1
                print "count = ", count
            print "got it!"
           
    hsv_text = str(hsv[mouse_x][mouse_y])
    cv2.putText(frame, hsv_text, (mouse_x, mouse_y), font, 0.8, (0, 0, 255), 1)
    cv2.circle(frame, (mouse_x, mouse_y), 10, (0, 0, 255))
    print_hsv(frame, lower_bound, upper_bound)

    cv2.imshow('window',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        cv2.imwrite("contour_test.png", frame)
        break

cv2.destroyAllWindows()
