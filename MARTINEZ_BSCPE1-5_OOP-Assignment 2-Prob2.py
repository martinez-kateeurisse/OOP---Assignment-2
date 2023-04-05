#Kate Eurisse L. Martinez_BSCPE 1-5_OOP Assignment 2-Problem 2

#PROBLEM 2 – DECRYPTION 
#A Python Script that accepts a string as encrypted text and then the program will decrypt it using the following character substitute:
#'a' = *, 'e' = & , 'i' = # , 'o' = + 'u' = !

#Importing certain modules for the program's design and text formatting
import pyfiglet 
from colorama import Back, Fore, Style 
import prog_design #own python file

#Printing a header art for the program
prog_design.decryption_header()

#Asking the user's name and printing a greeting
print("//" * 20)
name = input(f"{Fore.RED} Enter your name: "+ Fore.RESET)
print("//"*20, "\n\n") 
print(Back.LIGHTBLACK_EX, Fore.LIGHTCYAN_EX, ("Hello " + name).center(84, "*") + Back.RESET, "\n")

#Displaying the program's instructions
print(f"{Fore.GREEN}This program will decrypt your encrypted text using the following character substitute:")
char_eq = "'a' = *,  'e' = & , 'i' = #, 'o' = + ,'u' = !"
print(char_eq.center(85, " "), "\n")

#Using a while loop in case that the user wanted to decrypt another message
Retry = 'y'
while Retry == 'y':
    #Ask the user to input an encrypted text
    user_input = input(f"{Fore.RED}Please enter a string to decrypt: " + Fore.RESET)
    print("\n")
    decrypted_output = ""
    #Checking each character of the user's input
    for i in range(len(user_input)):
    #If *, change to a
        if user_input[i] == "*":
            decrypted_output += "a"       
    #If &, change to e
        elif user_input[i] == "&":
            decrypted_output += "e"       
    #If #, change to i
        elif user_input[i] == "#":
            decrypted_output += "i"        
    #If +, change to o
        elif user_input[i] == "+":
            decrypted_output += "o"        
    #If !, change to u
        elif user_input[i] == "!":
            decrypted_output += "u"        
        else:
            decrypted_output += user_input[i]

    print(Fore.LIGHTYELLOW_EX, "⋆⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⊱∘────────────────────────────────────────────∘⊰⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋆\n")
    #Displaying the output with a design through the imported modules
    print(f"{Fore.BLUE}The plain text of ", ('\033[91m' + user_input), '\033[94m' + "is:" + "\n")

    #Output's upper border design
    def output_border():
        for i in range(len(decrypted_output)):
            if i <= 5:
                print(Fore.LIGHTCYAN_EX,"""██████████""", end ="""░░""")
            else:
                pass
        print("\n")
    output_border()
    
    #Output design executed using a pyfiglet font and colorama color
    print(Fore.MAGENTA,Style.BRIGHT,pyfiglet.figlet_format(decrypted_output, font = "block"))
    
    #Output's lower border design
    output_border()
    
    #Asking the user whether to decrypt another message or not
    Retry = input(f"{Fore.GREEN}\n\n\nDo you want to decrypt another message? (Please type 'y' if yes and any key if no): ")
    Retry = Retry.lower()    
    #The program will decide depending on the user's input
    if Retry == 'y':
        print("\n\n",("="*85),"\n\n")
    else:
        print("\n\n")
        break

#Displaying thank you message
prog_design.decryption_footer()

