from colorama import Back, Fore, Style 

def decryption_header():
    print(Fore.CYAN, """
                                ──────▄▀▄─────▄▀▄
                                ─────▄█░░▀▀▀▀▀░░█▄ 
                                ─▄▄──█░░░░░░░░░░░█──▄▄
                                █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█ """ + Fore.YELLOW,"""
                    ░▒█▀▀▄░█▀▀░█▀▄░█▀▀▄░█░░█░▄▀▀▄░▀█▀░░▀░░▄▀▀▄░█▀▀▄
                    ░▒█░▒█░█▀▀░█░░░█▄▄▀░█▄▄█░█▄▄█░░█░░░█▀░█░░█░█░▒█
                    ░▒█▄▄█░▀▀▀░▀▀▀░▀░▀▀░▄▄▄▀░█░░░░░▀░░▀▀▀░░▀▀░░▀░░▀ """)
    print(Fore.WHITE, " "*17 , "="* 20 + "PROBLEM 2" + "="* 20 ,"\n")

def decryption_footer():
    print(Fore.RED, """

                        ▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█ █
                        ░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█ ▄""" + Fore.WHITE, """
                                -🅗🅐🅥🅔 🅐 🅖🅡🅔🅐🅣 🅓🅐🅨-""")
    
def cipher_header():
    print(Fore.LIGHTYELLOW_EX, """ 
                                    ──▄▀▀▀▄───────────────
                                    ──█───█───────────────
                                    ─███████─────────▄▀▀▄─
                                    ░██─▀─██░░█▀█▀▀▀▀█░░█░
                                    ░███▄███░░▀░▀░░░░░▀▀░░"""+ Fore.RED,"""
              ▒█░░▒█ ░▀░ █▀▀▀ █▀▀ █▀▀▄ █▀▀ █▀▀█ █▀▀ ▒█▀▀█ ░▀░ █▀▀█ █░░█ █▀▀ █▀▀█ 
              ░▒█▒█░ ▀█▀ █░▀█ █▀▀ █░░█ █▀▀ █▄▄▀ █▀▀ ▒█░░░ ▀█▀ █░░█ █▀▀█ █▀▀ █▄▄▀░ 
              ░░▀▄▀░ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀ ▀░▀▀ ▀▀▀ ▒█▄▄█ ▀▀▀ █▀▀▀ ▀░░▀ ▀▀▀ ▀░▀▀ """)                                
    print(Fore.WHITE, " "*12 , "="* 29 + "PROBLEM 3" + "="* 29 ,"\n")
