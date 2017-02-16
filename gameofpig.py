# [Assignment-2] The Game of Pig
# Developed by Shayan Bozorgmanesh (10023332), 2017
# Special thanks to CISC101 Prof Alan McLeod

# This program allows a user to play a computer in The Game of Pig.
# Uses two dices, and traditional rules of the game.
# First one to score 100 wins!
# More information on the game can be found at: 
# https://en.wikipedia.org/wiki/Pig_%28dice_game%29

#   module
from random import randint

def main():
    RESET_SCORE = 0
    terminate = False
    endTurn = False
    AI = "Watson"
    userRoundScore = 0
    userTotalScore = 0
    AITotalScore = 0
    game_over = False

    #   program greeting
    print("Hello, we're going to play The Game of Pig, versus {}!".format(AI))
    user = input("What is your name?: ")
    print("\nNice to meet you, {}. Are you ready to play?".format(user))
    startGame = input("Type 1 if you are ready. "\
                          "Type 0 if you need more time: ")

    while startGame != "1":
        if startGame == "0":
            startGame = input("\nHmmm, {}.\nI need you to be ready if you " \
                              "want to beat {}.\n" \
                              "Press 1 when you are ready, "\
                              "master!\n".format(user, AI))
        else:
            startGame = input("Please Type 1 if you are ready, " \
                              "Type 0 if you need more time: ")


    print("\nLet the game begin! {0} versus {1}!\n".format(user, AI))
    print("{} goes first.".format(user))

    turn = 0

    #   start game
    while not game_over:
        RESET_SCORE = 0
        turn = turn + 1
        #   print turn; scores
        print("\n\n###########")
        print("###########")
        print("###########\n\n")
        roll = input("Turn {0} - {1}: {2} v.s. {3}: {4}" \
                     "\n\nPress <ENTER> to continue\n".format(turn, user, 
                                                              userTotalScore, 
                                                              AI, 
                                                              AITotalScore))

        if roll != "":
            roll = input("Press <ENTER> to continue.")
        userEndTurn = False
        AIEndTurn = False
        userRoundScore = 0
        AIRoundScore = 0

        #   rules of the game; including scores, rerolls (user)
        while userEndTurn == False:
            dice_one = randint(1,6)
            dice_two = randint(1,6)
            print("\nYou Roll...")
            print(dice_one, dice_two)
            #   conditional rules based on dice rolls
            if dice_one == 1 and dice_two == 1:
                print("Your total score resets and you lose your turn.")
                print("Sorry, {0}.".format(user))
                userRoundScore = RESET_SCORE
                userTotalScore = RESET_SCORE
                print("\n{0}'s score this round: {1}"
                      .format(user, userRoundScore))
                print("{0}'s total score: {1}".format(user, userTotalScore))
                userEndTurn = True
                break

            elif dice_one == 1 or dice_two == 1:
                print("\nOuch! You rolled a one.")
                print("You lose all the points gained in this round " \
                      "and your turn is over.")
                print("Sorry, {0}.".format(user))
                if turn == 1 or userTotalScore <= userRoundScore:
                    userRoundScore = RESET_SCORE
                    userTotalScore = userRoundScore
                else:
                    userTotalScore = userTotalScore - userRoundScore
                    userRoundScore = RESET_SCORE
                print("\n{0}'s score this round: {1}"
                      .format(user, userRoundScore))
                print("{0}'s total score: {1}".format(user, userTotalScore))
                userEndTurn = True
                break

            elif dice_one == dice_two:
                print("\nInteresting...You rolled matching numbers! " \
                      "Roll again!\n")
                roll_again = input("Press <ENTER> to roll again! ")
                while roll_again != "":
                    roll_again = input("Press <ENTER> to roll " 
                                       "again! ")

            else:
                print("\nGreat roll, {0}!".format(user))
                if turn == 1 or userTotalScore <= userRoundScore:
                    userRoundScore = dice_one + dice_two + userRoundScore
                    userTotalScore = userRoundScore 
                else:
                    userRoundScore = dice_one + dice_two + userRoundScore
                    userTotalScore = userTotalScore + dice_one + dice_two
                print("{0}'s score this round: {1}"
                      .format(user, userRoundScore))
                print("{0}'s total score: {1}".format(user, userTotalScore))
                #   if user scores >= 100, game is over
                if userTotalScore >= 100:
                    userEndTurn = True
                    AIEndTurn = True
                    game_over = True
                    break
                #   else ask user about rerolling
                else:
                    print("\nRoll again or end turn?")
                    roll = input("Type 'Y' to roll again. " \
                                 "Type 'N' to end your turn. ")
                    while roll != "Y" and roll != "N":
                        print("Invalid Entry.")
                        roll = input("Type 'Y' to roll again. " \
                                     "Type 'N' to end your turn. ")
                    if roll == "Y":
                        userEndTurn = False
                    else:
                        userEndTurn = True
        #   if user doesn't reroll, start computer's turn
        if roll == "N" or userEndTurn == True and AIEndTurn == False:
            AIEndTurn = False
            print("\nWatson's turn!\n")
            roll_again = input("Press <ENTER> to " \
                               "continue\n")
            while roll_again != "":
                roll_again = input("Press <ENTER> to " \
                                   "continue\n")

        #   rules of the game; including scores, rerolls (computer)
        while userEndTurn == True and AIEndTurn == False:
            print("{} rolls...".format(AI))
            dice_one = randint(1,6)
            dice_two = randint(1,6)
            print(dice_one, dice_two)
            #   conditional rules based on dice rules
            if dice_one == 1 and dice_two == 1:
                print("\nWoah! Double ones.")
                print("Watson's total score resets and "\
                      "loses its turn!")
                AIRoundScore = RESET_SCORE
                AITotalScore = RESET_SCORE
                print("\n{0}'s score this round: {1}"
                      .format(AI, AIRoundScore))
                print("{0}'s total score: {1}"
                      .format(AI, AITotalScore))
                AIEndTurn = True            
                break

            elif dice_one == 1 or dice_two == 1:
                print("\nOh! {0} rolled a one!".format(AI))
                print("{0} loses all points gained in this "\
                      "round and its turn is over.".format(AI))
                if turn == 1 or AITotalScore <= AIRoundScore:
                    AIRoundScore = RESET_SCORE
                    AITotalScore = AIRoundScore
                else:
                    AITotalScore = AITotalScore - AIRoundScore
                    AIRoundScore = RESET_SCORE
                print("\n{0}'s score this round: {1}"
                      .format(AI, AIRoundScore))
                print("{0}'s total score: {1}\n"
                      .format(AI, AITotalScore))
                AIEndTurn = True
                break
            
            elif dice_one == dice_two:
                print("\nInteresting...matching numbers!".format(AI))
                print("Roll again, {0}!\n".format(AI))

            else:
                print("\nOh dear, {}'s good...".format(AI))
                if turn == 1 or AITotalScore <= AIRoundScore:
                    AIRoundScore = AIRoundScore + dice_one + dice_two
                    AITotalScore = AIRoundScore 
                else:
                    AIRoundScore = AIRoundScore + dice_one + dice_two
                    AITotalScore = AITotalScore + dice_one + dice_two
                print("{0}'s score this round: {1}"
                      .format(AI, AIRoundScore))
                print("{0}'s total score: {1}\n"
                      .format(AI, AITotalScore))
            #   if computer total score >= 100, end game
            if AITotalScore >= 100:
                AIEndTurn = True
                userEndTurn = True
                game_over = True
                break
            #   else if computer round score >= 20, end turn
            else:
                if AIRoundScore >= 20:
                    AIEndTurn = True
    #   game over, display winner
    if game_over:
        if userTotalScore >= 100:
            print("\n**********")
            print("GAME OVER")
            print("**********\n")
            print("Congratulations, {}!".format(user))
            print("You reached 100!\n")
        else:
            print("\n**********")
            print("GAME OVER")
            print("**********\n")
            print("Oh no....")
            print("{} beat you to 100.\n".format(AI))
main()
