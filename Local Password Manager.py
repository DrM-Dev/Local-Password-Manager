#===================Imports
from tkinter import *
from tkinter import filedialog
import ADVANCED_Password_Generator

#===================Global Constants
PASS_GEN_WINDOW_Activation = False #False = 0 = OFF     True = 1 = ON
generated_pass = 0
#----
FONT_tuple = ("Courier", 11, "bold")
BUTTONS_FONT = ("Times New Roma", 8, "bold")

#===================Global Final Outputs
website_OUTPUT = ""
email_OUTPUT = ""
pass_OUTPUT = ""
#+#
path_OUTPUT = ""

#===================SETUP
window = Tk()
window_dim_x = 500
window_dim_y = 600
window.minsize(window_dim_x,window_dim_y)
window.minsize(window_dim_x+10,window_dim_y+10)
window.title("Local Pass Manager 0.1")
window.config(padx=20,pady=30)



#### - ######## - ######## - ######## - ######## - ######## - ####
#### - ######## - ######## - ######## - ######## - ######## - #### UI SETUP
entry_box_width = 50
label_displacement = -90
entry_y_displacement = 90
label_spacer_value = 184
spacer_value = 25

#======================Padding:
for child in window.winfo_children():
    child.grid_configure(padx=10, pady=15)


#======================Input UIs
canvas = Canvas(width=200, height=210)
#
logo_img = PhotoImage(file="logo.png")
logo_widget = canvas.create_image(200/2, 200/2, image = logo_img)
#
canvas.place(x=window_dim_x/4,y=window_dim_y/4-150) #<-------to center it :)
#to center anything using PLACE! just dived screen size on quarters "4"s

#______________________________
website_label = Label(text="Website:", font=FONT_tuple)
website_label.place(x=window_dim_x/4 +label_displacement,
                    y=window_dim_y/4 +entry_y_displacement +spacer_value*1)
#----
website_name = Entry(width=entry_box_width)
website_name.insert(END, "Ex: Blender.com")
website_name.place(x=window_dim_x/4,
                   y=window_dim_y/4 +entry_y_displacement +spacer_value*1)
website_name.focus() #nice

#______________________________
email_label = Label(text="Email:", font=FONT_tuple)
email_label.place(x=window_dim_x/4 +label_displacement,
                  y=window_dim_y/4 +entry_y_displacement +spacer_value*2)
#----
email_entry = Entry(width=entry_box_width)
email_entry.insert(END, "Ex: Name@gmail.com")
email_entry.place(x=window_dim_x/4,
                  y=window_dim_y/4 +entry_y_displacement +spacer_value*2)

#______________________________ SAVE PASS File-browser
#entry must be pre-made before function:
browse_save_box = Entry(width=50)
##############
file_path = ""

def browse_to_save():
    global file_path
    ####
    file_path = filedialog.askdirectory(
        title="Select A Folder To Save Your Documents"
    )
    ####
    browse_save_box.delete(0, END)
    browse_save_box.insert(END, f"{file_path}")

#-------
browse_save_l = Label(text="Save Location:", font=FONT_tuple)
browse_save_l.place(x=window_dim_x/4-90,y=window_dim_y/4+210)

#-------
browse_save_box.insert(END, "Press BROWSE to select a saving folder")
browse_save_box.place(x=window_dim_x/4-90,y=window_dim_y/4+235)

