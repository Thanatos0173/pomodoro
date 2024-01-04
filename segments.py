# ==============================USED TO DEBUG==============================
def seven_segment_display_all(canvas,left_pos_x,left_pos_y):
    canvas.create_rectangle(left_pos_x,left_pos_y,left_pos_x+10,left_pos_y+50,fill = "green")
    canvas.create_rectangle(left_pos_x,left_pos_y+60,left_pos_x+10,left_pos_y+110,fill = "green")
    canvas.create_rectangle(left_pos_x+20,left_pos_y+50,left_pos_x+50,left_pos_y+60,fill = "green")
    canvas.create_rectangle(left_pos_x+20,left_pos_y-10,left_pos_x+50,left_pos_y,fill = "green")
    canvas.create_rectangle(left_pos_x+20,left_pos_y+110,left_pos_x+50,left_pos_y+120,fill = "green")
    canvas.create_rectangle(left_pos_x+60,left_pos_y,left_pos_x+70,left_pos_y+50,fill = "green")
    canvas.create_rectangle(left_pos_x+60,left_pos_y+60,left_pos_x+70,left_pos_y+110,fill = "green")

def seven_segment_display_all_small(canvas,left_pos_x,left_pos_y):
    canvas.create_rectangle(left_pos_x,left_pos_y,left_pos_x+5,left_pos_y+25,fill = "green")
    canvas.create_rectangle(left_pos_x,left_pos_y+30,left_pos_x+5,left_pos_y+55,fill = "green")
    canvas.create_rectangle(left_pos_x+10,left_pos_y+25,left_pos_x+25,left_pos_y+30,fill = "green")
    canvas.create_rectangle(left_pos_x+10,left_pos_y-5,left_pos_x+25,left_pos_y,fill = "green")
    canvas.create_rectangle(left_pos_x+10,left_pos_y+55,left_pos_x+25,left_pos_y+60,fill = "green")
    canvas.create_rectangle(left_pos_x+30,left_pos_y,left_pos_x+35,left_pos_y+25,fill = "green")
    canvas.create_rectangle(left_pos_x+30,left_pos_y+30,left_pos_x+35,left_pos_y+55,fill = "green")

def fourteen_segment_display_all_small(canvas,left_pos_x,left_pos_y):
    canvas.create_rectangle(left_pos_x,left_pos_y,left_pos_x+5,left_pos_y+25,fill = "green")
    canvas.create_rectangle(left_pos_x,left_pos_y+30,left_pos_x+5,left_pos_y+55,fill = "green")
    canvas.create_rectangle(left_pos_x+5,left_pos_y+25,left_pos_x+15,left_pos_y+30,fill = "green")
    canvas.create_rectangle(left_pos_x+20,left_pos_y+25,left_pos_x+30,left_pos_y+30,fill = "green")
    canvas.create_rectangle(left_pos_x+15,left_pos_y+1,left_pos_x+20,left_pos_y+25,fill = "green")
    canvas.create_rectangle(left_pos_x+15,left_pos_y+30,left_pos_x+20,left_pos_y+54,fill = "green")
    canvas.create_rectangle(left_pos_x+5,left_pos_y-5,left_pos_x+30,left_pos_y,fill = "green")
    canvas.create_rectangle(left_pos_x+5,left_pos_y+55,left_pos_x+30,left_pos_y+60,fill = "green")
    canvas.create_rectangle(left_pos_x+30,left_pos_y,left_pos_x+35,left_pos_y+25,fill = "green")
    canvas.create_rectangle(left_pos_x+30,left_pos_y+30,left_pos_x+35,left_pos_y+55,fill = "green")
    canvas.create_line(left_pos_x+6,left_pos_y-1,left_pos_x+14,left_pos_y+28,fill = "green",width=5)
    canvas.create_line(left_pos_x+6,left_pos_y+53,left_pos_x+15,left_pos_y+33,fill = "green",width=5)
    canvas.create_line(left_pos_x+30,left_pos_y-1,left_pos_x+22,left_pos_y+25,fill = "green",width=5)
    canvas.create_line(left_pos_x+27,left_pos_y+53,left_pos_x+22,left_pos_y+33,fill = "green",width=5)

