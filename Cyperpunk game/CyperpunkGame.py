print('''            _                                 _    
           | |                               | |   
  ___ _   _| |__   ___ _ __ _ __  _   _ _ __ | | __
 / __| | | | '_ \ / _ \ '__| '_ \| | | | '_ \| |/ /
| (__| |_| | |_) |  __/ |  | |_) | |_| | | | |   < 
 \___|\__, |_.__/ \___|_|  | .__/ \__,_|_| |_|_|\_\
       __/ |               | |                     
      |___/                |_|                     
''')
print("Wake The Fuck Up Samurai We have a city to burn")
choice1 = input("Your sitting on a lawn chair on a roof over looking Night-City. Times Running out you've 3 choices Either call Panam or Rouge or End It Here. type 'Panam','Rogue' or 'End Here'. \n").lower()
if choice1 == "panam":
  choice2 = input("You've called Panam and have decided to use here dusty nomad family to storm Arasaka Hq. As you push your way through the door your left with a choice corridor or elevator type 'corridor' or 'elevator'. \n ").lower()
elif choice1 == "rogue":
      print("You and Rogue run into Adam Fucking Smasher and got zero'd Game Over. ")
if choice2 == "elevator":
    choice3 = input("You've made your way to Mikoshi you plug in and are given a choice V or Johnny. type 'V' or 'Johnny'. \n ").lower()
    if choice3 == "v":
     print("Congrats You chose to live. The End ")
    elif choice2 == "corridor":
       print(" You and Panam ran into Adam Fucking Smasher and got zero'd Game Over. ")
    else: 
     print("you've chosen to let johnny take you body. The End")
else:
 print("I'm disappointed you chose the easy way out. fucking coward. Game Over. ")