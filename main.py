print("You are an explorer looking for treasure. You have read in ancient documents that the late King Fritz has buried all his riches somewhere in the Andes mountains. It was said he was a stingy man who left nothing for his poeple or family. After exploring them for years, you find a cave that matches the description. The treasure is hidden inside. But the path of the cave splits into three directions. Unknown dangers and rewards lie beyond each path. You must chose what adventure awaits you. ")

def start():
    choice1 = input(" Enter left, right, or middle: ")
    if choice1 == "left":
        print(
            "Wrong way, You enter the dark cave and wander off a cliff. Your adventure is over. Try again. "
        )
        start()
    elif choice1 == "right":
        right()
    elif choice1 == "middle":
        middle()
    else:
        print("You must choose left, middle, or right")
        start()
torchyesno = 0
def right():
  print("You enter a dark room full of snakes with a locked door on the other side. On the floor in the middle of the snakes is a key. Alternatively, there is a torch on the wall that you can take to see the room better. ")
  choice11 = input("Enter [key] or [torch]: ")
  if choice11 == "key": 
    global torchyesno
    torchyesno = 0
    key()
  if choice11 == "torch":
    torchyesno = 1
    torch()
  else:
    print("Invalid answer")
    right()

def torch():
  print("You pick up the torch to illuminate the room and you see another door, this one unlocked. Do you go through that door or try to get the key?")
  choice111 = input("Enter [door] or [key]: ")
  if choice111 == "door":
            middle()
  if choice111 == "key":
            key()
  else:
            print("Invalid answer")
            torch()


def key():
  print("The key is surrounded by snakes. Do you sneak past them or run through them?")
  choice112 = input("Choose [sneak] or [run]: ")
  if choice112 == "sneak":
        sneak()
  if choice112 == "run":
    run()
  else:
    print("Invalid answer")
    key()

def run():
  global torchyesno
  if torchyesno == 1:
    print("The noise you make while running alerts the snakes! You cannot get to the key in time. Do you run away back through the entrance or through the side door")
    choicerun1 = input("Choose [entrance] or [side]: ")
    if choicerun1 == "entrance":
      print("You escape through the entrance. Game over.")
      start()
    if choicerun1 == "side":
      middle()
  if torchyesno == 0:
    print("The noise you make while running alerts the snakes! You cannot get to the key in time. You must escape back through the entrance.")
    start()
      

def sneak():
  print("You sneak past the snakes, get, the key, and open the door. You enter a long hallway, and at the end is a small golden statue. You know that King Fritz left behind much more than this, and this statue might be a trap. There is also another door at the end of the hallway. Do you take the gold, which may be a trap, or ignore it and go through the door?")
  choicesneak = input("Enter [take] or [ignore]: ")
  if choicesneak == "take":
    boulder()
  if choicesneak == "ignore":
    doortwo()
  else:
    print("Invalid answer")
    sneak()

def boulder():
  print("You take the statue, but it was booby-trapped! A huge boulder starts rolling toward you! You sprint out of the cave with the gold statue in hand, but the boulder destroys everything in the cave. You leave disappointed, knowing that you could have had more treasure if you had not been so greedy as to take the statue. Game over: neutral ending")
  
def doortwo():
  print("Ignoring the small statue, you open the door and your eye are met with such riches as you had never imagined. Congratulations. If you had taken the statue, all of this treasure would have been destroyed. Since you were not greedy, you get a greater reward. Game over: good ending")


def middle():
    print(
        "You walk into a large dark room, the only things you're able to see are a sign to your right lit up by two   torches. The sign reads [To get the treasure you so seek, you must be strong not meek. YOu must take a leap.] And what seems to be a door on the far side of the room. Next to it is a similar sign lit up with a singular torch. You can't make out much but you can tell that door is your ticket to getting closer to the treasure. You take one of the torches lighting up the sign next to you and throw it across the dark room to the other side. The light reveals two planks that strech from one side of the room to the next. You must chose"
    )
    choice12 = input("Enter one or two: ")
    if choice12 == "one":
        one()
    elif choice12 == "two":
        two()
    else:
        print("Invalid answer")
        middle()


def one():
    print(
        "You shakily walk to the other side of the platform and enter through the door and...you're back at the start. Would you like to start again?"
    )
    choice13 = input("Enter yes or no: ")
    if choice13 == "yes":
        start()
    elif choice13 == "no":
        print("Game Ended")
    else:
        print("Invalid Answer")
        one()


