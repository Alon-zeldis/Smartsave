from tkinter import *
import shutil

# The function creates the button and input field to get the path the user want to move the file to, and creates the
# recommendation to where the file should go according to file type and the button to accept the move to that location


def file_move(source, log_info):
    move_message = Label(source, text="Enter the new path of the file ")
    user_path = Entry(source)
    move_butt = Button(source, text="Move", command=lambda: shutil.move(log_info[2], user_path.get()))

    move_message.grid(row=3, column=0)
    user_path.grid(row=3, column=1)
    move_butt.grid(row=3, column=2)

    new_location = log_info[-1]
    recommendation_msg = Label(source, text=f"We recommend moving the file to this location: {new_location}")
    recommended_move_btn = Button(source, text="Accept", command=lambda: shutil.move(log_info[2], new_location))

    recommendation_msg.grid(row=4, column=0)
    recommended_move_btn.grid(row=4, column=1)

    if new_location == ".\\Suspicious":
        warning_msg = Label(source, text="This file might contain malware, be careful!!")
        warning_msg.grid(row=5, column=0)

# Creates the UI for when a new file is added to the Downloads folder of the user and asks if the user want to change
# the location


def new_file_alert(log_info):
    root = Tk()
    root.geometry("500x500")
    root.eval('tk::PlaceWindow . center')

    welcome_message = Label(root,
                            text="You have created the file {fname}\n".format(fname=log_info[0]))
    welcome_message.grid(row=0, column=0, columnspan=3)

    file_shift_message = Label(root, text="Would you like to change the location of this file?\n")
    file_shift_message.grid(row=1, column=0, columnspan=3)

    yes_butt = Button(root, text="Yes", command=lambda: file_move(root, log_info))
    no_butt = Button(root, text="No", command=lambda: exit())

    yes_butt.grid(row=2, column=0)
    no_butt.grid(row=2, column=1)

    root.mainloop()
