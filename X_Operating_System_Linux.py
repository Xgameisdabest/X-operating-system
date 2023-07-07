#import things here
from time import *
from random import *
import os
from platform import *
import subprocess
import webbrowser
from tqdm import tqdm
#----------------------------------------------------------------

#variables
update_ver = "1.2.1 BETA"

# opening stuff
def loadingscreen():
    for i in tqdm(range(100),desc="READING_MACHINE_ARCHITECTURE",ascii=False,dynamic_ncols=True):
        sleep(0.1)
    for i in tqdm(range(100),desc="LOADING_OPERATING_SYSTEM",ascii=False,dynamic_ncols=True):
        sleep(0.01)
    for i in tqdm(range(100),desc="LOADING_DATA",ascii=False,dynamic_ncols=True):
        sleep(0.1)
    for i in tqdm(range(100),desc="CHECKING_OS_FILE_DATA",ascii=False,dynamic_ncols=True):
        sleep(0.1)
    os.system('clear')
    for i in tqdm(range(100),desc="Xos-boot.service",ascii=False,dynamic_ncols=True):
        sleep(0.2)
    for i in tqdm(range(100),desc="Final_Check",ascii=False,dynamic_ncols=True):
        sleep(0.15)
def opening():
    os.system('clear')
    loadingscreen()
    print("Complete!")
    sleep(2)
    os.system('clear')
    print('Welcome to X Operating System!')
    sleep(2)
    print('Type /help to show how to use the operating system!')
    print('Type /info to show more info about the operating system itself!')
    os.system('pause')
    os.system('clear')
# helping commands
def helpfunc():
    if inp == '/help'.lower():
     print('-----------------------------------------------------------')
     print('Type /exit to shutdown the operating system!')
     print('Type /clear to clear the mess you have just made!')
     print('Type /cmds to show all support commands that are all available!')
     print('-----------------------------------------------------------')
    
    if inp == '/info'.lower():
     print('-----------------------------------------------------------')
     print(f'X Operating System {update_ver}')
     print('A fully coded in python project made by Xytozine/Xgameisdabest')
     print('-----------------------------------------------------------')
# commands showcase
def funccmds():
    if inp == '/cmds'.lower():
     print('-----------------------------------------------------------')
     print('IN APP COMMANDS:')
     print('/exit to shutdown the operating system')
     print('/clear to clear the mess')
     print('/getgame to play game')
     print('/updatelog to view updates')
     print('/time to see what time is it')
     print('/saver to activate screen saver')
     print('/devinfo to view your current device information')
     print('')
     print('OPENING WINDOW APPS COMMANDS:')
     print('/chrome to open Google Chrome')
     print('/youtube to open Youtube')
     print('/gglphotos to open Google Photos')
     print('/explorer to open file manager')
     print('/sysmonitor to open system monitor')
     print('')
     print('HOST OPERATING SYSTEM COMMAND:')
     print('/readfile to open (VIEW ONLY) a directory in the X Operating System\'s folder/directory')
     print('-----------------------------------------------------------')
# game
def rps():
  os.system('clear')    
  while True:
    player = None
    lists = ['rock', 'paper', 'scissors']
    computer = choice(lists)

    while player not in lists:
      player = input("rock, paper or scissors?: ")
     
    print('player chooses: ', player)
    print('computer chooses: ', computer)

    if player == computer:
             print('Tie!')
         
    if player == 'paper':
      if computer == 'rock':
        print('computer loses, player wins!')
      if computer == 'scissors':
        print('computer wins, player loses!')

    if player == 'rock':
      if computer == 'scissors':
        print('computer loses, player wins!')
      if computer == 'paper':
        print('computer wins, player loses!')

    if player == 'scissors':
      if computer == 'paper':
        print('computer loses, player winss!')
      if computer == 'rock':
        print('computer win, player lose!')

    play_again = input("Play again? yes or no: ").lower()
    if play_again != "yes".lower():
      break
    elif play_again == "yes".lower():
      os.system('clear')