#===========================================================================

def digitToTable(digit):
    match int(digit):
        case 0:
            return [1,1,1,1,1,1,0]
        case 1:
            return [0,1,1,0,0,0,0]
        case 2:
            return [1,1,0,1,1,0,1]
        case 3:
            return [1,1,1,1,0,0,1]
        case 4:
            return [0,1,1,0,0,1,1]
        case 5:
            return [1,0,1,1,0,1,1]
        case 6:
            return [1,0,1,1,1,1,1]
        case 7:
            return [1,1,1,0,0,0,0]
        case 8:
            return [1,1,1,1,1,1,1]
        case 9:
            return [1,1,1,1,0,1,1]

def textToTable(letter):
    match letter.upper():
        case "W":
            return [0,1,1,0,1,1,0,0,0,0,0,1,0,1]
        case "O":
            return [1,1,1,1,1,1,0,0,0,0,0,0,0,0]
        case "R":
            return [1,1,0,0,1,1,1,1,0,0,0,0,0,1]
        case "K":
            return [0,0,0,0,1,1,1,0,0,0,1,0,0,1]
        case "E":
            return [1,0,0,1,1,1,1,0,0,0,0,0,0,0]
        case "S":
            return [1,0,1,1,0,0,0,1,1,0,0,0,0,0]
        case "T":
            return [1,0,0,0,0,0,0,0,0,1,0,0,1,0]
        case "P":
            return [1,1,0,0,1,1,1,1,0,0,0,0,0,0]
        case "A":
            return [1,1,1,0,1,1,1,1,0,0,0,0,0,0]
        case "U":
            return [0,1,1,1,1,1,0,0,0,0,0,0,0,0]
        case "M":
            return [0,1,1,0,1,1,0,0,1,0,1,0,0,0]
        case "V":
            return [0,0,0,0,1,1,0,0,0,0,1,1,0,0]
        case "U":
            return [0,1,1,1,1,0,0,0,0,0,0,0,0,0]
        case "L":
            return [0,0,0,1,1,1,0,0,0,0,0,0,0,0]


def seven_segment_display_digit(canvas,left_pos_x,left_pos_y,truthTable):
    if truthTable[5]:
        canvas.create_rectangle(left_pos_x,left_pos_y,left_pos_x+10,left_pos_y+50,fill = "green")
    if truthTable[4]:
        canvas.create_rectangle(left_pos_x,left_pos_y+60,left_pos_x+10,left_pos_y+110,fill = "green")
    if truthTable[6]:
        canvas.create_rectangle(left_pos_x+20,left_pos_y+50,left_pos_x+50,left_pos_y+60,fill = "green")
    if truthTable[0]:
        canvas.create_rectangle(left_pos_x+20,left_pos_y-10,left_pos_x+50,left_pos_y,fill = "green")
    if truthTable[3]:
        canvas.create_rectangle(left_pos_x+20,left_pos_y+110,left_pos_x+50,left_pos_y+120,fill = "green")
    if truthTable[1]:
        canvas.create_rectangle(left_pos_x+60,left_pos_y,left_pos_x+70,left_pos_y+50,fill = "green")
    if truthTable[2]:
        canvas.create_rectangle(left_pos_x+60,left_pos_y+60,left_pos_x+70,left_pos_y+110,fill = "green")

