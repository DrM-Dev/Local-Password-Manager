#===================Imports
from tkinter import *

#===================Global Constants
FONT_tuple = ("Courier", 11, "bold")

#===================SETUP
window = Tk()
window_dim_x = 500
window_dim_y = 500
window.minsize(window_dim_x,window_dim_y)
window.title("Local Pass Manager 0.1")
window.config(padx=20,pady=20)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #




# ---------------------------- SAVE PASSWORD ------------------------------- #




# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas(width=200, height=210)
#
logo_img = PhotoImage(file="logo.png")
logo_widget = canvas.create_image(200/2, 200/2, image = logo_img)
#
canvas.place(x=window_dim_x/4,y=window_dim_y/4) #<-------to center it :)
#to center anything using PLACE! just dived screen size on quarters "4"s


#======================Input UIs
entry_box_width = 50
label_displacement = -90
entry_y_displacement = 160
label_spacer_value = 184
spacer_value = 25

website_label = Label(text="Website:", font=FONT_tuple)
website_label.place(x=window_dim_x/4 +label_displacement,
                    y=window_dim_y/4 +entry_y_displacement +spacer_value*1)
#----
website_name = Entry(width=entry_box_width)
website_name.insert(END, "Ex: Blender.com")
website_name.place(x=window_dim_x/4,
                   y=window_dim_y/4 +entry_y_displacement +spacer_value*1)

#______________________________
email_label = Label(text="Email:", font=FONT_tuple)
email_label.place(x=window_dim_x/4 +label_displacement,
                  y=window_dim_y/4 +entry_y_displacement +spacer_value*2)
#----
email_entry = Entry(width=entry_box_width)
email_entry.insert(END, "Ex: Name@gmail.com")
email_entry.place(x=window_dim_x/4,
                  y=window_dim_y/4 +entry_y_displacement +spacer_value*2)

#______________________________
password_label = Label(text="Password:", font=FONT_tuple)
password_label.place(x=window_dim_x/4 +label_displacement,
                     y=window_dim_y/4 +entry_y_displacement +spacer_value*3)
#----
pass_entry = Entry(width=entry_box_width-20)
pass_entry.insert(END, "Ex: Password")
pass_entry.place(x=window_dim_x/4,
                 y=window_dim_y/4 +entry_y_displacement +spacer_value*3)
####
def pass_generator():
    pass
    #generate a password :)

pg_button = Button(text="Generate Password",width=20,height=20,command=pass_generator)
pg_button.place(x=window_dim_x/4 + 20,
                 y=window_dim_y/4 +entry_y_displacement +spacer_value*3)

#===================END:
window.mainloop()
