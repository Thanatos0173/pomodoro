import segments as s
import sounds as so

def pause(window,canvas,isPaused):
    isPaused[0] = True

def resume(window,canvas,isPaused):
    isPaused[0] = False



def on_enter(event,canvas):
    global is_left
    is_left = 0 <= event.x <= canvas.winfo_width() // 2 - 30
    if is_left:
        s.wordToSegmentDisplay(canvas,"pause",10,25, "red")
    else:
        s.wordToSegmentDisplay(canvas,"resume",280,25, "red")


def on_leave(event,canvas):
    global is_left
    is_left = 0 <= event.x <= canvas.winfo_width() // 2 - 30
    if is_left:
        s.wordToSegmentDisplay(canvas,"pause",10,25, "green" )
    else:
        s.wordToSegmentDisplay(canvas,"resume",280,25,"green")


def on_motion(event,canvas):
    global is_left
    new_is_left = 0 <= event.x <= canvas.winfo_width() // 2 - 30
    if new_is_left != is_left:
        is_left = new_is_left
        if not is_left:
            s.wordToSegmentDisplay(canvas,"resume",280,25, "red")
            s.wordToSegmentDisplay(canvas,"pause",10,25, "green" )
        else:
            s.wordToSegmentDisplay(canvas,"pause",10,25, "red")
            s.wordToSegmentDisplay(canvas,"resume",280,25,"green")

def on_click(event,window, canvas,isPaused):
    half_clicked = "Left" if event.x <= canvas.winfo_width() // 2 else "Right"
    if half_clicked == "Left" and not isPaused[0]:
        pause(window,canvas,isPaused)
        so.play_sound_1()

    elif half_clicked == "Left" and isPaused[0]:
        pause(window,canvas,isPaused)
        so.play_sound_3()
    elif half_clicked == "Right" and isPaused[0]:
        resume(window,canvas,isPaused)
        so.play_sound_1()
    elif half_clicked == "Right" and not isPaused[0]:
        resume(window,canvas,isPaused)
        so.play_sound_3()
    else: None
