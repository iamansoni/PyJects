import tkinter
import cv2  # pip install opencv-python
import PIL.Image  # pip install pillow
import PIL.ImageTk  # pip install pillow
from functools import partial
import threading
import time
import imutils

stream= cv2.VideoCapture('Decision Review System/clip.mp4')
flag = True

def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")

    #Play the video in reverse mode
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame= imutils.resize(frame, width =SET_WIDTH, height= SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0, image=frame, anchor= tkinter.NW)
    if flag:
        canvas.create_text(132, 29, fill= "red", font = "Times 27 bold", text = "Descion Pending")
    flag = not flag

def pending(decision):
    frame = cv2.cvtColor(cv2.imread("Decision Review System\pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor= tkinter.NW)

    time.sleep(1)

    frame = cv2.cvtColor(cv2.imread("Decision Review System\sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor= tkinter.NW)

    time.sleep(1.5)

    if decision=='out':
        decisionImg="Decision Review System\out.png"
    else:
        decisionImg="Decision Review System\img_not_out.png"

    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor= tkinter.NW)

def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out!")


def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out!")


# Width and height of our main screen

SET_WIDTH = 650
SET_HEIGHT = 368

# Tkinter GUI starts here
window = tkinter.Tk()
window.title("Third Umpire Decision Review System")
cv_img = cv2.cvtColor(cv2.imread(
    "Decision Review System\welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()

# Buttons to control playback
btn = tkinter.Button(window, text="<< Previous (FAST)",
                     width=50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< Previous (SLOW)",
                     width=50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Next (FAST)>>",
                     width=50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Next (SLOW)>>",
                     width=50, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text="Give Out", width=50, command=out)
btn.pack()

btn = tkinter.Button(window, text="Give Not Out", width=50, command=not_out)
btn.pack()

window.mainloop()
