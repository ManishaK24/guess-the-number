'Python Project.py'
'Python Project 7.py'
print('Guess the number game (randomly generated numbers).')
# Import the random module, and display a random number from 0 to 100.
import random
secret_number = int(random.randint(1,100))
input_count = 0
# Start the while loop
while True:
    current_input = int(input('Provide your guess between 1 to 100: '))
    if current_input < 0 or current_input > 100: # needed "or" logic operator not "and" logic operator.
        print('Please provide a number within the range [0,100].')
    # provide feed back on how close the user guess is to the random secret number.
    distance = abs(secret_number - current_input) # TODO
    if distance >= 20: 
        print('Very cold')
    if distance < 15 and distance > 10:
        print('Cold') # TODO
    if distance < 10 and distance > 5:
        print('Hot')
    if distance <= 5:
        print('Very hot')                    
    if current_input == secret_number:
        break
    input_count += 1
print(f'Congrats! The secret was {secret_number}. You found the secret after {input_count} attempts.')


      
       
            
          