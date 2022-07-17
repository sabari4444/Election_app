from tkinter import *
from tkinter import messagebox

import os

# Current dir
dir_ = os.getcwd()

# Window
window = Tk()
window.geometry("1366x768")
window.title('Vote')
window.iconbitmap(fr'{dir_}\Elements\vote.ico')
window.configure(bg="#ffffff")

# Variables
value = StringVar()
n = 4
names = []
voted = []
# Canvas
canvas = Canvas(
    window,
    bg="#ffffff",
    height=768,
    width=1366,
    bd=0,
    highlightthickness=0,
    relief="ridge")

# Elements
# main win
background_img = PhotoImage(file=fr"{dir_}\Elements\bg.png")
entry0_img = PhotoImage(file=fr"{dir_}\Elements\img_textBox0.png")
red_entry = PhotoImage(file=fr'{dir_}\Elements\entry_red.png')
con = PhotoImage(file=fr"{dir_}\Elements\continue_.png")

# window 2
bg = PhotoImage(file=fr'{dir_}\Elements-2\background1.png')
done_btn = PhotoImage(file=fr'{dir_}\Elements-2\done.png')
c1_wh_img = PhotoImage(file=fr'{dir_}\Elements-2\candidates\c1-wh.png')
c1_bl_img = PhotoImage(file=fr'{dir_}\Elements-2\candidates\c1-b.png')
c2_wh_img = PhotoImage(file=fr'{dir_}\Elements-2\candidates\c2-wh.png')
c2_bl_img = PhotoImage(file=fr'{dir_}\Elements-2\candidates\c2-b.png')
c3_wh_img = PhotoImage(file=fr'{dir_}\Elements-2\candidates\c3-wh.png')
c3_bl_img = PhotoImage(file=fr'{dir_}\Elements-2\candidates\c3-b.png')
c4_wh_img = PhotoImage(file=fr'{dir_}\Elements-2\candidates\c4-wh.png')
c4_bl_img = PhotoImage(file=fr'{dir_}\Elements-2\candidates\c4-b.png')
c5_wh_img = PhotoImage(file=fr'{dir_}\Elements-2\candidates\c5-wh.png')
c5_bl_img = PhotoImage(file=fr'{dir_}\Elements-2\candidates\c5-b.png')
c6_wh_img = PhotoImage(file=fr'{dir_}\Elements-2\candidates\c6-wh.png')
c6_bl_img = PhotoImage(file=fr'{dir_}\Elements-2\candidates\c6-b.png')

# win 3
img_3 = PhotoImage(file=fr'{dir_}\Elements-2\3sec.png')
img_2 = PhotoImage(file=fr'{dir_}\Elements-2\2sec.png')
img_1 = PhotoImage(file=fr'{dir_}\Elements-2\1 sec.png')
background_img3 = PhotoImage(file=fr"{dir_}\Elements-2\Loding.png")

# result page
bg3 = PhotoImage(file=fr'{dir_}\result page\bg.png')
resu = PhotoImage(file=fr'{dir_}\result page\result.png')