def mathgame():
  global yes, no, points
  yes = "1"
  no = "0"
  points = 0
  lvllists = ["l1", "l2", "l3", "l4"]

  def lvl1():
      global yes, no, points
      while True:
          n1 = randint(0, 100)
          n2 = randint(0, 100)
          true = n1 + n2
          wrong = randint(0, 200)
          n3 = choice([true, wrong])
          
          print(f"Current point: {points}")
          print(f"{n1} + {n2} = {n3}")
          input2 = input(f"{yes} for Yes, {no} for No: ")

          if n1 + n2 == n3 and input2 == yes or n1 + n2 != n3 and input2 == no:
              points += 1
              os.system('clear')

          if n1 + n2 == n3 and input2 == no or n1 + n2 != n3 and input2 == yes:
              os.system('clear')
              print("You lost!")
              print(f"POINTS: {points}")
              print("Play again? yes or no")
              ask = input("Player:~$ ")
              if ask == "yes".lower():
                  points = 0
                  os.system('clear')
              else:
                  break

          if input2 == "//settings":
              os.system('clear')
              print("Please input your keys")
              yes = input("KEY FOR YES: ")
              no = input("KEY FOR NO: ")
              os.system('clear')

          if input2 == "//exit":
              break

          if input2 == "//changelvl":
              os.system('clear')
              changelvl()

              if chlvl == True:
                  break

  def lvl2():
      global yes, no, points
      while True:
          n1 = randint(0, 100)
          n2 = randint(0, 100)
          true = n1 - n2
          wrong = randint(0, 200)
          n3 = choice([true, wrong])
          
          print(f"Current point: {points}")
          print(f"{n1} - {n2} = {n3}")
          input2 = input(f"{yes} for Yes, {no} for No: ")

          if n1 - n2 == n3 and input2 == yes or n1 - n2 != n3 and input2 == no:
              points += 1
              os.system('clear')

          if n1 - n2 == n3 and input2 == no or n1 - n2 != n3 and input2 == yes:
              os.system('clear')
              print("You lost!")
              print(f"POINTS: {points}")
              print("Play again? yes or no")
              ask = input("Player:~$ ")
              if ask == "yes":
                  points = 0
                  os.system('clear')
              else:
                  break

          if input2 == "//settings":
              os.system('clear')
              print("Please input your keys")
              yes = input("KEY FOR YES: ")
              no = input("KEY FOR NO: ")
              os.system('clear')

          if input2 == "//exit":
              break

          if input2 == "//changelvl":
              os.system('clear')
              changelvl()

              if chlvl == True:
                  break

  def lvl3():
      global yes, no, points
      while True:
          n1 = randint(0, 100)
          n2 = randint(0, 100)
          true = n1 * n2
          wrong = randint(0, 200)
          n3 = choice([true, wrong])
          
          print(f"Current point: {points}")
          print(f"{n1} x {n2} = {n3}")
          input2 = input(f"{yes} for Yes, {no} for No: ")

          if n1 * n2 == n3 and input2 == yes or n1 * n2 != n3 and input2 == no:
              points += 1
              os.system('clear')

          if n1 * n2 == n3 and input2 == no or n1 * n2 != n3 and input2 == yes:
              os.system('clear')
              print("You lost!")
              print(f"POINTS: {points}")
              print("Play again? yes or no")
              ask = input("Player:~$ ")
              if ask == "yes":
                  points = 0
                  os.system('clear')
              else:
                  break

          if input2 == "//settings":
              os.system('clear')
              print("Please input your keys")
              yes = input("KEY FOR YES: ")
              no = input("KEY FOR NO: ")
              os.system('clear')

          if input2 == "//exit":
              break

          if input2 == "//changelvl":
              os.system('clear')
              changelvl()

              if chlvl == True:
                  break

  def lvl4():
      global yes, no, points
      while True:
          n1 = randint(0, 100)
          n2 = randint(0, 100)
          true = n1 / n2
          wrong = randint(0, 200)
          n3 = choice([true, wrong])
          print(f"Current point: {points}")
          print(f"{n1} : {n2} = {n3}")
          input2 = input(f"{yes} for Yes, {no} for No: ")

          if n1 / n2 == n3 and input2 == yes or n1 / n2 != n3 and input2 == no:
              points += 1
              os.system('clear')

          if n1 / n2 == n3 and input2 == no or n1 / n2 != n3 and input2 == yes:
              os.system('clear')
              print("You lost!")
              print(f"POINTS: {points}")
              print("Play again? yes or no")
              ask = input("Player:~$ ")
              if ask == "yes":
                  points = 0
                  os.system('clear')
              else:
                  break

          if input2 == "//settings":
              os.system('clear')
              print("Please input your keys")
              yes = input("KEY FOR YES: ")
              no = input("KEY FOR NO: ")
              os.system('clear')

          if input2 == "//exit":
              break

          if input2 == "//changelvl":
              os.system('clear')
              changelvl()

              if chlvl == True:
                  break

  def menu():
      os.system('clear')
      print("If you need to change the keys type \"//setting\" to do it")
      os.system('pause')
      os.system('clear')
      print("===LEVEL===")
      print("LEVEL 1: PLUS")
      print("LEVEL 2: MINUS")
      print("LEVEL 3: MULTIPLICATION")
      print("LEVEL 4: DIVISION")
      print("===TO INPUT THE LEVEL, TYPE IN \"l\"*level number*===")
      print("Example: Player:~$ l1")
      global opt
      opt = input("PLayer:~$ ")
      while opt not in lvllists:
          opt = input("PLayer:~$ ")
      if opt == "//settings":
          os.system('clear')
          print("Please input your keys")
          global yes, no
          yes = input("KEY FOR YES: ")
          no = input("KEY FOR NO: ")
          os.system('clear')
      
      os.system('clear')

  def changelvl():
      print("===LEVEL===")
      print("LEVEL 1: PLUS")
      print("LEVEL 2: MINUS")
      print("LEVEL 3: MULTIPLICATION")
      print("LEVEL 4: DIVISION")
      print("===TO INPUT THE LEVEL, TYPE IN \"l\"*level number*===")
      print("Example: Player:~$ l1")
      global opt
      opt = input("PLayer:~$ ")
      while opt not in lvllists:
          opt = input("PLayer:~$ ")
      if opt == "//settings":
          os.system('clear')
          print("Please input your keys")
          global yes, no
          yes = input("KEY FOR YES: ")
          no = input("KEY FOR NO: ")
          os.system('clear')
      os.system('clear')

      global chlvl
      chlvl = True

  menu()

  if opt == "l1":
      print("Type \"//changelvl\" to change level! Type \"//exit\" to exit the game!")
      os.system('pause')
      os.system('clear')
      lvl1()

  if opt == "l2":
      print("Type \"//changelvl\" to change level! Type \"//exit\" to exit the game!")
      os.system('pause')
      os.system('clear')
      lvl2()

  if opt == "l3":
      print("Type \"//changelvl\" to change level! Type \"//exit\" to exit the game!")
      os.system('pause')
      os.system('clear')
      lvl3()

  if opt == "l4":
      print("Type \"//changelvl\" to change level! Type \"//exit\" to exit the game!")
      os.system('pause')
      os.system('clear')
      lvl4()
