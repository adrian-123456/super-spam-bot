#Import modules
import pyautogui
import time
import tkinter as tk
import random

#Define informations

#Load default wordlist
wordlist = []
wordlist.append('super')
wordlist.append('spam')
wordlist.append('bot')

#Define GUIs
def maingui_load():
    #Define WordlistGUI
    def wordlistgui():
        def add_word_to_list():
            wordlist_entry_text = wordlist_entry.get()
            wordlist.append(wordlist_entry_text)
            wordlist_box.insert(len(wordlist), wordlist_entry_text)
            wordlist_entry.delete(first=0, last=len(wordlist_entry.get()))
        
        def delete_selected_item():
            selected_index = wordlist_box.curselection()
            if selected_index:
                wordlist_box.delete(selected_index[0])  # Delete only the first selected item
                wordlist.remove(wordlist[selected_index[0]])
        
        #Start up GUI
        wordlistgui = tk.Tk(className=' Adjust Words')
        #Load list
        wordlist_box = tk.Listbox(master = wordlistgui, font = ('Arial', 16))
        for x in range(len(wordlist)):
            wordlist_box.insert(x, wordlist[x])
        wordlist_box.pack(padx=10, pady=5, side=tk.LEFT)
        #Label
        wordlist_label = tk.Label(master = wordlistgui, text = 'Enter text below to add spam items', font = ('Arial', 12))
        wordlist_label.pack(padx=10, pady=3)
        #Entry box
        wordlist_entry = tk.Entry(master = wordlistgui, font = ('Arial', 14))
        wordlist_entry.pack(pady=10)
        #Entry submit button
        wordlist_submit_btn = tk.Button(master = wordlistgui, text = 'Add to list', font=('Arial', 15), command = add_word_to_list)
        wordlist_submit_btn.pack(pady=10)
        #Delete item button
        wordlist_del_btn = tk.Button(master=wordlistgui, text='''Delete
Selected Item''', font=('Arial', 15), command=delete_selected_item)
        wordlist_del_btn.pack(pady=10)
        #Loop GUI
        wordlistgui.mainloop()
    
    #Define spam button
    def SPAM():
        SPAM_timestorepeat = repeat_entry.get()
        SPAM_delay1 = int(delay_1.get())
        SPAM_delay2 = int(delay_2.get())
        SPAM_input_type = int(input_type_var.get())
        #If input is numeric:
        if repeat_entry.get().isnumeric() == True:
            global main_bottom
            main_bottom.config(text=f'Starting in {SPAM_delay1} seconds...')
            maingui.update()
            time.sleep(SPAM_delay1)
            #Pick a random word and print it (convert into pyautogui '.typewrite' later on)
            if SPAM_input_type == 0:
                for x in range(int(repeat_entry.get())):
                    main_bottom.configure(text=f'Completed round {x}/{SPAM_timestorepeat}')
                    maingui.update()
                    pyautogui.typewrite(random.choice(wordlist))
                    pyautogui.press('enter')
                    time.sleep(SPAM_delay2)
            elif SPAM_input_type == 1:
                for x in range(int(repeat_entry.get())):
                    main_bottom.configure(text=f'Completed round {x}/{SPAM_timestorepeat}')
                    maingui.update()
                    pyautogui.typewrite(wordlist[x % len(wordlist)])
                    pyautogui.press('enter')
                    time.sleep(SPAM_delay2)
            main_bottom.configure(text='Completed!')
            maingui.update()
        else:
            #Error message
            main_bottom.configure(text='Please only input numbers.')
            maingui.update()
            repeat_entry.delete(first=0, last=len(repeat_entry.get()))
    #Start up GUI
    maingui = tk.Tk(className=' SuperSpam Bot')
    #Heading
    heading = tk.Label(master=maingui, text='Thanks for using SuperSpam Bot!', underline=1, font=('Arial', 20))
    heading.pack(padx=10, pady=6)
    #Left frame
    main_left_frame = tk.Frame(maingui)
    main_left_frame.pack(side=tk.LEFT, padx=10, pady=3)
    #Word list button
    word_list_btn = tk.Button(master=main_left_frame, text='Adjust Words', command=wordlistgui, font=('Arial', 16))
    word_list_btn.pack(padx=5, pady=3)
    #Slider - Starting Delay
    delay_1=tk.DoubleVar(main_left_frame)
    start_delay = tk.Scale(main_left_frame, label='Starting Delay', orient=tk.HORIZONTAL, variable=delay_1, from_=1, to=10, resolution=0.5)
    start_delay.pack(padx=5,pady=3)
    #Slider - Interval Delay
    delay_2=tk.DoubleVar(main_left_frame)
    interval_delay = tk.Scale(main_left_frame, label='Interval Delay', orient=tk.HORIZONTAL, variable=delay_2, from_=0, to=10, resolution=0.2)
    interval_delay.pack(padx=5,pady=3)
    #Right frame
    main_right_frame = tk.Frame(maingui)
    main_right_frame.pack(side = tk.RIGHT, padx=10, pady=3)
    #Start spam button
    start_btn = tk.Button(master=main_right_frame, text='START SPAM', command=SPAM, font=('Arial', 25), fg='red')
    start_btn.pack(padx=10, pady=3)
    #Times to repeat frame
    repeat_frame = tk.Frame(master=main_right_frame)
    repeat_frame.pack(pady=3)
    #Times to repeat desc
    repeat_desc = tk.Label(master=repeat_frame, text = 'Times to repeat:')
    repeat_desc.pack(padx=10, pady=3, side=tk.LEFT)
    #Times to repeat entry
    global times_to_repeat
    repeat_entry = tk.Entry(master=repeat_frame, width=6)
    repeat_entry.pack(padx=10, pady=3, side=tk.RIGHT)
    #Bottom text
    global main_bottom
    main_bottom = tk.Label(main_right_frame, text='Made by Adrian :)')
    main_bottom.pack(pady=3, side=tk.BOTTOM)
    #input_type Frame
    input_type_frame = tk.Frame(main_right_frame)
    input_type_frame.pack()
    #input_type Label
    input_type_label = tk.Label(input_type_frame, text='Input type:')
    input_type_label.pack()
    #input_type defining
    global input_type_var
    input_type_var = tk.IntVar()
    #input_type Random
    input_type_random = tk.Radiobutton(input_type_frame, text='Random', variable=input_type_var, value=0)
    input_type_random.pack(side=tk.LEFT)
    #input_type Ordered
    input_type_ordered = tk.Radiobutton(input_type_frame, text='Ordered', variable = input_type_var, value=1)
    input_type_ordered.pack(side=tk.RIGHT)
    #Loop GUI
    maingui.mainloop()

##Run script
maingui_load() #Open Main GUI
