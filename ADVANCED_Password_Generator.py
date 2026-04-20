#ADVANCED_Password Generator Project  -  By:  Dr.M-Dev
import random

# print("******** WELCOME TO ADVANCED-Password Generator - By: Dr.m DEV *********")
# =================================================================
print("Password Generator ONLINE!")
# ===================================================================================================
# ADVANCED MODE:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+','!', '#', '$', '%', '&', '(', ')', '*', '+', '+', "-", "_", " "]

#NOTE:
# I have EXTENDDEDDD the smaller lists like the SYMBOLS ONE...from 6 to be more than 10...because what if the
# user asked for more than 10 symbols... I know...some people are silly SO! I increased it even beyond 10 :)
#all of it will be randomized anyway!

# print("NOTE: pick the amount of characters between 1 and 10 for each type of characters [so the password won't be impossibly long] haha")
# print("\n") #spacer
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))


def advanced_pass_generator(nr_letters, nr_numbers, nr_symbols):
    global letters
    global numbers
    global symbols
    #############
    #__________________________________________Letters
    #For letters I used print(len(letters)) to find how many so I can set a RANDOMATION-RANGE!

    # password_generated_letters = 0
    generated_letters_container = []

    for Generated_Letter in range(0,nr_letters):  #remember.ther range count until the end but lacks 1 on the far end
        letters_randomizer = random.randint(0, 52-1)           #generates random value
        password_generated_letters = letters[letters_randomizer]      #to pick a random item & store it in a variable
        generated_letters_container.append(password_generated_letters) #THEN store it into a list to use it later!!!

    #the generated list from that is [[[ generated_letters_container ]]]


    #__________________________________________Numbers
    # password_generated_number = 0
    generated_number_container = []

    for Generated_Number in range(0,nr_numbers):#remember.ther range count until the end but lacks 1 on the far end
        numbers_randomizer = random.randint(0, 10-1)           #generates random value
        password_generated_number = numbers[numbers_randomizer]      #to pick a random item & store it in a variable
        generated_number_container.append(password_generated_number) #THEN store it into a list to use it later!!!

    #the generated list from that is [[[ generated_number_container ]]]


    # __________________________________________Symbols
    # password_generated_symbol = 0
    generated_symbol_container = []

    for Generated_Symbol in range(0,nr_symbols):#remember, ther range count until the end but lacks 1 on the far end
        symbols_randomizer = random.randint(0, 10-1)           #generates random value
        password_generated_symbol = symbols[symbols_randomizer]      #to pick a random item & store it in a variable
        generated_symbol_container.append(password_generated_symbol) #THEN store it into a list to use it later!!!

    #the generated list from that is [[[ generated_symbol_container ]]]




    #__________________________________________________________assemble
    password_assembling_list = []
    password_assembling_list.extend(generated_letters_container)
    password_assembling_list.extend(generated_number_container)
    password_assembling_list.extend(generated_symbol_container)


    assembling_list_amount = len(password_assembling_list) #---->the reason why every len(list_name) needs "-1" because
    #|                                                          the length will calculate the last number of the list-size
    items_picked_from_assembly = ""                             #which is gonna be OUTSIDE THE INDEX AMOUNT OF THE LIST
                                                                #a list of 20letters has only 19 spaces (it starts from 0)
                                                                # <!><!><!><!><!><!><!><!><!><!><!><!><!><!><!><!><!><!>


    for assembling_cycle_turns in range(0,assembling_list_amount -1):
        random_items_picker_num = random.randint(0, assembling_list_amount-1)
        items_picked_from_assembly += password_assembling_list[random_items_picker_num]
        #|
        #we didn't use [assembling_cycle_turns] to add items we used [ random_items_picker_num ]
        #NOTE:
        #always keep the RANDOMIZER inside the for-loop.so it can RANDOMIZE and change value after each cycle!!


    # print(f"Your generated password is:\n {items_picked_from_assembly}")
    #note: no need to add + between these variables... because the F-string will combine them anyway!