#game selector
def funcgame():
  if inp == '/getgame'.lower():
    os.system('clear')
    print("Choose a game to play!")
    print('-----------------------------------------------------------')
    print("Built in games:")
    print("(1) Rock, paper, scissors")
    print("(2) Math game")
    print('-----------------------------------------------------------')
    print("Website games (NOTE: THESE WEBSITES CAN ONLY BE OPENED IN GOOGLE CHROME!):")
    print("(3) Roblox")
    print("(4) Chess.com")
    print("(5) Slither.io")
    print('-----------------------------------------------------------')
    gamechooser = input("GameHub$>>_ ")
    if gamechooser == '1':
        rps()
    if gamechooser == '2':
        mathgame()
    if gamechooser == '3':
        webbrowser.open('https://www.roblox.com/home')
    if gamechooser == '4':
        webbrowser.open('https://www.chess.com/')
    if gamechooser == '5':
        webbrowser.open('http://slither.io/')
# log command
def funcupdate():
  if inp == '/updatelog'.lower():
    print(f'UPDATE {update_ver}')
    print("NOW USER CAN OPEN AND READ FILES BY USING THE \'/readfile\' COMMAND")
# time
def functime():
    if inp == '/time'.lower():
        print(strftime("Clock: %H:%M:%S %p"))
        print(strftime("Date: %D"))