def two():
    print(
        "You nervously crawl across the platform but lose your balance and fall off the beam! You fall for a few seconds and land in a pool of water. You have been expelled out of the cave but you see a ladder that leads back in. Do you want to leave or climb back in."
    )
    choice14 = input("Enter [l] to leave or [c] to climb into the cave: ")
    if choice14 == "l":
        l()
    elif choice14 == "c":
        c()
    else:
        print("Invalid Answer")
        two()


def l():
    print(
        "You walk back the way you came out of the cave and to the water. You leave the fortune behind"
    )
    print("Game Over")
    choiceA = input("Enter [r] to restart or [n] to end game: ")
    if choiceA == "r":
        start()
    elif choiceA == "n":
        print("Game Ended")
    else:
        print("Invalid Answer")
        l()


def c():
    print(
        "You climb back into the cave and walk a about sixty feet to a room illumeted with sunlight. Infornt of you are two pillars each with a shimmering golden goblet."
    )
    print(
        "Next to the pillars is a sign that reads[You have made it this far maybe off of intuition or luck. No matter the case the choice infront of you is clear. Pick one goblet or the other, keep in mind this choice is deathly serious."
    )
    print("Will you rely on your luck or your intuition")
    choice15 = input("Enter [i] for inspect, or [p] for lets just pick: ")
    if choice15 == "i":
        i()
    elif choice15 == "p":
        p()
    else:
        print("Invalid Answer")
        c()


def i():
    print(
        "You lean in to look at both the goblets closer you lightly blow on the first one and it doesn't budge. You do the same second and it moves just slightly. The real one is obvius"
    )
    choice16 = input("Enter first or second: ")
    if choice16 == "first":
        first()
    elif choice16 == "second":
        second()
    else:
        print("Invalid Answer")
        i()


def p():
    print("You have made it this far with a bit of luck why not keep going")
    print("pick between the first or second goblet")
    choice16 = input("Enter first or second: ")
    if choice16 == "first":
        print(
            "You confidently reach for the first goblet it is obvoiusly the real one made with pure gold. As you pick up the goblet and put it in your bag your. As you exit the cave happy with your loot the ceilling starts to crumble, large pieces start to fall and crush you to bits"
        )
    elif choice16 == "second":
        second()
    else:
        print("Invalid Answer")
        p()


def first():
    print(
        "You confidently reach for the first goblet it is obvoiusly the real one made with pure gold. As you exit the cave happy with your loot the ceilling starts to crumble, large pieces start to fall and crush you."
    )
    print("Game Over")
    choiceA = input("Enter [r] to restart or [n] to end game: ")
    if choiceA == "r":
        start()
    elif choiceA == "n":
        print("Game Ended")
    else:
        print("Invalid Answer")
        first()


def second():
    print(
        "You weren't hudred percent sure but you use your previous knowledge on the dead King Fritz. He might of been rich but he was very cautious with his riches. He would never waste precious gold on a silly cup."
    )
    print(
        "You reach for the second cup and pick it up, its light. Fools Gold! The moment the cup leaves the pillar you  hear a click. The pillar starts to lower down further into the earth, it continues to fall deeper into the cave and has yet to stop."
    )
    print(
        "Do you take a leap of faith into the dark and let the pillar take you down into the unkown. Or to you give up and leave the cave"
    )
    choice17 = input("Enter [j] for jump or [e] for exit: ")
    if choice17 == "j":
        j()
    elif choice17 == "e":
        e()
    else:
        print("Invalid Answer")
        second()


def e():
    print(
        "You walk back the way you came out of the cave and to the water. You leave the fortune behind"
    )
    print("Game Over")
    choiceA = input("Enter [r] to restart or [n] to end game: ")
    if choiceA == "r":
        start()
    elif choiceA == "n":
        print("Game Ended")
    else:
        print("Invalid Answer")
        e()


def j():
    print(
        "You jump down onto the pillar and allow it to go further down for roughly 2 minutes. The pillar stops perfectly in the ground."
    )
    print(
        "The moment the pillar snapped into place the room lit up with torches streched along the wall. Surrounding you are piles of gold, diamonds, crystals, and more. Yu finally found the treasure!"
    )
    print(
        "A sign to the right of you reads the following [So you are the worthy adevnturer that finally found my treasure] A message from King Fritz! It continues: [I have no knowledge of how long it has been since my passing but this room contains roughly 10 million of my time] King Fritz's era was in the 15th century, so that must be well over a billion dollars today!"
    )
    print(
        "King Fritz's message goes on [The challenges I have laid out for you involve skill and intelegance. But that are not the only factors that determine a great man. You most be wise with your money and you can only go so far in life with lady luck on your side. I hope this message reaches the right person]"
    )
    print(
        "You have won your riches through luck determination, and skill. The only question left is how do you transport your riches out of the cave."
    )
    print("Game Finished!")


start()
