import random

attempts = []


def show_score():
    if len(attempts) <= 0:
        print("There's currently no high score, keep going!")
    else:
        print('Current high score is {} attempts'.format(min(attempts)))


def start_game():
    number = int(random.randint(1, 10))
    print("Hello, Master, welcome to the game of guesses;)")
    player_name = input("What's your name, traveller? ", )
    wanna_play = input("Greetings, {}, would you like yo play a game? (Enter yes/no) ".format(player_name), )
    attempt_counter = 0
    show_score()
    while wanna_play.lower() == ("yes"):
        try:
            guess = input("Choose a number between 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please, pick a number within the given range")
            if int(guess) == int(number):
                print("Woah, you got it! The number was {}".format(number))
                attempt_counter += 1
                print("It took you {} attempt(s).".format(attempt_counter))
                attempts.append(attempt_counter)
                play_again = input("Would you like to play again? (Enter Yes/No) ", )
                attempt_counter = 0
                show_score()
                number = int(random.randint(1, 10))
                if play_again.lower() == ('no'):
                    print("It's cool, have a good day!")
                    break
            elif int(guess) > int(number):
                attempt_counter += 1
                print("Hidden numbber is lower!")
            elif int(guess) < int(number):
                attempt_counter += 1
                print("Hidden number is higher!")
        except ValueError as err:
            print("Oh no, thats not valiid value! Please try again...")
            print("{}".format(err))
    else:
        print("No problem, Dude =)")


start_game()
