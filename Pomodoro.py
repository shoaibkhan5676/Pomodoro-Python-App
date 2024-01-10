




# ///////////////////////////////   POMODORO GUI APPLICATION      ///////////////////////////////

import tkinter
import math
import pygame.mixer
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
BLACK="#000000"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
vari=""
timer=None;
pygame.mixer.init()
audio_file="./MixSongs.wav"
second=0



def set_default():
    global reps
    global vari
    stop_audio() 
    canvas.itemconfig(timer_text,text="30:00")
    heading.config(text="Timer",font=(FONT_NAME,28),fg=GREEN,bg=BLACK);
    check_mark.config(text="",fg=GREEN,font=(FONT_NAME,20),bg=BLACK)
    reps=0
    vari=""

try:
    pygame.mixer.music.load(audio_file)
    print("Audio file loaded successfully!")
except pygame.error as e:
    print("Error loading audio file:", e)



def reset_button_function():
    window.after_cancel(timer)
    set_default()


def play_audio():
    pygame.mixer.music.play(loops=-1)

def stop_audio():
    pygame.mixer.music.stop()


def pause():
    global minutes
    global second
    mi=minutes
    sec=second
    pygame.mixer.music.pause()
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text=f"{mi:02d}:{sec:02d}")
    
def trigger():
    set_default()
    try:
        window.after_cancel(timer)
    except ValueError as e:
        pass      
    finally:
        start_countDown()



def resume_audio():
    global minutes
    global second
    resume_time=(minutes*60)+second
    pygame.mixer.music.unpause()
    count_Down(resume_time)




def count_Down(count):
    global timer
    global minutes
    global second

    minutes=int(count/60);
    second=math.ceil(count%60);
    if count>=0:
        canvas.itemconfig(timer_text,text=f"{minutes:02d}:{second:02d}")
        timer=window.after(1000,count_Down,count-1)
    else:
        global vari
        if reps==7:
            check_mark.config(text="😴",fg=RED)

        elif reps%2!=0:
            vari+="✔"
            check_mark.config(text=vari)
        
        start_countDown()




def start_countDown():
   
    global reps;
    reps+=1

    work_time=WORK_MIN*60;
    break_time=SHORT_BREAK_MIN*60;
    rest_time=LONG_BREAK_MIN*60;
    if reps<9:
        if reps==8:
            heading.config(text="Rest Time",fg=GREEN)
            stop_audio() 
            count_Down(rest_time)


        elif reps%2==0:
            heading.config(text="Break Time",fg=GREEN)
            stop_audio() 
            count_Down(break_time)
        else :
            heading.config(text="Work Time")
            play_audio()
            count_Down(work_time)        

   



window=tkinter.Tk();
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=BLACK,highlightthickness=0)



canvas=tkinter.Canvas(width=200,height=224,highlightthickness=0)
tomato_img=tkinter.PhotoImage(file="D:/Python Journey/PYTHON CODEBACKGROUND/Images/newimg.png")
canvas.create_image(102,112,image=tomato_img)
timer_text=canvas.create_text(102,130,text="30:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.config(bg=BLACK)
canvas.grid(column=1,row=1)





heading=tkinter.Label(text="Timer")
heading.config(font=(FONT_NAME,32),bg=BLACK,fg=GREEN)
heading.grid(column=1,row=0)



start_button=tkinter.Button(text="Start",command=trigger)
start_button.grid(column=0,row=2)


reset_button=tkinter.Button(text="Reset",command=reset_button_function)
reset_button.grid(column=2,row=2)

pause_button=tkinter.Button(text="Pause",command=pause)
pause_button.grid(column=0,row=4)

resume_button=tkinter.Button(text="Resume",command=resume_audio)
resume_button.grid(column=2,row=4)

check_mark=tkinter.Label()
check_mark.config(bg=BLACK,fg=GREEN,font=(FONT_NAME,28))
check_mark.grid(column=1,row=3)


window.mainloop()





