#-------
browse_save_button = Button(text="🔍Browse", font=BUTTONS_FONT,width=12,height=1,command=browse_to_save)
browse_save_button.place(x=window_dim_x/4+220,y=window_dim_y/4+231)




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
    global PASS_GEN_WINDOW_Activation
    global generated_pass
    #-------------#
    pass_gen_window = Tk()
    pass_gen_window.config(padx=30, pady=20)
    pass_gen_window.title("Generate Your Password")
    pass_gen_window.minsize(390,300)
    pass_gen_window.maxsize(390,320)
    ####
    for children in pass_gen_window.winfo_children():
        children.grid_configure(padx=10, pady=10)
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
    letters_count_sbox = Spinbox(pass_gen_window, width=3, from_=0, to=20)
    letters_count_sbox.grid(column=1,row=3)
    # -------------
    numbers_count_l = Label(pass_gen_window, text="How Many Numbers?", font=FONT_tuple)
    numbers_count_l.grid(column=0, row=4)
    ####
    numbers_count_sbox = Spinbox(pass_gen_window, width=3, from_=0, to=20)
    numbers_count_sbox.grid(column=1, row=4)
    # -------------
    symbols_count_l = Label(pass_gen_window, text="How Many Symbols?", font=FONT_tuple)
    symbols_count_l.grid(column=0, row=5)
    ####
    symbols_count_sbox = Spinbox(pass_gen_window, width=3, from_=0, to=20)
    symbols_count_sbox.grid(column=1, row=5)

    # _____________<Pass Entry>
    resalt_l = Label(pass_gen_window, text="Password:", font=FONT_tuple)
    resalt_l.place(x=-2,y=136)
    ####
    resalt_box = Entry(pass_gen_window, width=30)
    resalt_box.place(x=110,y=135)

    #######################################  PASS-SET BUTTON
    center_pg_buttons = 120
    # __________________________SET-PASS:
    def set_pass():
        global generated_pass
        # -------------#
        pass_entry.delete(0,END)
        pass_entry.insert(END, f"{generated_pass}")
    ##############
    set_pass_b = Button(pass_gen_window, text="SET", width=8, height=1, command=set_pass)
    set_pass_b.config(state="disabled")
    set_pass_b.place(x=25 + center_pg_buttons, y=230)
    #######################################
    #######################################  PASS-GEN MAIN-BUTTON
    def generate():
        global PASS_GEN_WINDOW_Activation
        global generated_pass
        # -------------#
        resalt_box.delete(0, END)
        ####
        nr_letters = int(letters_count_sbox.get())
        nr_numbers = int(numbers_count_sbox.get())
        nr_symbols = int(symbols_count_sbox.get())
        #  |  #
        #  v  #
        generated_pass = ADVANCED_Password_Generator.advanced_pass_generator(nr_letters,nr_numbers,nr_symbols)
        #  |  #
        #  v  #
        ####
        resalt_box.insert(END, f"{generated_pass}")
        resalt_box.place(x=110,y=135)
        #### <!> #### -Activate / Deactivate - PASS-SET BUTTON
        if len(generated_pass) > 4:
            ##############
            set_pass_b.config(state="normal")
        else:
            set_pass_b.config(state="disabled")
    #######################################
    # __________________________GENERATE:
    generate_pass_b = Button(pass_gen_window ,text="GENERATE!", width=10,height=1, command=generate)
    generate_pass_b.place(x=20+center_pg_buttons,y=200)
    #######################################
    # ##############################################################################-CHECKING IF Pass-Generate-Is ACTIVE using [ON-CLOSE]
    # CHECK Pass-Gen-WINDOW state:
    if pass_gen_window.state() == 'normal':
        PASS_GEN_WINDOW_Activation = True
        print("\nPASS-GEN-WINDOW ACTIVATED + ")
        pg_button.config(state="disabled")
    # if pass_gen_window.state() == 'disabled':  <---------------------NO NEED FOR THIS, it's better to DISABLE the Pass-Gen-Button from the "[ON-CLOSE] CHECK"
    #     PASS_GEN_WINDOW_Activation = False
    #     print("\nPASS-GEN-WINDOW NOTTTTT activated - ")
    #     print(f"confirm -> {PASS_GEN_WINDOW_Activation}")

    #-----------------------------------------------ON-CLOSING FUN
    def on_closing():
        global PASS_GEN_WINDOW_Activation
        PASS_GEN_WINDOW_Activation = False
        print("PASS-GEN-Window is closing")
        pg_button.config(state="normal")
        #----#
        pass_gen_window.destroy()
    #------------------------------------------------ON-CLOSING CHECK
    pass_gen_window.protocol("WM_DELETE_WINDOW", on_closing)


#______________________________________________________________________________________________________________________|
#Advanced_Pasword_Generator Button:
pg_button = Button(text="⚙️Generate Password", font=BUTTONS_FONT,width=18,height=1,command=pass_generator)
pg_button.place(x=window_dim_x/4 + 183,
                 y=window_dim_y/4 +entry_y_displacement +spacer_value*3-3)
#-----------------
# pass_generator()
if PASS_GEN_WINDOW_Activation:
    pg_button.config(state="disabled")
else:
    pg_button.config(state="normal")

#______________________________________________________________________________________________________________________|
#SAVING DATA:

