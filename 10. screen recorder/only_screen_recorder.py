#importing the required packages
import pyautogui
import cv2
import numpy as np
import datetime
from win32api import GetSystemMetrics


def screen_recorder():
    #get the current date and time
    time_stamp=datetime.datetime.now()
    time_stamp=time_stamp.strftime('%Y-%m-%d %H-%M-%S')

    #Specifying the resolutions
    width=GetSystemMetrics(0)
    height=GetSystemMetrics(1)
    resolution=(width,height)

    #specify the video codec
    codec=cv2.VideoWriter_fourcc('m','p','4','v')

    #specify the name of the file
    filename=f"{time_stamp}.mp4"

    #specify the frames per second
    fps=60

    #creating the video writer object
    captured_video=cv2.VideoWriter(filename,codec,fps,resolution)

    #create an empty window
    cv2.namedWindow("Live",cv2.WINDOW_NORMAL)

    #Resize the window
    cv2.resizeWindow('Live', 1280, 720)

    #capture the webcam
    webcam=cv2.VideoCapture(0)

    while True:
        #take screenshot using python gui
        img=pyautogui.screenshot()

        #convert the screenshot to a numpy array
        img_np=np.array(img)

        #convert it from BGR to RGB
        img_np=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)

        #getting dimensions for the camera
        _, frame=webcam.read()
        frame_height,frame_width,_=frame.shape

        #imposing the camera frame on top of the final frame
        img_np[0:frame_height, 0:frame_width, :]= frame[0:frame_height, 0:frame_width, :]

        #write it to the output file
        captured_video.write(img_np)

        #display the recording screen
        cv2.imshow("Live",img_np)

        #display the webcam
        #cv2.imshow('webcam',frame)

        #stop recording when we press "q"
        if cv2.waitKey(1)==ord("q"):
            break

    #release the video writer
    captured_video.release()

    #destroy all windows
    cv2.destroyAllWindows()

Video_output=screen_recorder()

