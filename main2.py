from tkinter import *
from customtkinter import *
import pyttsx3

set_appearance_mode('dark')
# set_default_color_theme('green')
assist = pyttsx3.init()
voice = assist.getProperty('voices')

def speak(audio):
    assist.say(audio)
    assist.runAndWait()

def speak_btn_cmd():
    input_text = input_txt.get(1.0, 'end')
    speak(input_text)
    input_txt.delete(1.0, 'end')

def voice_opt_cmd(choice):
    global assist
    match choice:
        case 'Male':
            assist.setProperty('voice', voice[0].id)
        case 'Female':
            assist.setProperty('voice', voice[1].id)

def speed_opt_cmd(choice):
    global assist
    match choice:
        case 'Slow':
            assist.setProperty('rate', 120)
        case 'Normal':
            assist.setProperty('rate', 200)
        case 'Fast':
            assist.setProperty('rate', 280)

window = CTk()
window.title('Text to Speech')
window.configure(fg_color = ('#ebebeb','#242424'))
window.geometry('900x500')
window.resizable(False, False)

aside_frame = CTkFrame(master = window, width = 250, fg_color = ('#dbdbdb', '#2b2b2b'))
aside_frame.place(relheight = 1, relwidth = 0.3)

voice_lbl = CTkLabel(master = aside_frame, text = 'Voices', fg_color = ('#dbdbdb', '#2b2b2b'), text_color = ('#1a1a1a', '#dce4ee'), font = ('Arial', 20))
voice_lbl.place(relx = 0.5, rely = 0.3, anchor = E)
voice_options = CTkOptionMenu(master = aside_frame, values = ['Male', 'Female'], command = voice_opt_cmd)
voice_options.set('Female')
voice_options.place(relx = 0.5, rely = 0.37, anchor = CENTER)

speed_lbl = CTkLabel(master = aside_frame, text = 'Speed', fg_color = ('#dbdbdb', '#2b2b2b'), text_color = ('#1a1a1a', '#dce4ee'), font = ('Arial', 20))
speed_lbl.place(relx = 0.5, rely = 0.5, anchor = E)
speed_options = CTkOptionMenu(master = aside_frame, values = ['Slow', 'Normal', 'Fast'], command = speed_opt_cmd)
speed_options.set('Normal')
speed_options.place(relx = 0.5, rely = 0.57, anchor = CENTER)

title_lbl = CTkLabel(master = window, text = 'Text to Speech', font = ('Arial', 30), text_color = ('#1a1a1a', '#dce4ee'))
title_lbl.place(relx = 0.65, rely = 0.1, anchor = CENTER)

input_txt = CTkTextbox(master = window, height = 320, width = 550, font = ('Arial', 18), border_width = 10, border_color = ('#f9f9fa', '#1d1e1e'), corner_radius = 20)
input_txt.place(relx = 0.65, rely = 0.5, anchor = CENTER)

speak_btn = CTkButton(master = window, text = 'Speak', font = ('Arial', 20), height = 40, command = speak_btn_cmd)
speak_btn.place(relx = 0.65, rely = 0.9, anchor = CENTER)

window.mainloop()
