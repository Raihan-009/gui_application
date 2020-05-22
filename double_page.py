from tkinter import *
from tkinter import messagebox
import smtplib

if __name__ == "__main__" :
    pro = Tk()
    pro.geometry("450x575+325+40")
    pro.resizable(0, 0)
    pro.title("MAIL APPLICATION")
    # pro.configure(background = "light green")
    label = Label(pro, text="please Log In First", height=2)
    label.configure(font="Mimmo 18")
    label.pack(side=TOP)

    user_icon = PhotoImage(file="F:/Python_with_Atom/gui_mail_pplication/login.png")
    label0 = Label(pro, image=user_icon)
    label0.pack(side=TOP)

    label0 = Label(pro, fg='red', text="\nBefore log in, please\n"
                                       "Allow less secure apps: ON\n")
    label0.configure(font="Mimmo 15")
    label0.pack(side=TOP)

    frame = Frame(pro, width=450, height=300)
    # frame.configure(background = 'Light Green')
    frame.pack(side=TOP)

    m_mail = StringVar(frame)
    m_pass = StringVar(frame)

    frame_label = Label(frame, text="Email ID :")
    frame_label.configure(font='Impact 12')
    frame_label.grid(row=1, column=1)

    frame_entry1 = Entry(frame, textvariable=m_mail, width=30, bd=4, bg='light grey')
    frame_entry1.grid(row=1, column=2)
    # m_mail.set("Enter Your Mail Address")

    frame_label1 = Label(frame, text="Password :")
    frame_label1.configure(font='Impact 12')
    frame_label1.grid(row=2, column=1)

    frame_entry2 = Entry(frame, textvariable=m_pass, width=30, bd=4, bg='light grey')
    frame_entry2.grid(row=2, column=2)
    frame_entry2.configure(show = "*")

    def enter():
        bro = Toplevel()
        bro.geometry("450x575+325+40")

        label9 = Label(bro, text = "Do Your Formalities..",height = 2)
        label9.configure(font = "Mimmo 15")
        label9.pack(side = TOP)


        mail_icon = PhotoImage(file = "F:/Python_with_Atom/gui_mail_pplication/paper-plane.png")
        label8 = Label(bro, image = mail_icon)
        label8.pack(side = TOP)

        bro_frame = Frame(bro, width = 450, height = 300)
        bro_frame.pack(side = TOP)

        frame_label9 = Label(bro_frame, text = "TO :")
        frame_label9.configure(font = "Impact 12")
        frame_label9.grid(row = 1, column = 1)

        bro_text = Text(bro_frame, width = 30, height = 1, bd = 3, bg = "light grey")
        bro_text.grid(row = 1, column = 2)

        frame_label8 = Label(bro_frame, text = "Subject :")
        frame_label8.configure(font = "Impact 12")
        frame_label8.grid(row = 2, column =1)

        bro_text1 = Text(bro_frame, width = 30, height = 1, bd = 3, bg = "light grey")
        bro_text1.grid(row=2, column = 2)

        frame_label7 = Label(bro_frame, text = "\nEnter Your Message...\n",fg = "green")
        frame_label7.configure(font = "Mimmo 16")
        frame_label7.grid(row = 3, columnspan = 10)


        bro_text2 = Text(bro_frame, width = 50, height = 5, bd =3, bg ='light grey')
        bro_text2.grid(row =4 , columnspan = 10)

        frame_label6 = Label(bro_frame, text = "\n")
        frame_label6.grid(row = 5, columnspan = 10)


        def send():
            TO = bro_text.get(1.0, END)
            SUB = bro_text1.get(1.0, END)
            TEXT = bro_text2.get(1.0, END)
            email  = m_mail.get()
            password = m_pass.get()
            message = "Subject :{}\n\n{}".format(SUB,TEXT)
            #print(email)
            #print(password)
            #print(TO)
            #print(SUB)
            #print(TEXT)
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(email,password)
                server.sendmail(email,TO,message)
                statement1 = "MAIL HAS BEEN SENT"
                messagebox.showinfo("SUCCESS!", statement1)
                print(statement1)
            except:
                statement2 = "SOMETHING WINT WRONG"
                messagebox.showerror("ERROR!", statement2)
                print(statement2)



        bro_button = Button(bro_frame, text = "Send", bd =3, bg ="grey", command = send)
        bro_button.grid(row = 5, columnspan=10)

        bro_button1 = Button(bro_frame, text = "Back", bd =3, bg ="grey", command = bro.destroy)
        bro_button1.grid(row = 6, columnspan=10)



        bro.mainloop()

    frame_label0 = Label(frame , text= "\n")
    frame_label0.grid(row = 3 ,columnspan = 10)

    frame_button = Button(frame,text = "LOGIN", bd = 3, bg = "grey", command = enter)
    frame_button.grid(row = 4 , columnspan = 10)

    frame_button1 = Button(frame, text = "Quit", bd =3 , bg = "grey", command = pro.destroy)
    frame_button1.grid(row = 5, columnspan = 10)

    pro.mainloop()
