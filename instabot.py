import cv2
import time
import subprocess

def video(seconds, frameRate):
    cap = cv2.VideoCapture(0)
    width = cap.get(3)
    height = cap.get(4)
    if(not cap.isOpened()):
        return "error"

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'hvc1')
    name = "/tmp/" + time.strftime("%d-%m-%Y_%X")+".mov"
    out = cv2.VideoWriter(name, fourcc, frameRate, (width,height))
    program_starts = time.time()
    result = subprocess.Popen(["ffprobe", name], stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell=True)
    nFrames=0
    while(nFrames<seconds*frameRate):
        ret, frame = cap.read()
        if ret==True:
            out.write(frame)
            nFrames += 1
        else:
            break
    cap.release()
    return name
# Store a video to /tmp for 2 seconds
print(video(2,15))