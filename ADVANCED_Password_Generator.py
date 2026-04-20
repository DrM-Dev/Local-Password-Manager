#ADVANCED_Password Generator Project  -  By:  Dr.M-Dev
import random

print('''                                                                                                                                                  
                                                              ...::::.      ...::::::::    :.      .:.   
  5@@@@@@@@B!    &@@@@@@@&G:        ^G&@@@&P#@@@@B~          J@@@@@@@@@G.   #@@@@@@@@@@   .@@B    7@@?   
  G@@~::::J@@!   @@#     B@@.      :@@G::~&@@!::Y@@~         J@@~    ^@@B   #@@.           !@@J  .@@B    
  G@@     .@@Y   @@@    5&@#       ~@@!   B@&   :@@?         J@@:     &@#   #@@BBBBBBB      P@@: #@@.    
  7BP     .@@J   PBGGGGGB@@B       :BB^   B@&   :@@?         ~GP.     &@#   JGPYYYYYYY       &@# @@!     
  Y&&^....?@@7   #&P     J@@:  ##  ^&&~   B@&   ^@@?         ?@@7:  :7@@P   Y@& ......       ^@@@@P      
  P@@@@@@@@&?    &@B     ?@@:  ##  ~@@!   B@&   :@@?         ?@@@@@@@@#J    J&@@@@@@@@?       ?@@B  


                                                             !J!:                                                                
                                                              ^G@@&P7:                                                           
                                         .~7YGB#&&&&&&&#BG5?~:  .Y@@@@&G^                                                        
                                    :?P&@@@@@@@@@@@@@@@@@@@@@@@&G?J@@@@@&                                                        
                                .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P   ...                                                 
                              ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG&&@@@@                                              
                            ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                                             
                          7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GYP#&J                                            
                        .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!                                                
                       :&@@@@@@@@@@@@@@@@J7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P                                               
                      .@@@@@@@@@@@@@@@@#:  ^&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G                                              
                      #@@@@@@@@@@@@@@&7      P@@@@@@@@@@@@@B&@@@@@@@&@@#&@@@@@@@@@@J                                             
                     !@@@@@@@@@@@@@&?         ^#@@@@&&@@@@@@#PPGB##? B@5#@#@@@@@@@@@:                                            
                     B@@@@@@@@@@@G~             ^B@@@&GG#@@@@@@@#~   .&#J@Y&@@@@@@@@G                                            
                     @@@@@@@@@@~                  .?#@@@&BGPGBBJ      .#5G&J@@@@@@@@@.                                           
                   .@@@@@@@@@7      !PB##B4^        .^JG#&&P:  ^4B###P4?!~!?@@@@@@@@^                                           
                   .@@@@@@@@#      !4~.. .~4^                 ~4~....~4^    #@@@@@@@^   .~                                      
               ~BJ :@@@@@@@@BJYYYYYYJJJJYJJJJJJJ?!.     .!?JYYYJJYYYJJJYYYYY&@@@@@@@P7: .G#?.                                   
            .?BG^  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?...5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?  .Y#5:                                 
          :5BJ.    @@@@@@@@@&PJJJJJJ????JJJJ5&@@@@@@@@@@@@@@@GYJJ??????JJJJJYB@@@@@@@@@Y     7BB~                               
        !GG~       .YGG@@@@B        ...       G@@@@@@@@@@@@@:     .::.        !@@@@&GP7        ^G#?                             
     .JB5:             &@@@Y      4P..P@G.    7@@@@@@@@@@@@&    ^:^B@@@P.      @@@@~             .J#5.                          
     J@J               &@@@5     G@@4Y&@@&    ?@@@@?::^#@@@&   ~@4^B@@@@#     .@@@@~              ^#&:                          
      .5#J.            &@@@5     ?@@@@@@@P    7@@@@.   ?@@@&   .@@@@@@@@Y     .@@@@~           .J#P:                            
        .?#P:          #@@@G      .JGBBY:     5@@@&    ^@@@@.    ?B&&#P^      :@@@@~         ^PBJ.                              
           ~BB!        7@@@@5.              :P@@@@J     #@@@&!.             .!&@@@&        7BG~                                 
             :5#J.      ?@@@@@@@@@@@@@@@@@@@@@@@@J      .#@@@@@@&&&&&&&@&&@@@@@@@B.     :5BY.                                   
               .J#!      .7G&&@@@@@@@@@@@@@@&&G7.         ^5#&@@@@@@@@@@@@@@@&BJ:       7!                                      


 ''')


print("******** WELCOME TO SIMPLE-Password Generator - By: Dr.m DEV *********")
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

print("NOTE: pick the amount of characters between 1 and 10 for each type of characters [so the password won't be impossibly long] haha")
print("\n") #spacer
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))



#__________________________________________Letters
#For letters I used print(len(letters)) to find how many so I can set a RANDOMATION-RANGE!

password_generated_letters = ""
generated_letters_container = []

for Generated_Letter in range(0,nr_letters +1):  #remember..ther range count until the end but lacks 1 on the far end
    letters_randomizer = random.randint(0, 52)           #generates random value
    password_generated_letters = letters[letters_randomizer]      #to pick a random item & store it in a variable
    generated_letters_container.append(password_generated_letters) #THEN store it into a list to use it later!!!

#the generated list from that is [[[ generated_letters_container ]]]


#__________________________________________Numbers
password_generated_number = 0
generated_number_container = []

for Generated_Number in range(0,nr_numbers +1):#remember..ther range count until the end but lacks 1 on the far end
    numbers_randomizer = random.randint(0, 10)           #generates random value
    password_generated_number = numbers[numbers_randomizer]      #to pick a random item & store it in a variable
    generated_number_container.append(password_generated_number) #THEN store it into a list to use it later!!!

#the generated list from that is [[[ generated_number_container ]]]


# __________________________________________Symbols
password_generated_symbol = 0
generated_symbol_container = []

for Generated_Symbol in range(0,nr_symbols +1 ):#remember..ther range count until the end but lacks 1 on the far end
    symbols_randomizer = random.randint(0, 10)           #generates random value
    password_generated_symbol = symbols[symbols_randomizer]      #to pick a random item & store it in a variable
    generated_symbol_container.append(password_generated_symbol) #THEN store it into a list to use it later!!!

#the generated list from that is [[[ generated_symbol_container ]]]




#__________________________________________________________ASSEMBLEEEEEEEEEE!!!! Ahem...assemble


password_assembling_list = []
password_assembling_list.extend(generated_letters_container)
password_assembling_list.extend(generated_number_container)
password_assembling_list.extend(generated_symbol_container)


assembling_list_amount = len(password_assembling_list)
#|
items_picked_from_assembly = ""


for assembling_cycle_turns in range(0,assembling_list_amount):
    RANDOM_items_picker_num = random.randint(1, assembling_list_amount)
    items_picked_from_assembly += password_assembling_list[RANDOM_items_picker_num]
    #|
    #we didn't use [assembling_cycle_turns] to add items we used [ RANDOM_items_picker_num ]
    #NOTE:
    #always keep the RANDOMIZER inside the for-loop..so it can RANDOMIZE and change value after each cycle!!


print(f"Your generated password is:\n {items_picked_from_assembly}")
#note: no need to add + between these variables... because the F-string will combine them anyway!

