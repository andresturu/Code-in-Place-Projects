import random


NUM_PAIRS = 3

def main():
    truth_list = []
    for i in range (NUM_PAIRS):
        truth_list.append(i)
        truth_list.append(i)
    random.shuffle(truth_list)
    display_list = ['*', '*', '*', '*', '*', '*']
    
    while is_still_playing(display_list):
        print(display_list)
        first_index = get_valid_index(display_list, None)
        second_index = get_valid_index(display_list, first_index)

        
        if is_match: #(truth_list, first_index, second_index): for some reason this stuff isn't necessary?
            print("Match!")
            display_list[first_index] = truth_list[first_index]
            display_list[second_index] = truth_list[second_index]
        else:
            print(f"Value at index {first_index} is {truth_list[first_index]}")
            print(f"Value at index {second_index} is {truth_list[second_index]}")
            print("No match. Try again.")
            input("Press Enter to continue...")     
        clear_terminal()
    
    print(truth_list)
    print("Congratulations! You won!")

def is_still_playing(display_list):
    counter = 0
    for elem in display_list:
        if elem == '*':
            counter += 1
    if counter != 0:
        return True
    else:
        return False



def is_match(truth_list, first_index, second_index):
    first_value = truth_list[first_index]
    second_value = truth_list[second_index]
    if first_value == second_value:
        return True
    else:
        return False

def get_valid_index(display_list, previous_index):
    while True:
        chosen_index = input("Enter an index: ")
        try: #checks for an error
            chosen_index = int(chosen_index) #also covers floats which, even though they are numbers just not ints
            
        except ValueError: #if the error was a ValueError, then print this, if not it skips
            print("Not a number. Try again.")
            
        else: # only runs if no exceptions, if input is really a string, then this code block won't run and it will prompt the user to enter another input
            if chosen_index == previous_index:
                print("You entered the same index twice. Try again.")
                
            elif (0<= chosen_index < len(display_list)) and (display_list[chosen_index] == '*'): 
                return chosen_index
            elif chosen_index > (len(display_list) -1) or chosen_index < 0:
                    print("Invalid index. Try again.")
        


def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()