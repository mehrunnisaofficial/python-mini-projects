"""
Code Pseudocode
Each part should be done in seperate function for readability
- Take input of how many people wanna play the game
- Take input of their names
- Make truth Questions
- Make dare question 
"""



# nop = No. of Players
# tnop = Total No. of Players
# pn = Players Name
# tr = total rounds
from random import choice, shuffle

def players_number():
    while True:
        try:
            nop = int(input("Enter how many People are playing the Truth and Dare game: "))

            if nop <= 0:
                print('Enter Valid Number of players\n"Are you stupid, how 0 or less than 0 gonna play game?"')
            else:
                return nop
        except ValueError:
            print("Please enter numbers sir/ma'am")

def playes_list():
    tnop = players_number()
    pn = []
    count = 0
    print(f"Total number of players: {tnop}")

    for players in range(tnop):
        while True:
                name = input(f"Enter player {players + 1} name: ").strip().title()
        
                if name.replace(" ", "").isalpha():
                    pn.append(name)
                    break
                else:
                    print("Please enter letters only.")
        count += 1

    if count == tnop:
        return pn

def truth():
    easy_truth = [
        "What is one thing you are scared of?",
        "What is the funniest nickname someone has given you?",
        "What is the most childish thing you still do?",
        "Who in this group knows you the best?",
        "What is your favorite thing to do when you're bored?",
        "What is the weirdest food you have ever eaten?",
        "What is your favorite movie or show?",
    ]

    medium_truth = [
        "Who is your crush?",
        "Who was your first crush?",
        "Have you ever lied to your best friend?",
        "Have you ever sent a message to the wrong person?",
        "Have you ever pretended to be sick to skip something?",
        "What is the most embarrassing thing you've ever done?",
        "What is the weirdest thing you have ever searched online?",
    ]

    hard_truth = [
        "What is your biggest secret?",
        "What is the biggest lie you've ever told your parents?",
        "What is something you've never told anyone in this room?",
        "Have you ever blamed someone else for something you did?",
        "Have you ever sneaked out of this class?",
        "Which teacher's class is the most boring?",
        "What is the most awkward moment you've ever experienced?",
    ]


def dare():
    easy_dare = [
        "Smile for 10 seconds.",
        "Make a funny face and hold it for 10 seconds.",
        "Tell everyone a really bad joke.",
        "Clap 10 times dramatically.",
        "Say your name backwards.",
        "Compliment the person sitting next to you.",
    ]

    medium_dare = [
        "Dance for 30 seconds without music.",
        "Sing the chorus of your favorite song.",
        "Do 10 jumping jacks.",
        "Talk in a funny voice for one minute.",
        "Walk around like a robot for one minute.",
        "Act like your favorite cartoon character.",
        "Tell a story using only five words.",
    ]

    hard_dare = [
        "Go and shake hands with your crush.",
        "Imitate a teacher for 30 seconds.",
        "Say the alphabet backwards as far as you can.",
        "Do your best celebrity impression.",
        "Pretend to be a news reporter and report what is happening in the room.",
        "Try to make everyone laugh in 30 seconds.",
        "Speak only in questions for the next two minutes.",
        "Do your best dramatic movie scene.",
        "Pretend the floor is lava for 30 seconds.",
        "Let the group choose a funny word that you must use in every sentence for one minute.",
    ]

def how_many_round():
    while True:
        try:
            times = int(input("Enter how round u wanna play this game: "))  

            if times > 0:
                return times
            else:
                print("Please enter number more than 0")

        except ValueError:
            print("Please Enter a Valid Number")

def game_start():
    tr = how_many_round()

    for total_round in range(tr):
        print(f"\n========== ROUND {total_round + 1} ==========")

        for chance in playes_list():

            input("\nPress ENTER to continue...")

            what = choice(["Truth", "Dare"])
            