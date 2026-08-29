from random import choice, shuffle


# -------------------- PLAYERS --------------------

people = []

while True:
    try:
        num = int(input("Enter how many people are gonna play the game? "))

        if num > 0:
            break
        else:
            print("Please enter a number greater than 0.")

    except ValueError:
        print("Please enter a number.")


# Get and validate each player's name
for _ in range(num):
    while True:
        name = input(f"Enter player {_ + 1} name: ").strip().title()

        if name.replace(" ", "").isalpha():
            people.append(name)
            break
        else:
            print("Please enter letters only.")


# -------------------- TRUTH QUESTIONS --------------------

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


# -------------------- DARES --------------------

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


# Keep a copy of the original questions and dares.
# These are used to refill a list when all items have been used.
original_easy_truth = easy_truth.copy()
original_medium_truth = medium_truth.copy()
original_hard_truth = hard_truth.copy()

original_easy_dare = easy_dare.copy()
original_medium_dare = medium_dare.copy()
original_hard_dare = hard_dare.copy()


# Shuffle players so their order changes every game
shuffle(people)


# Give every player an initial score of 0
scores = {}

for person in people:
    scores[person] = 0


# -------------------- GAME SETUP --------------------

print("==============================")
print("      🎲 TRUTH OR DARE 🎲      ")
print("==============================")


while True:
    try:
        rounds = int(input("Enter how many rounds you wanna play: "))

        if rounds > 0:
            break
        else:
            print("Please enter a number greater than 0.")

    except ValueError:
        print("Please enter a number.")


game_over = False


# -------------------- GAME LOOP --------------------

for round_number in range(rounds):

    print(f"\n========== ROUND {round_number + 1} ==========")

    for chance in people:

        input("\nPress ENTER to continue...")

        what = choice(["Truth", "Dare"])


        # -------------------- TRUTH --------------------

        if what == "Truth":

            print(f"\n{chance} → TRUTH")

            while True:

                enter = input(
                    "Enter command (E for Enter, S for Skip, Q for Quit): "
                ).lower()

                if enter == "e":

                    difficulty = input(
                        "Enter your difficulty level (1, 2, 3): "
                    )

                    match difficulty:

                        case "1":

                            # Refill the list if all easy questions were used
                            if not easy_truth:
                                easy_truth.extend(original_easy_truth)

                            question = choice(easy_truth)
                            easy_truth.remove(question)


                        case "2":

                            if not medium_truth:
                                medium_truth.extend(original_medium_truth)

                            question = choice(medium_truth)
                            medium_truth.remove(question)


                        case "3":

                            if not hard_truth:
                                hard_truth.extend(original_hard_truth)

                            question = choice(hard_truth)
                            hard_truth.remove(question)


                        case _:

                            print("Please enter 1, 2, or 3.")
                            continue


                    print(f"\nQuestion: {question}")

                    answer = input("Your answer: ")

                    # A player earns a point after answering the Truth
                    scores[chance] += 1

                    print(f"{chance} earned 1 point! 🏆")

                    break


                elif enter == "s":

                    print("Skipped!")
                    break


                elif enter == "q":

                    print("Game ended!")
                    game_over = True
                    break


                else:

                    print("Please enter a correct command.")


        # -------------------- DARE --------------------

        else:

            print(f"\n{chance} → DARE")

            while True:

                enter = input(
                    "Enter command (E for Enter, S for Skip, Q for Quit): "
                ).lower()

                if enter == "e":

                    difficulty = input(
                        "Enter your difficulty level (1, 2, 3): "
                    )

                    match difficulty:

                        case "1":

                            if not easy_dare:
                                easy_dare.extend(original_easy_dare)

                            work = choice(easy_dare)
                            easy_dare.remove(work)


                        case "2":

                            if not medium_dare:
                                medium_dare.extend(original_medium_dare)

                            work = choice(medium_dare)
                            medium_dare.remove(work)


                        case "3":

                            if not hard_dare:
                                hard_dare.extend(original_hard_dare)

                            work = choice(hard_dare)
                            hard_dare.remove(work)


                        case _:

                            print("Please enter 1, 2, or 3.")
                            continue


                    print(f"\nDare: {work}")


                    # Player decides whether they completed the dare
                    while True:

                        done = input(
                            "Are you done? (D for Done, N for Not done): "
                        ).lower()

                        if done == "d":

                            scores[chance] += 1

                            print(
                                f"{chance} earned 1 point! 🏆"
                            )

                            break


                        elif done == "n":

                            print(
                                f"{chance}, you didn't earn a point."
                            )

                            break


                        else:

                            print("Please enter D or N.")


                    break


                elif enter == "s":

                    print("Skipped!")
                    break


                elif enter == "q":

                    print("Game ended!")
                    game_over = True
                    break


                else:

                    print("Please enter a correct command.")


        # Stop the current round if Q was selected
        if game_over:
            break


    # Stop all remaining rounds if Q was selected
    if game_over:
        break


# -------------------- FINAL SCOREBOARD --------------------

print("\n==============================")
print("        🏆 SCOREBOARD 🏆")
print("==============================")


for person, score in scores.items():
    print(f"{person}: {score} point(s)")


print("\n🎮 Game Over!")
print("Thanks for playing!")