class Window_1:

    def result_win(self):
        top = Toplevel(window)
        top.geometry('700x768')
        top.title('Result')
        canvas1 = Canvas(
            top,
            bg="#ffffff",
            height=760,
            width=700,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas1.place(x=0, y=0)
        canvas1.create_image(350, 384, image=bg3)
        l0 = Label(canvas1,text='0',
                   bg='#D9D9D9',
                   font=("Comic Sans MS", 20, "roman"),
                   fg='#000000')
        l1 = Label(canvas1, text='0',
                   bg='#D9D9D9',
                   font=("Comic Sans MS", 20, "roman"),
                   fg='#000000')
        l2 = Label(canvas1, text='0',
                   bg='#D9D9D9',
                   font=("Comic Sans MS", 20, "roman"),
                   fg='#000000')
        l3 = Label(canvas1, text='0',
                   bg='#D9D9D9',
                   font=("Comic Sans MS", 20, "roman"),
                   fg='#000000')
        l4 = Label(canvas1, text='0',
                   bg='#D9D9D9',
                   font=("Comic Sans MS", 20, "roman"),
                   fg='#000000')
        l5 = Label(canvas1, text='0',
                   bg='#D9D9D9',
                   font=("Comic Sans MS", 20, "roman"),
                   fg='#000000')
        file3 = open(fr'{dir_}\Data\VotedList.txt', 'r')
        lines = file3.readlines()
        for i in lines:
            _, vote = i.split('-')
            vote = vote.strip('\n')
            global voted
            voted.append(vote)

        def calulate_vote(lis):
            dic = {'c1': 0, 'c2': 0, 'c3': 0, 'c4': 0, 'c5': 0,'c6': 0}
            a = lis.count('c1')
            b = lis.count('c2')
            c = lis.count('c3')
            d = lis.count('c4')
            e = lis.count('c5')
            f = lis.count('c6')
            l0.configure(text=a)
            l1.configure(text=b)
            l2.configure(text=c)
            l3.configure(text=d)
            l4.configure(text=e)
            l5.configure(text=f)

        calulate_vote(voted)
        l0.place(x=480, y=170)
        l1.place(x=480, y=270)
        l2.place(x=480, y=370)
        l3.place(x=480, y=470)
        l4.place(x=480, y=570)
        l5.place(x=480, y=670)
        top.mainloop()

    class Win3:
        def __init__(self):
            def clear():
                global n
                n = 4
                canvas.delete('all')
                label1.destroy()
                Window_1()

            def load():
                global n
                n -= 1
                if n > 0:
                    if n == 2:
                        label1.config(image=img_2)
                        window.after(1000, load)
                    elif n == 1:
                        label1.config(image=img_1)
                        window.after(1000, load)
                    elif n == 3:
                        file2 = open(fr'{dir_}\Data\VotedList.txt', 'a')
                        file2.write(f'{user_name}-{vote_option}\n')
                        file2.close()
                        window.after(1000, load)
                elif n == 0:
                    clear()

            canvas.create_image(
                682, 365.0,
                image=background_img3)
            label1 = Label(window, text="Please Wait It Won't take More Than 3 Seconds", image=img_3, bg='#A876E8')
            label1.place(x=150, y=415)
            load()

    class Win2:
        def clear_w2(self1):

            canvas.delete('all')
            self1.btn_w2_0.destroy()
            self1.c1.destroy()
            self1.c2.destroy()
            self1.c3.destroy()
            self1.c4.destroy()
            self1.c5.destroy()
            self1.c6.destroy()
            Window_1.Win3()

        def can1(self1):
            self1.c1.configure(image=c1_bl_img)
            self1.c2.configure(image=c2_wh_img)
            self1.c3.configure(image=c3_wh_img)
            self1.c4.configure(image=c4_wh_img)
            self1.c5.configure(image=c5_wh_img)
            self1.c6.configure(image=c6_wh_img)
            global vote_option
            vote_option = "c1"

        def can2(self1):
            self1.c1.configure(image=c1_wh_img)
            self1.c2.configure(image=c2_bl_img)
            self1.c3.configure(image=c3_wh_img)
            self1.c4.configure(image=c4_wh_img)
            self1.c5.configure(image=c5_wh_img)
            self1.c6.configure(image=c6_wh_img)
            global vote_option
            vote_option = "c2"

        def can3(self1):
            self1.c1.configure(image=c1_wh_img)
            self1.c2.configure(image=c2_wh_img)
            self1.c3.configure(image=c3_bl_img)
            self1.c4.configure(image=c4_wh_img)
            self1.c5.configure(image=c5_wh_img)
            self1.c6.configure(image=c6_wh_img)
            global vote_option
            vote_option = "c3"

        def can4(self1):
            self1.c1.configure(image=c1_wh_img)
            self1.c2.configure(image=c2_wh_img)
            self1.c3.configure(image=c3_wh_img)
            self1.c4.configure(image=c4_bl_img)
            self1.c5.configure(image=c5_wh_img)
            self1.c6.configure(image=c6_wh_img)
            global vote_option
            vote_option = "c4"

        def can5(self1):
            self1.c1.configure(image=c1_wh_img)
            self1.c2.configure(image=c2_wh_img)
            self1.c3.configure(image=c3_wh_img)
            self1.c4.configure(image=c4_wh_img)
            self1.c5.configure(image=c5_bl_img)
            self1.c6.configure(image=c6_wh_img)
            global vote_option
            vote_option = "c5"

        def can6(self1):
            self1.c1.configure(image=c1_wh_img)
            self1.c2.configure(image=c2_wh_img)
            self1.c3.configure(image=c3_wh_img)
            self1.c4.configure(image=c4_wh_img)
            self1.c5.configure(image=c5_wh_img)
            self1.c6.configure(image=c6_bl_img)
            global vote_option
            vote_option = "c6"

        def __init__(self1, self):
            canvas.delete('all')
            self.entry0.destroy()
            self.entry0_bg.destroy()
            self.b0.destroy()
            self.b1.destroy()

            canvas.create_image(680,
                                355,
                                image=bg)
            self1.c1 = Button(image=c1_wh_img,
                        borderwidth=0,
                        command=lambda: Window_1.Win2.can1(self1),
                        highlightthickness=0,
                        bg='#C2BABA',
                        activebackground='#C2BABA')

            self1.c2 = Button(image=c2_wh_img,
                        borderwidth=0,
                        command=lambda: Window_1.Win2.can2(self1),
                        highlightthickness=0,
                        bg='#C2BABA',
                        activebackground='#C2BABA')

            self1.c3 = Button(image=c3_wh_img,
                        borderwidth=0,
                        command=lambda: Window_1.Win2.can3(self1),
                        highlightthickness=0,
                        bg='#C2BABA',
                        activebackground='#C2BABA')

            self1.c4 = Button(image=c4_wh_img,
                        borderwidth=0,
                        command=lambda: Window_1.Win2.can4(self1),
                        highlightthickness=0,
                        bg='#C2BABA',
                        activebackground='#C2BABA')

            self1.c5 = Button(image=c5_wh_img,
                        borderwidth=0,
                        command=lambda: Window_1.Win2.can5(self1),
                        highlightthickness=0,
                        bg='#C2BABA',
                        activebackground='#C2BABA')

            self1.c6 = Button(image=c6_wh_img,
                        borderwidth=0,
                        command=lambda: Window_1.Win2.can6(self1),
                        highlightthickness=0,
                        bg='#C2BABA',
                        activebackground='#C2BABA')
            self1.btn_w2_0 = Button(image=done_btn,
                          borderwidth=0,
                          highlightthickness=0,
                          activebackground='#D9D9D9',
                          command=lambda: Window_1.Win2.clear_w2(self1),
                          bg='#D9D9D9',
                          relief='flat')

            self1.btn_w2_0.place(x=1200,
                           y=630)

            self1.c1.place(x=240,
                     y=220)

            self1.c2.place(x=240,
                     y=340)

            self1.c3.place(x=240,
                     y=460)

            self1.c4.place(x=680,
                     y=220)

            self1.c5.place(x=680,
                     y=340)

            self1.c6.place(x=680,
                     y=460)


    def done(self, name):
        global user_name
        user_name = name
        if name == '':
            self.entry0_bg.configure(image=red_entry)
            self.entry0.configure(bg='#F80000')
            messagebox.showerror("Error", "Error: Enter Your Name !!")

        else:
            self.entry0.delete("0", "end")
            self.entry0_bg.configure(image=entry0_img)
            self.entry0.configure(bg='#c7c9fc')
            file0 = open(fr'{dir_}\Data\NameList.txt', 'r')
            f0 = file0.readlines()
            file0.close()
            if name in f0 or name + '\n' in f0:
                file1 = open(fr'{dir_}\Data\VotedList.txt', 'r')
                f1 = file1.readlines()
                file1.close()
                if len(f1) > 0:
                    for i in f1:
                        n_name, candidate_voted = i.split('-')
                        names.append(n_name)
                    if name in names:
                        self.entry0_bg.configure(image=red_entry)
                        self.entry0.configure(bg='#F80000')
                        messagebox.showerror("You already voted ", "Error: you voted already")
                    else:
                        Window_1.Win2(self)
                else:
                    Window_1.Win2(self)
            else:
                messagebox.showerror("You Dont Have A Vote ", "Error: You Dont Have A Vote Go Register Your Name")

    def __init__(self):
        canvas.create_image(
            682.0, 382.5,
            image=background_img)

        # Entry
        self.entry0_bg = Label(
            canvas,
            image=entry0_img,
            bg='#A969F1')

        self.entry0 = Entry(
            canvas,
            bd=0,
            bg="#c7c9fc",
            highlightthickness=0,
            textvariable=value,
            font='Arial 40',
            fg='#A969F1')

        # Buttons
        self.b0 = Button(
            image=con,
            borderwidth=0,
            highlightthickness=0,
            activebackground='#A969F1',
            bg='#A969F1',
            command=lambda: Window_1.done(self, name=value.get()),
            relief="flat")
        self.b1 = Button(
            image=resu,
            borderwidth=0,
            highlightthickness=0,
            activebackground='#C7C9FC',
            bg='#C7C9FC',
            command=lambda: Window_1.result_win(self))

        # Placing Elements

        canvas.place(x=0, y=0)

        self.entry0_bg.place(x=78,
                        y=417)

        self.entry0.place(
            x=93,
            y=425,
            width=382.0,
            height=90)

        self.b0.place(
            x=739,
            y=547,
            width=627,
            height=197)

        self.b1.place(
            x=1050,
            y=40,
            width=297,
            height=101)

        window.mainloop()
Window_1()