# screensaver
def funcscrsaver():
    if inp == '/saver'.lower():
        try:
            print("Press CTRL + C to exit the screen saver!")
            os.system('pause')
            os.system('clear')
            while True:
                print(strftime("Clock: %H:%M:%S %p"))
                print(strftime("Date: %D"))
                print(">")
                sleep(1)
                os.system('clear')
                print(strftime("Clock: %H:%M:%S %p"))
                print(strftime("Date: %D"))
                print(">>")
                sleep(1)
                os.system('clear')
                print(strftime("Clock: %H:%M:%S %p"))
                print(strftime("Date: %D"))
                print(">>>")
                sleep(1)
                os.system('clear')
        except KeyboardInterrupt:
            os.system('clear')
            return
# machine info
def funcmachineinfo():
    if inp == '/devinfo'.lower():
        my_system = uname()
        print(f"System: {my_system.system}")
        print(f"Node Name: {my_system.node}")
        print(f"Release: {my_system.release}")
        print(f"Version: {my_system.version}")
        print(f"Machine: {my_system.machine}")
        print(f"Processor: {my_system.processor}")
# opening host operating system apps
def funcopenapps():
    global inp
    if inp == "/explorer":
        print("opening explorer...")
        os.system("nautilus")

    if inp == "/chrome":
        print("opening Google Chrome...")
        webbrowser.open('https://www.google.com')

    if inp == "/youtube":
        print("opening Youtube...")
        webbrowser.open('https://youtube.com')

    if inp == "/gglphotos":
        print("opening photos...")
        webbrowser.open('https://photos.google.com')

    if inp == "/sysmonitor":
        print("opening task manager...")
        os.system('htop')
# operating system run commands
def osruncmds():
    if inp == "/HOST_SYSTEM_RUN":
        while True:
            os.system("uname -o")
            i = input('↳')
            os.system(i)

            if i == "/exit":
                os.system('clear')
                break
# opening file
def usrfile():
    if inp == "/readfile".lower():
        os.system('dir')
        print('')
        openfile = input("FILE TO OPEN (VIEW ONLY): ")
        print("")
        try:
            
            f = open(openfile, "r")
            print(f.read())
            os.system("pause")
        
        
        except FileNotFoundError:
            print('SYSTEM_ERROR: FILE NOT FOUND OR HAVING ISSUES!')
        except FileExistsError:
            print('SYSTEM_ERROR: FILE NOT FOUND OR HAVING ISSUES!')
        except OSError:
            print('SYSTEM_ERROR: FILE NOT FOUND OR HAVING ISSUES!')
#installer
def install():
    if inp == "/install":
        downloadpath = input("input your download path (default = ~)")
        if downloadpath == None:
            gitlink = input("paste your github link here: ")
            os.system(f"git clone {gitlink}")
        if downloadpath != None:
            gitlink = input("paste your github link here: ")
            os.system(f"git clone {gitlink} {downloadpath}")
# all functions
def funcs():

    helpfunc()
    
    funccmds()

    funcgame()

    funcupdate()

    functime()

    funcscrsaver()

    funcmachineinfo()

    funcopenapps()

    osruncmds()

    usrfile()

    install()
    
    return
#----------------------------------------------------------------

# MAINFRAME / TASK PERFORMANCE
opening()

while True:
    inp = input('$>_ ')
    
    funcs()

    if inp == "/exit".lower():
        break

    if inp == '/clear'.lower():
     os.system('clear')