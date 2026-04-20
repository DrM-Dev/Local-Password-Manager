#===================Imports
from tkinter import *
import ADVANCED_Password_Generator

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
entry_y_displacement = 170
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
pass_entry = Entry(width=entry_box_width-21)
pass_entry.insert(END, "Ex: Password")
pass_entry.place(x=window_dim_x/4,
                 y=window_dim_y/4 +entry_y_displacement +spacer_value*3)
####
def pass_generator():
    pass_gen_window = Tk()
    pass_gen_window.config(padx=20, pady=20)
    pass_gen_window.title("Generate Your Password")
    pass_gen_window.minsize(300,200)
    # pass_gen_window.maxsize(310,210)
    ####
    #-------------
    pass_gen_label = Label(pass_gen_window, text="Make your own password with:", font=FONT_tuple)
    pass_gen_label.config(padx=20, pady=10)
    pass_gen_label.grid(column=0,row=1)
    #-------------
    grid_spacer_1 = Label(pass_gen_window, text="༻━━━━━━━🔓━━━━━━━༺ ", font=FONT_tuple)
    grid_spacer_1.grid(column=0,row=2)

    # _____________
    letters_count_l = Label(pass_gen_window, text="How Many Letters?", font=FONT_tuple)
    letters_count_l.grid(column=0,row=3)
    ####
    letters_count_sbox = Spinbox(pass_gen_window, width=3, from_=1, to=10)
    letters_count_sbox.grid(column=1,row=3)
    # -------------
    numbers_count_l = Label(pass_gen_window, text="How Many Numbers?", font=FONT_tuple)
    numbers_count_l.grid(column=0, row=4)
    ####
    numbers_count_sbox = Spinbox(pass_gen_window, width=3, from_=1, to=10)
    numbers_count_sbox.grid(column=1, row=4)
    # -------------
    symbols_count_l = Label(pass_gen_window, text="How Many Symbols?", font=FONT_tuple)
    symbols_count_l.grid(column=0, row=5)
    ####
    symbols_count_sbox = Spinbox(pass_gen_window, width=3, from_=1, to=10)
    symbols_count_sbox.grid(column=1, row=5)

    # _____________
    def generate():
        nr_letters = letters_count_sbox.get()
        nr_numbers = numbers_count_sbox.get()
        nr_symbols = symbols_count_sbox.get()
        #  v  #
        ADVANCED_Password_Generator.advanced_pass_generator(nr_letters,nr_numbers,nr_symbols)
    ##############
    generate_pass_b = Button(pass_gen_window ,text="GENERATE!", width=10,height=2, command=generate)
    generate_pass_b.grid(column=1,row=6)

    #Advanced_Pasword_Generator
    #


pg_button = Button(text="Generate Password", font=("Times New Roma", 8, "bold"),width=16,height=1,command=pass_generator)
pg_button.place(x=window_dim_x/4 + 183,
                 y=window_dim_y/4 +entry_y_displacement +spacer_value*3-3)

#===================END:
window.mainloop()
