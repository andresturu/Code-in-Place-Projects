
def main():
    num_stones = 20 #initialize the number of stones in the beginning variable
    turn_counter = 0 #initialize the turn_counting variable

    while num_stones > 0:
        
        if turn_counter == 0:
            current_player = "Player 1"
            turn_counter = turn_counter + 1 #changes value to 1 so that player 2 is next
        elif turn_counter == 1:
            current_player = "Player 2"
            turn_counter = turn_counter -1. #changes value to 0 so that player 1 is next
        

        print (f"There are {num_stones} stones left.")
        stones_taken = int(input(f"{current_player} would you like to remove 1 or 2 stones? "))
        while (stones_taken != 1) and (stones_taken !=2):
            stones_taken= int(input("Please enter 1 or 2: "))
        num_stones = num_stones - stones_taken
        print("")

    if turn_counter == 1:
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")




if __name__ == '__main__':
    main()