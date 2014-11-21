def binary_search():
    start = 0
    end = 100
    answer = ''
    
    print("Please think of a number between 0 and 100!")
    
    while (answer != 'c'):
        secret_number = (end + start) / 2
        print("Is your secret number " + str(secret_number) + "?")
        answer = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        
        if answer == 'h':
            end = secret_number
        elif answer == 'l':
            start = secret_number
        elif answer == 'c':        
            break;
        else:
            print("Sorry, I did not understand your input.")
            continue
            
    print("Game over. Your secret number was: " + str(secret_number))