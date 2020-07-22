import tkinter
import cv2
import PIL.Image
import PIL.ImageTk
from functools import partial
import  threading
import imutils
import time


stream = cv2.VideoCapture('clip.mp4')
def play(speed):
    print(f"you click on play {speed}")
    # play vedio reverse direction
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1 + speed)

    grabbed,frame = stream.read()
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)


    canvas.create_text(129,30,fill="red",font="Times 27 bold ",text="decision pending")



def out():
    thread = threading.Thread(target=pending,args=("out",))
    thread.daemon = 1
    thread.start()
    print("player in out")

def pending(decision):
    # Display disicion pending image
    frame = cv2.cvtColor(cv2.imread("pending.jpg"),cv2.COLOR_BGR2RGBA)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    # wait for 1 second
    time.sleep(1)
    frame = cv2.cvtColor(cv2.imread("sponser.jpg"), cv2.COLOR_BGR2RGBA)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    # display sponser image
    # wait for 1.5 second
    time.sleep(1.5)
    if decision == 'out':
        decisionImg = "out.jpg"

    else:
         decisionImg = "notout.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGBA)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    # display out/not out image




def not_out():
    thread = threading.Thread(target=pending,args=("not out",))
    thread.daemon = 1
    thread.start()
    print("player in not out")


SET_WIDTH = 650
SET_HEIGHT = 368


window = tkinter.Tk()
window.title("bpm umpire revi")

cv_img = cv2.cvtColor(cv2.imread("bg.jpg"),cv2.COLOR_BGR2RGBA)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0, ancho=tkinter.NW, image=photo)
canvas.pack()

btn = tkinter.Button(window, text="<< Previous (fast)",width=50, command=partial(play,-25))
btn.pack()

btn = tkinter.Button(window, text="<< Previous (slow)",width=50,command=partial(play,-2))
btn.pack()

btn = tkinter.Button(window, text=" Forward (fast)>>",width=50,command=partial(play,25))
btn.pack()

btn = tkinter.Button(window, text="Forward (slow)>>",width=50,command=partial(play,2))
btn.pack()

btn = tkinter.Button(window, text="give out ",width=50,command=out)
btn.pack()

btn = tkinter.Button(window, text=" give not out",width=50,command=not_out)
btn.pack()

window.mainloop()