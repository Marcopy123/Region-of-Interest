import cv2

width = 640
height = 360

windowName = "my WEBcam"

cam = cv2.VideoCapture(1,cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

evt = 0

xPos1 = 0
yPos1 = 0

xPos2 = 0
yPos2 = 0

def mouseClick(event, xPos, yPos, flags, params):
    global evt
    global xPos1
    global xPos2
    global yPos1
    global yPos2

    if event == cv2.EVENT_LBUTTONDOWN:
        xPos1, yPos1 = xPos, yPos
        evt = event

    if event == cv2.EVENT_LBUTTONUP:
        xPos2, yPos2 = xPos, yPos
        evt = event
    
    if event == cv2.EVENT_RBUTTONDOWN:
        evt = event

cv2.namedWindow(windowName)
cv2.setMouseCallback(windowName, mouseClick)

while True:
    ignore,  frame = cam.read()

    if evt == 4:
        new_frame = frame[yPos1:yPos2, xPos1:xPos2]
        cv2.rectangle(frame, (xPos1, yPos1), (xPos2, yPos2), (255, 0, 0), 2)
        cv2.imshow("Region of Interest", new_frame)
        cv2.moveWindow("Region of Interest", width, 0)
    
    if evt == 2:
        cv2.destroyWindow("Region of Interest")
        evt = 0

    cv2.imshow(windowName, frame)
    cv2.moveWindow(windowName, 0, 0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