def seven_segment_display_digit_small(canvas,left_pos_x,left_pos_y,truthTable):
    if truthTable[5]:
        canvas.create_rectangle(left_pos_x,left_pos_y,left_pos_x+5,left_pos_y+25,fill = "green")
    if truthTable[4]:
        canvas.create_rectangle(left_pos_x,left_pos_y+30,left_pos_x+5,left_pos_y+55,fill = "green")
    if truthTable[6]:
        canvas.create_rectangle(left_pos_x+10,left_pos_y+25,left_pos_x+25,left_pos_y+30,fill = "green")
    if truthTable[0]:
        canvas.create_rectangle(left_pos_x+10,left_pos_y-5,left_pos_x+25,left_pos_y,fill = "green")
    if truthTable[3]:
        canvas.create_rectangle(left_pos_x+10,left_pos_y+55,left_pos_x+25,left_pos_y+60,fill = "green")
    if truthTable[1]:
        canvas.create_rectangle(left_pos_x+30,left_pos_y,left_pos_x+35,left_pos_y+25,fill = "green")
    if truthTable[2]:
        canvas.create_rectangle(left_pos_x+30,left_pos_y+30,left_pos_x+35,left_pos_y+55,fill = "green")

def fourteen_segment_display_letter_small(canvas,left_pos_x,left_pos_y,truthTable,color):
    if truthTable[0]:
        canvas.create_rectangle(left_pos_x+5,left_pos_y-5,left_pos_x+30,left_pos_y,fill = color)#a
    if truthTable[1]:
        canvas.create_rectangle(left_pos_x+30,left_pos_y,left_pos_x+35,left_pos_y+25,fill = color)#b
    if truthTable[2]:
        canvas.create_rectangle(left_pos_x+30,left_pos_y+30,left_pos_x+35,left_pos_y+55,fill = color)#c
    if truthTable[3]:
        canvas.create_rectangle(left_pos_x+5,left_pos_y+55,left_pos_x+30,left_pos_y+60,fill = color)#d
    if truthTable[4]:
        canvas.create_rectangle(left_pos_x,left_pos_y+30,left_pos_x+5,left_pos_y+55,fill = color) #e
    if truthTable[5]:
        canvas.create_rectangle(left_pos_x,left_pos_y,left_pos_x+5,left_pos_y+25,fill = color)#f
    if truthTable[6]:
        canvas.create_rectangle(left_pos_x+5,left_pos_y+25,left_pos_x+15,left_pos_y+30,fill = color)#g1
    if truthTable[7]:
        canvas.create_rectangle(left_pos_x+20,left_pos_y+25,left_pos_x+30,left_pos_y+30,fill = color)#g2
    if truthTable[8]:
        canvas.create_line(left_pos_x+7,left_pos_y+3,left_pos_x+13,left_pos_y+23,fill = color,width=3)#h
    if truthTable[9]:
        canvas.create_rectangle(left_pos_x+15,left_pos_y+1,left_pos_x+20,left_pos_y+25,fill = color)#i
    if truthTable[10]:
        canvas.create_line(left_pos_x+27,left_pos_y+3,left_pos_x+22,left_pos_y+23,fill = color,width=3)#j
    if truthTable[11]:
        canvas.create_line(left_pos_x+7,left_pos_y+53,left_pos_x+13,left_pos_y+33,fill = color,width=3)#k
    if truthTable[12]:
        canvas.create_rectangle(left_pos_x+15,left_pos_y+30,left_pos_x+20,left_pos_y+54,fill = color)#l
    if truthTable[13]:
        canvas.create_line(left_pos_x+27,left_pos_y+53,left_pos_x+22,left_pos_y+33,fill = color,width=3)#m

def timeToSegmentConvertable(seconds):
    sec = "{:02}".format(int(seconds)%60)
    min = "{:02}".format(int(seconds/60))
    hour = "{:02}".format(int(seconds/3600))
    return list(hour + min + sec)

def wordToSegmentDisplay(canvas,word,x,y,color):
    for i in range(len(word)):
        fourteen_segment_display_letter_small(canvas,x + i*50,y,textToTable(word[i]),color)

def numberToSmallSegmentDisplay(canvas,word,x,y):
    for i in range(len(str(word))):
        seven_segment_display_digit_small(canvas,x + i*50,y,digitToTable(int(str(word)[i])))
