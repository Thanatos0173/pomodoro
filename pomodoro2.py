import random
import tkinter as tk
import time
import segments as s
import sounds as so
import pause as p





def update(window,canvas,time):
    canvas.delete("all")
    s.seven_segment_display_digit(canvas,30,50,s.digitToTable(time[-6]))
    s.seven_segment_display_digit(canvas,130,50,s.digitToTable(time[-5]))
    s.seven_segment_display_digit(canvas,250,50,s.digitToTable(time[-4]))
    s.seven_segment_display_digit(canvas,350,50,s.digitToTable(time[-3]))
    s.seven_segment_display_digit_small(canvas,450,110,s.digitToTable(time[-2]))
    s.seven_segment_display_digit_small(canvas,500,110,s.digitToTable(time[-1]))

    canvas.create_oval(220,60,230,70,fill="green",outline="green",width=1)
    canvas.create_oval(220,140,230,150,fill="green",outline="green",width=1)
    canvas.create_oval(430,160,440,170,fill="green",outline="green",width=1)

    window.update()


def update2(window,canvas,doWork):
    canvas.delete("all")
    if doWork:
        s.wordToSegmentDisplay(canvas,"work",200,25,"green")
    else:
        s.wordToSegmentDisplay(canvas,"rest",200,25,"green")

    window.update()

def update3(window,canvas):
    canvas.delete("all")
    s.wordToSegmentDisplay(canvas,"pause",10,25, "green")
    s.wordToSegmentDisplay(canvas,"resume",280,25,"green")

    window.update()

def update4(window,canvas):
    canvas.delete("all")
    s.wordToSegmentDisplay(canvas,"start",10,25, "green")
    s.wordToSegmentDisplay(canvas,"stop",280,25,"green")

    window.update()



def clockwatch(window,duration,canvas,isPaused):
    last_second = round(time.time(),2)
    currentTime = duration
    while True:
        current_second = round(time.time(),2)
        window.update()
        if current_second != last_second: # A second elapsed
            last_second = current_second
            if not isPaused[0]:
                currentTime -= 0.01
                listToAdd = s.timeToSegmentConvertable(int(currentTime))
                if(len(str(round(currentTime,2)).split(".")[-1]) == 2):
                    listToAdd.append(str(round(currentTime,2))[-2])
                    listToAdd.append(str(round(currentTime,2))[-1])
                else:
                    listToAdd.append(str(round(currentTime,2))[-1])
                    listToAdd.append("0")
                update(window,canvas,listToAdd)
            if currentTime <= 0:
                so.play_sound_2()
                return




def start(window,canvas,isPaused):
    while True:
        for i in range(3):
            update2(window,canvas2,True)
            clockwatch(window,25*60,canvas,isPaused)
            update2(window,canvas2,False)
            clockwatch(window,300,canvas,isPaused)
        update2(window,canvas2,True)
        clockwatch(window,25*60,canvas,isPaused)
        update2(window,canvas2,False)
        clockwatch(window,15*60,canvas,isPaused)

isPaused = [False] # To be able to edit isPaused inside of function.

window = tk.Tk()
window.config(bg="#000000")
canvas = tk.Canvas(window,width=570,height=200)
canvas.config(bg="#000000")
canvas2 = tk.Canvas(window,width=570,height=110)
canvas2.config(bg="#000000")
canvas3 = tk.Canvas(window,width=570,height=110)
canvas3.config(bg="#000000")
canvas4 = tk.Canvas(window,width=570,height=110)
canvas4.config(bg="#000000")

so.play_sound_1()
canvas2.pack()
canvas.pack()
canvas3.pack()
canvas4.pack()
update3(window,canvas3)
update4(window,canvas4)

canvas3.bind('<Enter>', lambda event: p.on_enter(event,canvas3))
canvas3.bind('<Leave>', lambda event: p.on_leave(event,canvas3))
canvas3.bind('<Motion>', lambda event: p.on_motion(event,canvas3))
canvas3.bind('<Button-1>', lambda event: p.on_click(event,window, canvas3,isPaused))

canvas4.bind('<Enter>', lambda event: p.on_enter2(event,canvas4))
canvas4.bind('<Leave>', lambda event: p.on_leave2(event,canvas4))
canvas4.bind('<Motion>', lambda event: p.on_motion2(event,canvas4))
canvas4.bind('<Button-1>', lambda event: p.on_click2(event,window, canvas4,isPaused,start,canvas))
