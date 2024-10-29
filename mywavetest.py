#ONCE CODE IS EXITED, MANUALLY DELETE THE APPENDED EXTRA HEADINGS IN THE HTML FILE OTHERWISE THERE WILL BE EXTRA LOGS WHEN RERUN
#BEFORE YOU RUN INSTALL THE FOLLOWING MODULES THROUGH CMD PROMPT/TERMINAL/POWERSHELL: pygame, roboflow, keyboard
#DO NOT SHARE API KEY WITH ANYONE OUTSIDE WAvE! IF YOU WANT TO SHARE THE CODE, DELETE THE API KEY SO NO ONE ELSE HAS ACCESS TO THE MODEL

#importing pygame for the camera
import pygame 
import pygame.camera

#This is for creating the global dataframe for streamlit access to update data vis
import numpy as np
import pandas as pd

#importing roboflow for the model api call (interchangeable model plug and play)pip
from roboflow import Roboflow

#os for image deletion and appending
import os

#time for sleep
import time

#webbrowser for html append
import webbrowser

#datetime for html update and keyboard for reload
from datetime import datetime
import keyboard

#subprocess for xcode build
import subprocess
from subprocess import call

#counter induces infinite loop MUST BE MANUALLY STOPPED OTHERWISE TOO MANY API CALLS UNECESSARILY
counter = 1
#Creating a df and array
log_array = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
df = pd.DataFrame(log_array, columns=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
# initializing  the camera; pygame camera from geeks for geeks tutorrial 
pygame.camera.init() 
  
# make the list of all available cameras 
camlist = pygame.camera.list_cameras()
filename = 'file:///'+os.getcwd()+'/' + 'wavewrite.html'
webbrowser.open_new_tab(filename) 

def get_df():
    df = pd.DataFrame(log_array, columns=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# if camera is detected or not 
while counter != 0:
    if camlist: 
 
        cam = pygame.camera.Camera(camlist[0], (640, 480)) 

        cam.start() 
 
        image = cam.get_image() 
  
        pygame.image.save(image, "image2.jpg") 
 
    else: 
        print("No camera on current device")
        quit() 

    #roboflow API Call (from the roboflow docs)
    rf = Roboflow(api_key="DCoxTb2e1y9IPD07P4sg")
    project = rf.workspace().project("wave-detect")
    model = project.version(1).model
    image = "image2.jpg"

    # infer on a local image print(model.predict(image, confidence=40, overlap=30).json())
    prediction = model.predict(image)
    print(prediction.json())
    #case for updating CRS (PLS MAKE SURE IN DEMO THAT THIS CASE MUST BE CHANGED TO IN, REMOVE THE NOT)
    # if "asleep" not in prediction:
    #     curTime = datetime.datetime.now().strftime("%H:%M:%S")
    #     curTimeList = []
    #     curTimeList.append(curTime)

    #removing the image for looping later; saves space only one image generated
    time.sleep(1.5)
    os.remove("image2.jpg")
    

    #case for updating CRS (PLS MAKE SURE IN DEMO THAT THIS CASE MUST BE CHANGED TO IN, REMOVE THE NOT)
    curTime = datetime.datetime.now().strftime("%H:%M:%S")
    cur_month = datetime.now().month
    if "asleep" not in prediction:
        log_array[cur_month] += 1


        #Used subprocess to build xcode project
        #build = f{"xcodebuild -project {WAvE_haptics_watch.xcodeproj} -scheme WAvE_haptics_watch -destination platform=watchOS Simulator,name=Series 9"}
        subprocess.run("xcodebuild -project WAvE_haptics_watch.xcodeproj -scheme WAvE_haptics_watch -destination platform=watchOS Simulator,name=Series 9", shell=True)

        #Keyboard was previous attempt at running the xcode project; did not work
        #keyboard.press_and_release('ctrl+r')

    time.sleep(1.5)
    os.remove("image2.jpg")
    time.sleep(1)