def final_document_save():
    # got_website = False #"Ex: Blender.com"
    # got_email = False #"Ex: Name@gmail.com"
    # got_pass = False #"Ex: Password"
    # is_path_ready = False
    #--------
    global website_OUTPUT
    website_OUTPUT = website_name.get()
    ########
    global email_OUTPUT
    email_OUTPUT = email_entry.get()
    ########
    global generated_pass
    global pass_OUTPUT
    pass_OUTPUT = generated_pass
    ########
    global file_path
    global path_OUTPUT
    path_OUTPUT = file_path

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~inputs check:
    if website_OUTPUT != "Ex: Blender.com" and website_OUTPUT != 0 and website_OUTPUT != "":
        got_website = True
    else:
        got_website = False

    # ~~~~~~~~~~~~~
    if email_OUTPUT != "Ex: Name@gmail.com" and website_OUTPUT != 0 and website_OUTPUT != "":
        got_email = True
    else:
        got_email = False

    # ~~~~~~~~~~~~~
    if pass_OUTPUT != "Ex: Password" and website_OUTPUT != 0 and website_OUTPUT != "":
        got_pass = True
    else:
        got_pass = False

    # ~~~~~~~~~~~~~
    if path_OUTPUT != "":
        is_path_ready = True
    else:
        is_path_ready = False

    ## -- ----------------------------- -- ##
    if got_website and got_email and got_pass and is_path_ready: #IF ALL IS TRUE
        website_raw_name = website_OUTPUT.replace("@","")
        file_name_refine_1 = website_raw_name.replace(".com", "")
        ####
        with open(fr"{path_OUTPUT}/{file_name_refine_1}.txt", mode="w" ) as file:
            file.write(f"================================\n"
                       f"{website_OUTPUT}-Account info save:\n\n"
                       f"Email:     | {email_OUTPUT}\n"
                       f"Password:  | {pass_OUTPUT}\n"
                       "=================================\n"
                       )
    #==========================================================================
    #======================================ERRORS:
    #Error windows dimensions:
    er_w_width = 300
    er_w_height = 100
    #----
    er_w_padx = 10
    er_w_pady = 10
    #----
    er_w_placex = er_w_width / 4 - 35
    er_w_placey = er_w_height / 4
    #----
    er_w_font = ("Courier", 8, "bold")

    #============================================
    if not got_website:  # WEBSITE-ERROR:
        warning_win_web = Tk()
        warning_win_web.maxsize(er_w_width, er_w_height)
        warning_win_web.minsize(er_w_width, er_w_height)
        warning_win_web.title("⚠️ERROR")
        warning_win_web.config(padx=er_w_padx, pady=er_w_pady)
        #
        website_warning_l = Label(warning_win_web, text="Please give a proper website name!", font=er_w_font)
        website_warning_l.place(x=er_w_placex, y=er_w_placey)
        # --X--X--X--#
        def closing_web_error():
            website_warning_l.destroy()
            warning_win_web.destroy()
        ####
        warning_win_web.protocol("WM_DELETE_WINDOW", closing_web_error)
    #==========================================
    if not got_email:  # EMAIL-ERROR:
        warning_win_email = Tk()
        warning_win_email.maxsize(er_w_width, er_w_height)
        warning_win_email.minsize(er_w_width, er_w_height)
        warning_win_email.title("⚠️ERROR")
        warning_win_email.config(padx=er_w_padx, pady=er_w_pady)
        #
        website_warning_l = Label(warning_win_email, text="Please give a proper Email !", font=er_w_font)
        website_warning_l.place(x=er_w_placex, y=er_w_placey)
        # --X--X--X--#
        def closing_email_error():
            website_warning_l.destroy()
            warning_win_email.destroy()
        ####
        warning_win_email.protocol("WM_DELETE_WINDOW", closing_email_error)
    #==========================================
    if not got_pass:
        warning_win_pass = Tk()
        warning_win_pass.maxsize(er_w_width, er_w_height)
        warning_win_pass.minsize(er_w_width, er_w_height)
        warning_win_pass.title("⚠️ERROR")
        warning_win_pass.config(padx=er_w_padx, pady=er_w_pady)
        #
        website_warning_l = Label(warning_win_pass, text="Please give a Password", font=er_w_font)
        website_warning_l.place(x=er_w_placex, y=er_w_placey)
        # --X--X--X--#
        def closing_pass_error():
            website_warning_l.destroy()
            warning_win_pass.destroy()
        ####
        warning_win_pass.protocol("WM_DELETE_WINDOW", closing_pass_error)
    # ==========================================
    if not is_path_ready:
        warning_win_path = Tk()
        warning_win_path.maxsize(er_w_width, er_w_height)
        warning_win_path.minsize(er_w_width, er_w_height)
        warning_win_path.title("⚠️ERROR")
        warning_win_path.config(padx=er_w_padx, pady=er_w_pady)
        #
        website_warning_l = Label(warning_win_path, text="Please select a saving folder", font=er_w_font)
        website_warning_l.place(x=er_w_placex, y=er_w_placey)
        # --X--X--X--#
        def closing_path_error():
            website_warning_l.destroy()
            warning_win_path.destroy()
        ####
        warning_win_path.protocol("WM_DELETE_WINDOW", closing_path_error)


#==========================SAVE-BUTTON:
save_data_b = Button(text="💾SAVE", font=("Times New Roma", 10, "bold"), bg="blue", fg="white",width=10,height=2,command=final_document_save)
save_data_b.place(x=window_dim_x/4 + 60,
                 y=window_dim_y/4 +entry_y_displacement +spacer_value*3+100)


#===================END:
window.mainloop()
