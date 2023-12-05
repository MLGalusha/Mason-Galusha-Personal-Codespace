import random  # Import the 'random' module to generate random numbers

def main():
    level = get_level()  # Get the level from the user
    score = simulate_game(level)  # Simulate the game and get the score
    print(f"Score: {score}")  # Print the final score

def get_level():
    while True:
        try:
            level = int(input("Level: "))  # Attempt to convert user input to an integer
            if level in [1, 2, 3]:  # Check if the input is one of the valid levels (1, 2, or 3)
                break  # Break out of the loop if the level is valid
        except:
            pass  # Ignore exceptions (e.g., non-integer input) and continue the loop
    return level  # Return the chosen level

def generate_integer(level):
    if level == 1:
        x = random.randint(1, 9)
        y = random.randint(1, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y  # Return the generated integers

def simulate_round(x, y):
    count_tries = 1
    while count_tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))  # Get the user's answer
            if answer == (x + y):  # Check if the answer is correct
                return True  # Return True if the answer is correct
            else:
                count_tries += 1  # Increment the number of tries and print an error message
                print("EEE")
        except:
            count_tries += 1  # Increment the number of tries and print an error message for non-integer input
            print("EEE")
    print(f"{x} + {y} = {x + y}")  # If the user fails to answer correctly after 3 tries, print the correct answer and return False
    return False

def simulate_game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x, y = generate_integer(level)  # Generate random integers for the round based on the chosen level
        response = simulate_round(x, y)  # Simulate a round and get the user's response
        if response == True:  # If the response is True (correct answer), increment the score
            score += 1
        count_round += 1  # Increment the round counter
    return score  # Return the final score

if __name__ == "__main__":
    main()  # Call the main function
