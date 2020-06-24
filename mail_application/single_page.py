from tkinter import *
from tkinter import messagebox
import  smtplib

def sendMail():
    email = m_mail.get()
    password = m_pass.get()
    to = frame_box.get(1.0, END)
    sub = frame_box1.get(1.0, END)
    text = frame_box2.get(1.0, END)
    message = "Subject : {}\n\n{} ".format(sub,text)
    #print(message)
    #print(text)
    #print(sub)
    #print(to)
    #print(password)
    #print(email)
    try:

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,to,message)
        statement1 = "Mail Has Been Sent"
        print(statement1)
        messagebox.showinfo("SUCCESS!", "YOUR MAIL HAS BEEN SENT")
        server.quit()
    except:
        statement2 = "Something Went Wrong"
        messagebox.showerror("ERROR!", "SOMETHING WENT WRONG")
        print(statement2)

if __name__ == "__main__" :
    pro = Tk()
    pro.geometry("600x600+325+40")
    pro.resizable(0, 0)
    pro.title("MAIL APPLICATION")
    # pro.configure(background = "light green")
    label = Label(pro, text="please Log In First", height=2)
    label.configure(font="Mimmo 18")
    label.pack(side=TOP)

    user_icon = PhotoImage(file="F:/Python_with_Atom/gui_mail_pplication/login.png")
    label0 = Label(pro, image=user_icon)
    label0.pack(side=TOP)

    label0 = Label(pro, fg='red', text="Before log in, please\n"
                                       "Allow less secure apps: ON\n")
    label0.configure(font="Mimmo 12")
    label0.pack(side=TOP)

    frame = Frame(pro, width=550, height=300)
    # frame.configure(background = 'Light Green')
    frame.pack(side=TOP)

    m_mail = StringVar(frame)
    m_pass = StringVar(frame)

    frame_label = Label(frame, text="Email ID :")
    frame_label.configure(font='Impact 10')
    frame_label.grid(row=1, column=1)

    frame_entry1 = Entry(frame, textvariable=m_mail, width=25, bd=4, bg='light grey')
    frame_entry1.grid(row=1, column=2)
    # m_mail.set("Enter Your Mail Address")

    frame_label1 = Label(frame, text="Password :")
    frame_label1.configure(font='Impact 10')
    frame_label1.grid(row=2, column=1)

    frame_entry2 = Entry(frame, textvariable=m_pass, width=25, bd=4, bg='light grey')
    frame_entry2.grid(row=2, column=2)
    frame_entry2.configure(show = "*")
    # m_pass.set("Enter Your Password")

    frame_label2 = Label(frame, text='\nNow Do Your Formalities...\n')
    frame_label2.configure(font="Mimmo 12")
    frame_label2.grid(row=3, columnspan=10)

    frame_label3 = Label(frame, text="TO :")
    frame_label3.configure(font="Impact 12")
    frame_label3.grid(row=4, column=1)

    frame_box = Text(frame, width=40, bd=3, height=1, bg="light grey")
    frame_box.grid(row=4, column=2)

    frame_label4 = Label(frame, text="Subject :")
    frame_label4.configure(font="Impact 12")
    frame_label4.grid(row=5, column=1)

    frame_box1 = Text(frame, width=40, bd=3, height=1, bg="light grey")
    frame_box1.grid(row=5, column=2)

    frame_label5 = Label(frame, text="\n Enter Your Message...")
    frame_label5.configure(font="Mimmo 12")
    frame_label5.grid(row=6, columnspan=10)

    frame_box2 = Text(frame, width=50, height=4, bd=3, bg="light grey")
    frame_box2.grid(row=7, columnspan=10)

    frame_button = Button(frame, text="Send", bd=3, bg="grey", command = sendMail )
    frame_button.grid(row=8, columnspan=10)

    frame_button1 = Button(frame, text="Quit", bd=3, bg="grey", command = pro.destroy )
    frame_button1.grid(row=9, columnspan=10)
    pro.mainloop()
